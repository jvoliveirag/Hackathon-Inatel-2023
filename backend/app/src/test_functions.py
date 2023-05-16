"""
TEST MODULE.
TODO: REMOVE
"""


def test_deque():
    from collections import deque

    queue = deque()

    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)

    print(queue)

    for _ in range(3):
        element = queue.popleft()
        print(element)


def v1():
    from application.infra.frameworks.network_traffic_provider.sockets import SocketIO

    socket = SocketIO()
    socket.start()
    # socket.read_data()
    socket.print_data()


def v2():
    from application.infra.frameworks.network_traffic_provider.sockets import SocketIO

    socket_1 = SocketIO()
    socket_1.start()
    # socket.read_data()
    socket_1.print_data()

    socket_2 = SocketIO()
    socket_2.start()
    # socket.read_data()
    socket_2.print_data()

    socket_3 = SocketIO()
    socket_3.start()
    # socket.read_data()
    socket_3.print_data()

def test_builder():
    from application.infra.frameworks.network_traffic_provider.sockets.socket_to_network_traffic_provider_data import SocketToNetworkTrafficProviderDataBuilder
    payload = {
        "pid": "36003",
        "name": "code",
        "create_time": "13/05/2023, 15:07:19",
        "last_time_update": "13/05/2023, 15:49:53",
        "upload": "0.00B",
        "download": "35.38KB",
        "upload_speed": "0.00B/s",
        "download_speed": "54.00B/s",
        "protocol_traffic": [
            {
                "protocol": "others",
                "download": "14.68KB",
                "upload": "0.00B"
            },
            {
                "protocol": "https",
                "download": "20.64KB",
                "upload": "0.00B"
            }
        ],
        "host_traffic": [
            {
                "host": "192.168.0.106",
                "download": "14.68KB",
                "upload": "0.00B"
            },
        ]
    }

    builder = SocketToNetworkTrafficProviderDataBuilder()
    response = builder.build(payload)
    import pdb; pdb.set_trace()


def test_tkinter():
    from application.infra.ui.desktop.tkinter_ui import TkinterUI
    ui = TkinterUI()
    ui.execute()


def test_flask():
    from application.infra.ui.rest.web.flask_ui import FlaskUI

    ui = FlaskUI()
    ui.execute()


def test_use_case():
    """"""
    from domain.use_cases.network_traffic.read_network_traffic_data import ReadNetworkTrafficData
    from dependencies import NETWORK_TRAFFIC_PROVIDER_INJECTION
    import time

    use_case = ReadNetworkTrafficData(NETWORK_TRAFFIC_PROVIDER_INJECTION)
    use_case.execute()

    import pdb; pdb.set_trace()
