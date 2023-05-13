import Link from 'next/link'
import Image from 'next/image'
import Head from 'next/head'

import net from 'net';

const HOST = '127.0.0.1';
const PORT_NETWORK_TRAFFIC = 50000;
const PORT_PROTOCOL_TRAFFIC = 50001;
const PORT_HOSTNAME_TRAFFIC = 50002;


export default function Home() {

  const network_client = new net.Socket();
  const protocol_client = new net.Socket();
  const hostname_client = new net.Socket();

  const handleClick = () => {
    network_client.write('Hello, server! Love, Client.');
    protocol_client.write('Hello, server! Love, Client.');
    hostname_client.write('Hello, server! Love, Client.');
  }

  network_client.connect(PORT_NETWORK_TRAFFIC, HOST, () => {
    console.log('Conectado ao provedor de tráfego por aplicativo.');
  });

  protocol_client.connect(PORT_PROTOCOL_TRAFFIC, HOST, () => {
    console.log('Conectado ao provedor de tráfego por protocolo de rede.');
  });

  hostname_client.connect(PORT_HOSTNAME_TRAFFIC, HOST, () => {
    console.log('Conectado ao provedor de tráfego por hosts.');
  });

  network_client.on('data', (data: Buffer) => {
    console.log('Dado recebido do network_client:', data.toString());
  });

  protocol_client.on('data', (data: Buffer) => {
    console.log('Dado recebido do protocol_client:', data.toString());
  });

  hostname_client.on('data', (data: Buffer) => {
    console.log('Dado recebido do hostname_client:', data.toString());
  });

  network_client.on('error', (error: Error) => {
    console.error('Erro recebido no network_client:', error);
  });

  protocol_client.on('error', (error: Error) => {
    console.error('Erro recebido no protocol_client:', error);
  });

  hostname_client.on('error', (error: Error) => {
    console.error('Erro recebido no hostname_client:', error);
  });

  network_client.on('close', () => {
    console.log('Conexão encerrada com o network_client.');
  });

  protocol_client.on('close', () => {
    console.log('Conexão encerrada com o protocol_client.');
  });

  hostname_client.on('close', () => {
    console.log('Conexão encerrada com o hostname_client.');
  });


  return (
    <>
      <Head>
        <title>nTracker</title>
      </Head>
        
      <div className='h-screen flex flex-col'>  

        <main className='flex items-center justify-center flex-wrap flex-col flex-1 pb-10'>

          <button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded' onClick={handleClick}>
            Clique aqui
          </button>

        </main>

        <footer className='flex items-center justify-center text-sm align-baseline text-white'>
          <p>₢ 2023 nTracker | Todos os direitos reservados</p>
        </footer>

      </div>
    </>
  )
}
