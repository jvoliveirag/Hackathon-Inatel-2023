import Link from 'next/link'
import Image from 'next/image'
import Head from 'next/head'
import axios from 'axios'
import { useEffect } from 'react';
import { NavBar } from '../../components/NavBar'
import { FaChevronDown, FaCog, FaSearch } from "react-icons/fa"
import Highcharts, { color } from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

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

  interface Asset {
    download: string;
    download_speed: string;
    upload: string,
    upload_speed: string;
    pid: string;
    name: string;
    last_time_update: string
  }

  function extractAssetData(assets: Asset[]): { download: number, download_speed: string, pid: string, name: string, upload: number, upload_speed: string, last_time_update: string }[] {
    return assets.map(asset => ({
      download: parseFloat(asset.download),
      download_speed: asset.download_speed,
      upload: parseFloat(asset.upload),
      upload_speed: asset.upload_speed,
      last_time_update: asset.last_time_update,
      pid: asset.pid,
      name: asset.name
    }));
  }
  
  const extractedAssetData = extractAssetData(assets);

  // Função para calcular o tamanho da fonte com base no tamanho da janela
  function calculateFontSize() {
    if (typeof window !== 'undefined') {
      const windowWidth = window.innerWidth;
      // Defina o tamanho da fonte de acordo com o tamanho da janela
      if (windowWidth < 768) {
        return '11px'; // Tamanho da fonte para telas menores
      } else {
        return '16px'; // Tamanho da fonte para telas maiores
      }
    } else {
      console.log('Código sendo executado fora do ambiente do navegador');
    }

  }
  // Preparar os dados para Highcharts
  const chartData = {
    chart: {
      type: 'column',
      height: (9 / 16 * 100) + '%',
      borderRadius: 10,
    },
    title: {
      text: 'Download e Upload por Programa',
      style: {
        fontSize: calculateFontSize()
      }
    },
    xAxis: {
      categories: extractedAssetData.map(item => item.name),
      labels: {
        style: {
          fontSize: calculateFontSize() // Chamar a função para definir o tamanho da fonte
        }
      }
    },
    yAxis: {
      title: {
        text: 'Download | Upload',
        style: {
          fontSize: calculateFontSize() // Chamar a função para definir o tamanho da fonte
        }
      }
    },
    plotOptions: {
      column: {
        dataLabels: {
          enabled: true,
          style: {
            fontSize: calculateFontSize() // Definir o tamanho da fonte das séries
          }
        }
      }
    },
    series: [
      {
        name: 'Download',
        data: extractedAssetData.map(item => item.download),
        color: '#494F56',
      },
      {
        name: 'Upload',
        data: extractedAssetData.map(item => item.upload),
        color: '#0f0',
      }
    ],
    
    tooltip: {
      formatter(this: Highcharts.TooltipFormatterContextObject): string {
        const point = this.point as Highcharts.Point;
        const seriesName = point.series.name;
        const value = point.y;
  
        // Obter os valores extras
        const { pid, download_speed, upload_speed, last_time_update, name } = extractedAssetData[point.index];
  
        // Construir o conteúdo da legenda
        let tooltipContent = `<b>${name.toUpperCase()}</b><br>`;
        tooltipContent += `<b>${seriesName}: </b>`
        tooltipContent += `${value} Bytes<br>`;
        tooltipContent += `<b>PID: </b>${pid}<br>`;
        seriesName === 'Download' ? tooltipContent += `<b>Velocidade de Download: </b>${download_speed}<br>` : tooltipContent += `<b>Velocidade de Upload: </b>${upload_speed}<br>`;
        tooltipContent += `<b>Última Atualização: </b>${last_time_update}<br>`;
  
        // Retornar o conteúdo da legenda formatado
        return tooltipContent;
      }
    },
  };


  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('../api');
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

        <NavBar linkName={['Notificações', 'Home', 'Tráfego', 'Ajuda', 'Contato']} linkPath={['#', '/', '/traffic', HELP_CONTACT, HELP_CONTACT]} />
        
        <main className='md:col-start-1 md:col-end-5 lg:col-start-2 lg:col-end-5 md:flex md:items-center md:justify-center md:flex-wrap md:flex-col md:flex-1 md:pb-10 md:gap-4'>

            <div className='bg-white flex items-center justify-center rounded-full gap-2 p-1 opacity-80'>
              <input type="text" placeholder='procure aqui' className='rounded-full text-sm sm:pr-72 sm:mr-12 md:pr-56 md:mr-28 mr-16'/><FaSearch/> <FaChevronDown/> <FaCog className='mr-2'/>
            </div>

            <div className='md:flex bg-white justify-center items-center rounded-xl opacity-80'>
              <div className='mt-2'>
                <HighchartsReact highcharts={Highcharts} options={chartData} />
              </div>
            </div>

        </main>

        <footer className='flex items-center justify-center text-xs align-baseline text-white sm:hidden'>
          <p>₢ 2023 nTracker | Todos os direitos reservados</p>
        </footer>

      </div>
    </>
  )
}