from scapy.all import *
from collections import defaultdict
from threading import Thread
import psutil
import os
import socket
import json

# Endereço da máquina local
HOST = "0.0.0.0"

# Portas efêmeras utilizadas para comunicação por socket
PORT_NETWORK_TRAFFIC = 50_000

# Intervalo de esgotação (em segundos) para todos os sockets
SOCKET_TIMEOUT = 30

# Atraso padrão (em segundos) para envio de informação 
# Esse atraso é compartilhado entre todas as funções que enviam informações via comunicação por socket
# Ele NÃO afeta a taxa de captura de pacotes do Scapy 
INFO_DELAY = 1

# Variável que armazena todas as interfaces de rede disponíveis
all_macs = set()

for iface in psutil.net_if_addrs():
    try:
        mac = psutil.net_if_addrs()[iface][0].address.lower()
        if(os.name == "nt"):
            mac = mac.replace("-", ":")
    except:
        mac = psutil.net_if_addrs()[iface][0].address
    finally:
        all_macs.add(mac)

# Dicionário que mapeia cada conexão com o seu respection ID de processo (PID)
connection2pid = {}

# Dicionário que mapeia cada PID a um total de tráfego de Upload (0) e Download(1)
pid2process_class = {}

# Global boolean for status of the program
is_program_running = True

class Process:
    def __init__(self, pid, name, create_time, last_time_updated, upload, download):
        self.pid = pid
        self.name = name
        self.create_time = create_time
        self.last_time_updated = last_time_updated
        self.upload = upload
        self.download = download
        self.upload_speed = 0
        self.download_speed = 0
        self.protocol_traffic = defaultdict(lambda: [0,0])
        self.hosts_traffic = defaultdict(lambda: [0,0])

    def update_last_time_updated(self, new_time):
        self.last_time_updated = new_time

    def update_download(self, new_download: float):
        self.download += new_download
    
    def update_upload(self, new_upload: float):
        self.upload += new_upload

    def update_download_speed(self, new_download: float):
        self.download_speed = new_download
    
    def update_upload_speed(self, new_upload: float):
        self.upload_speed = new_upload

    def update_protocol_traffic(self, new_protocol_traffic: dict):
        protocol = list(new_protocol_traffic.keys())[0]

        self.protocol_traffic[protocol][0] += new_protocol_traffic[protocol][0] # Download
        self.protocol_traffic[protocol][1] += new_protocol_traffic[protocol][1] # Upload

    def update_hosts_traffic(self, new_hosts_traffic: dict):
        host = list(new_hosts_traffic.keys())[0]

        self.hosts_traffic[host][0] += new_hosts_traffic[host][0] # Download
        self.hosts_traffic[host][1] += new_hosts_traffic[host][1] # Upload
    
    def to_JSON(self):
        json_data = f'''{{
        "pid": "{self.pid}",
        "name": "{self.name}",
        "create_time": "{self.create_time}",
        "last_time_update": "{self.last_time_updated}",
        "upload": "{get_size(self.upload)}",
        "download": "{get_size(self.download)}",
        "upload_speed": "{get_size(self.upload_speed)}/s",
        "download_speed": "{get_size(self.download_speed)}/s",
        '''
        json_data += ''' "protocol_traffic": [ '''
        for protocol, traffic in self.protocol_traffic.items():
            json_data += f'''{{
            "protocol": "{protocol}",
            "download": "{get_size(traffic[0])}",
            "upload": "{get_size(traffic[1])}"
            '''
            if(protocol != list(self.protocol_traffic.keys())[-1]):
                json_data += ''' },'''
            else:
                json_data += ''' }'''

        
            
        json_data += ''' ], '''
    
        json_data += ''' "host_traffic": [ '''
        for host, traffic in self.hosts_traffic.items():
            json_data += f'''{{
            "host": "{host}",
            "download": "{get_size(traffic[0])}",
            "upload": "{get_size(traffic[1])}"
            '''
            if(host != list(self.hosts_traffic.keys())[-1]):
                json_data += ''' },'''
            else:
                json_data += ''' }'''
        
        json_data += ''']
        }'''

        json_object = json.loads(json_data)
        json_formatted_str = json.dumps(json_object, indent=4)

        return json_formatted_str
        #return json.dumps(self, default= lambda o: o.__dict__, sort_keys=True, indent=4)

def get_size(bytes : int):
    """
    Returns the formatted size of bytes, up to Petabytes
    """

    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

def get_connection():
    """A function that keeps listening for connections on this machine 
    and adds them to `connection2pid` dict"""

    global connection2pid
    # While is_program_running:
        # Using psutil, we can grab each connection's source and destination ports
        # And their process ID
    for c in psutil.net_connections():
        if c.laddr and c.raddr and c.pid:
            # If local address, remote address and PID are in the connection
            # Add them to our global dictionary
            connection2pid[(c.laddr.port, c.raddr.port)] = c.pid
            connection2pid[(c.raddr.port, c.laddr.port)] = c.pid

