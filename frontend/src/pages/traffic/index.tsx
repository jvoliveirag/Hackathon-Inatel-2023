import Link from 'next/link'
import Image from 'next/image'
import Head from 'next/head'
import axios from 'axios'
import { useEffect } from 'react';
import { NavBar } from '../../components/NavBar'

const HELP_CONTACT = 'https://github.com/jvoliveirag/Hackathon-Inatel-2023'

export default function Home() {

  const assets = [
    {
    "create_time": "16/05/2023, 08:32:23",
    "download": "561.00B",
    "download_speed": "66.00B/s",
    "host_traffic": [
    {
    "download": "60.00B",
    "host": "52.111.225.2",
    "upload": "0.00B"
    },
    {
    "download": "315.00B",
    "host": "10.0.16.31",
    "upload": "0.00B"
    },
    {
    "download": "132.00B",
    "host": "157.240.226.60",
    "upload": "0.00B"
    }
    ],
    "last_time_update": "16/05/2023, 20:04:37",
    "name": "chrome",
    "pid": "4556",
    "protocol_traffic": [
    {
    "download": "192.00B",
    "protocol": "https",
    "upload": "0.00B"
    },
    {
    "download": "315.00B",
    "protocol": "others",
    "upload": "0.00B"
    }
    ],
    "upload": "468.00B",
    "upload_speed": "0.00B/s"
    },
    {
      "create_time": "16/05/2023, 09:32:23",
      "download": "591.00B",
      "download_speed": "61.00B/s",
      "host_traffic": [
      {
      "download": "78.00B",
      "host": "52.131.225.5",
      "upload": "0.00B"
      },
      {
      "download": "295.00B",
      "host": "10.0.16.32",
      "upload": "0.00B"
      },
      {
      "download": "332.00B",
      "host": "157.240.226.61",
      "upload": "0.00B"
      }
      ],
      "last_time_update": "16/05/2023, 20:44:37",
      "name": " code",
      "pid": "556",
      "protocol_traffic": [
      {
      "download": "196.00B",
      "protocol": "https",
      "upload": "0.00B"
      },
      {
      "download": "319.00B",
      "protocol": "others",
      "upload": "0.00B"
      }
      ],
      "upload": "359.00B",
      "upload_speed": "0.00B/s"
    },
    {
      "create_time": "16/05/2023, 09:32:23",
      "download": "129.00B",
      "download_speed": "32.00B/s",
      "host_traffic": [
      {
      "download": "78.00B",
      "host": "52.131.225.5",
      "upload": "0.00B"
      },
      {
      "download": "295.00B",
      "host": "10.0.16.32",
      "upload": "0.00B"
      },
      {
      "download": "332.00B",
      "host": "157.240.226.61",
      "upload": "0.00B"
      }
      ],
      "last_time_update": "16/05/2023, 20:44:37",
      "name": "spotify",
      "pid": "526",
      "protocol_traffic": [
      {
      "download": "196.00B",
      "protocol": "https",
      "upload": "0.00B"
      },
      {
      "download": "319.00B",
      "protocol": "others",
      "upload": "0.00B"
      }
      ],
      "upload": "452.00B",
      "upload_speed": "2.00B/s"
    },
  ]


  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('./api');
        console.log(response.data);
        console.log(response.data.network_traffic_data[0])
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    };

    fetchData();
  }, []);


  return (
    <>
      <Head>
        <title>nTracker</title>
      </Head>
        
      <div className='h-screen flex flex-col'>  

        <NavBar linkName={['Notificações', 'Home', 'Métricas', 'Ajuda', 'Contato']} linkPath={['#', '/', '/report', HELP_CONTACT, HELP_CONTACT]} />
        
        <main className='md:col-start-1 md:col-end-5 lg:col-start-2 lg:col-end-5 md:flex md:items-center md:justify-center md:flex-wrap md:flex-col md:flex-1 md:pb-10 md:gap-4'>

          <h2 className='text-white text-left m-4 justify-center items-center text-sm font-thin'>{JSON.stringify(assets, null, 2)}</h2>

        </main>

        <footer className='flex items-center justify-center text-xs align-baseline text-white'>
          <p>₢ 2023 nTracker | Todos os direitos reservados</p>
        </footer>

      </div>
    </>
  )
}