def get_traffic_data(packet : Packet):
    """
    Maps each connection to a process ID and store this information along with download/upload statics into the `pid2traffic` dict
    """
    global pid2traffic
    global pid2process_class

    upload = 0
    download = 0
    protocol = defaultdict(lambda: [0, 0])
    host = defaultdict(lambda: [0, 0])

    is_source = False
    protocol_port = 0
    host_ip = ""

    packet_size = len(packet)

    try:
        # Get the packet source & destination IP addresses and ports
        packet_connection = (packet.sport, packet.dport)
    except (AttributeError, IndexError):
        # Sometimes the packet does not have TCP/UDP layers, we just ignore these packets
        pass
    else:
        # Get the PID responsible for this connection from our `connection2pid` global dictionary
        packet_pid = connection2pid.get(packet_connection)
        if packet_pid:
            try:
                # Get process related to the PID
                p = psutil.Process(packet_pid)
            except (ProcessLookupError, psutil.NoSuchProcess):
                # If the process was closed, we ignore this packet
                pass
            else:
                if packet.src in all_macs:
                    # The source MAC address of the packet is our MAC address
                    # So it's an outgoing packet, meaning it's upload
                    is_source = True
                    upload = packet_size
                    protocol_port = packet_connection[1]
                    host_ip = packet[IP].dst
                else:
                    # Incoming packet, download
                    download = packet_size
                    protocol_port = packet_connection[0]
                    host_ip = packet[IP].src
                
                protocol_name = IP().get_field("proto").i2s[packet[IP].proto]

                try:
                    service_name = socket.getservbyport(protocol_port, protocol_name)
                except OSError:
                    # "socket.getservbyport" has a limited amount of port-protocol combinations. If none match, we simply label the service as "others"
                    service_name = "others"
                
                if not is_source:
                    protocol[service_name][0] = packet_size
                    protocol[service_name][1] = 0
                    host[host_ip][0] = packet_size
                    host[host_ip][1] = 0
                else:
                    protocol[service_name][0] = 0
                    protocol[service_name][1] = packet_size
                    host[host_ip][0] = 0
                    host[host_ip][1] = packet_size
                
                new_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

                if not update_process(packet_pid, new_time, upload, download, protocol, host):
                    try:
                        create_time = datetime.fromtimestamp(p.create_time())
                    except OSError:
                        # System processes, using boot time instead
                        create_time = datetime.fromtimestamp(psutil.boot_time())
                    
                    create_time = create_time.strftime("%d/%m/%Y, %H:%M:%S")

                    try:
                        pid2process_class[packet_pid] = Process(packet_pid, p.name(), create_time, new_time, upload, download)
                    except psutil.NoSuchProcess:
                        pass

def json_serialize_traffic_data():
    process_list_data = '''['''
    for process in list(pid2process_class):
        process_list_data += pid2process_class[process].to_JSON()
        
        if(process != list(pid2process_class.keys())[-1]):
            process_list_data += ''','''
        
    process_list_data += ''']'''

    json_object = json.loads(process_list_data)
    json_formatted_str = json.dumps(json_object, indent=4)

    return json_formatted_str
 

def update_process(pid, new_time: str, upload: float, download: float, protocol: dict, host: dict) -> bool:

    global pid2process_class

    if pid in pid2process_class.keys(): # PID exists in the dictionary, therefore we update the process
        current_process = pid2process_class[pid]

        current_process.update_last_time_updated(new_time)
        current_process.update_upload(upload)
        current_process.update_download(download)
        current_process.update_upload_speed(upload)
        current_process.update_download_speed(download)
        current_process.update_protocol_traffic(protocol)
        current_process.update_hosts_traffic(host)

        pid2process_class[pid] = current_process

        # All updated, return true
        return True 
    
    # PID doesn't exist, return false to create a new Process
    return False

def send_traffic_data():
    """
    Sends all protocol/network statistics by socket communication.
    This function runs in its Thread to optimize performance and allow parallel socket connections.
    """

    protocol_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        protocol_socket.bind((HOST, PORT_NETWORK_TRAFFIC))
    except OSError:
        print("Port",PORT_NETWORK_TRAFFIC,"already in use, unable to bind port to socket.")
    else:
        protocol_socket.listen(1)
        print("Waiting for client connection on port", PORT_NETWORK_TRAFFIC, "for streaming network usage per protocol.")
    
        client_socket, client_address = protocol_socket.accept()
        print("Client connected on", client_address, ". Now streaming network usage per protocol.")

        protocol_socket.settimeout(SOCKET_TIMEOUT)

        while is_program_running:
            time.sleep(INFO_DELAY)
            json = json_serialize_traffic_data()

            response = (
                'HTTP/1.1 200 OK\r\n'
                'Content-Type: application/json\r\n'
                'Access-Control-Allow-Origin: *\r\n'
                'Access-Control-Allow-Headers: Content-Type\r\n'
                'Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n'
                f'Content-Length: {len(json)}\r\n'
                '\r\n'
                f'{json}\r\n'
            )

            try:
                client_socket.sendall(response.encode())
            except (ConnectionResetError, ConnectionRefusedError, ConnectionAbortedError, BrokenPipeError):
                print(f"Connection problem on port {PORT_NETWORK_TRAFFIC}")
                client_socket, client_address = attempt_socket_reconnection(protocol_socket, PORT_NETWORK_TRAFFIC, 5)
                if(client_socket == False):
                    print("Connection aborted by client, closing thread.")
                    break
                else:
                    print("Connection reestablished.")
                    continue
        
        protocol_socket.close()

def attempt_socket_reconnection(task_socket: socket, port: int, attempts: int):
    """
    Attempts to reconnect to a given socket and port by a non-negative number of attempts.
    """
    while True:
        try:
            client_socket, client_address = task_socket.accept()
            return client_socket, client_address
        except socket.timeout:
            continue

def fetch_connections():
    while is_program_running:
        get_connection()

def print_processes():
    global pid2process_class

    while is_program_running:
        print(json_serialize_traffic_data())
        time.sleep(1)


def main():
    print("SERVER STARTED")

    connection_thread = Thread(target=fetch_connections)
    printing_thread = Thread(target=send_traffic_data)

    connection_thread.start()
    printing_thread.start()

    # Starts network sniffing
    sniff(prn=get_traffic_data, store=False) 


if __name__ == "__main__":
    main()
