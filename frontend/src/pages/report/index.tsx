import Link from 'next/link'
import Image from 'next/image'
import Head from 'next/head'
import axios from 'axios'
import { useEffect, useState } from 'react';
import { NavBar } from '../../components/NavBar'
import { FaChevronDown, FaCog, FaSearch, FaRedo } from "react-icons/fa"
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

const HELP_CONTACT = 'https://github.com/jvoliveirag/Hackathon-Inatel-2023'

export default function Report() {

    const networkTrafficData = {
        "network-traffic-speed-package": [
           {
           "name": "chrome",
           "average_download_speed": 123,
           "average_upload_speed": 12,
           "pid": '1',
           "create_time": "18/05/2023, 10:07:19",
           "last_time_update": "18/05/2023, 12:04:37"
           },
           {
           "name": "code",
           "average_download_speed": 13,
           "average_upload_speed": 2,
           "pid": '2',
           "create_time": "18/05/2023, 11:07:19",
           "last_time_update": "18/05/2023, 13:04:37"
           },
           {
            "name": "dicord",
            "average_download_speed": 123,
            "average_upload_speed": 12,
            "pid": '3',
            "create_time": "18/05/2023, 10:07:19",
            "last_time_update": "18/05/2023, 12:04:37"
            },
            {
            "name": "spotify",
            "average_download_speed": 13,
            "average_upload_speed": 2,
            "pid": '4',
            "create_time": "18/05/2023, 11:07:19",
            "last_time_update": "18/05/2023, 13:04:37"
            },
            {
            "name": "teams",
            "average_download_speed": 123,
            "average_upload_speed": 12,
            "pid": '5',
            "create_time": "18/05/2023, 10:07:19",
            "last_time_update": "18/05/2023, 12:04:37"
           },
           {
           "name": "valorant",
           "average_download_speed": 13,
           "average_upload_speed": 2,
           "pid": '6',
           "create_time": "18/05/2023, 11:07:19",
           "last_time_update": "18/05/2023, 13:04:37"
           },
           {
            "name": "code",
            "average_download_speed": 123,
            "average_upload_speed": 12,
            "pid": '7',
            "create_time": "18/05/2023, 10:07:19",
            "last_time_update": "18/05/2023, 12:04:37"
            },
        ]
    }

    interface NetworkTrafficData {
        name: string,
        average_download_speed: number,
        average_upload_speed: number,
        pid: string,
        create_time: string,
        last_time_update: string
    }

    function extractNetworkTrafficData(networkTrafficData: {"network-traffic-speed-package": NetworkTrafficData[]}): { name: string, pid: string, download_speed: number, upload_speed: number, create_time: string, last_time_update: string }[] {
        
        const data = networkTrafficData["network-traffic-speed-package"];

        return data.map((item: NetworkTrafficData) => ({
          name: item.name,
          download_speed: item.average_download_speed,
          upload_speed: item.average_upload_speed,
          last_time_update: item.last_time_update,
          create_time: item.create_time,
          pid: item.pid
        }));
    }

    const extractedNetworkTrafficData = extractNetworkTrafficData(networkTrafficData);

  // Função para calcular o tamanho da fonte com base no tamanho da janela
  function calculateFontSize() {
        if (typeof window !== 'undefined') {
            const windowWidth = window.innerWidth;
            // Defina o tamanho da fonte de acordo com o tamanho da janela
            if (windowWidth < 1024 && 512 < windowWidth) {
                    return '14px'; // Tamanho da fonte para telas menores
            } 
                else if (windowWidth < 512){
                    return '6px'; // Tamanho da fonte para telas menores
            }
                else {
                    return '14px'; // Tamanho da fonte para telas maiores
            }
        } else {
            console.log('Código sendo executado fora do ambiente do navegador');
        }
    }

  // Preparar os dados para Highcharts
  const splineChartData = {
    chart: {
      type: 'spline',
      scrollablePlotArea: {
        minWidth: 700,
        scrollPositionX: 1
      },
      height: (9 / 16 * 100) + '%',
      borderRadius: 10,
    },
    title: {
      text: 'Download x Upload',
      style: {
        fontSize: calculateFontSize()
      }
    },
    subtitle: {
      text: '(Com base nos últimos 20s de varredura)',
      style: {
        fontSize: calculateFontSize()
      }
    },
    credits: {
      enabled: false,
    },
    xAxis: {
      min: 0, // Define o valor mínimo do eixo X
      max: extractedNetworkTrafficData.length, // Define o valor máximo do eixo X
      title: {
        text: 'tempo [s]',
        style: {
          fontSize: calculateFontSize()
        }
      }
    },
    yAxis: {
      title: {
        text: 'Taxa [kB]',
        style: {
          fontSize: calculateFontSize()
        }
      },
      labels: {
        style: {
          fontSize: calculateFontSize()
        }
      },
      type: 'linear' // Define o tipo de escala do eixo Y como linear para receber valores de ponto flutuante
    },
    plotOptions: {
      spline: { // Altera "column" para "spline" para aplicar as modificações nas séries de linha
        dataLabels: {
          enabled: false,
          style: {
            fontSize: calculateFontSize()
          }
        }
      }
    },
    series: [
        {
            name: 'Downloads',
            data: extractedNetworkTrafficData.map(item => item.download_speed),
            color: '#0f0'
        },
        {
            name: 'Uploads',
            data: extractedNetworkTrafficData.map(item => item.upload_speed),
            color: '#494F56',
        },
    ],
    tooltip: {
        formatter(this: Highcharts.TooltipFormatterContextObject): string {
            const point = this.point as Highcharts.Point;
            const seriesName = point.series.name;
            const value = point.y;
      

            // Verificar se o índice é válido
            if (point.index >= 0 && point.index < extractedNetworkTrafficData.length) {
                // Obter os valores extras
                const { pid, create_time, last_time_update, name } = extractedNetworkTrafficData[point.index];
        
                // Construir o conteúdo da legenda
                let tooltipContent = `<b>Programa:</b> ${name} | <b>PID: </b>${pid}<br>`;
                tooltipContent += `<b>${seriesName}: </b> ` + `${value} Bps<br>`;
                tooltipContent += `<b>Criado em: </b>${create_time}<br>`;
                tooltipContent += `<b>Última Atualização: </b>${last_time_update}<br>`;
        
                // Retornar o conteúdo da legenda formatado
                return tooltipContent;
            }
        
            // Se o índice for inválido, retornar uma string vazia
            return '';
        }
    },
  };
  

  const columnChartData = {
    chart: {
        type: 'column',
        scrollablePlotArea: {
                minWidth: 700,
                scrollPositionX: 1
            },
        height: (9 / 16 * 100) + '%',
        borderRadius: 10,
    },
    title: {
        text: 'Velocidade média de download e upload por Programa',
        style: {
            fontSize: calculateFontSize()
        }
    },
    subtitle:{
        text: '(Cálculo com base nos últimos 20s de varredura)',
        style: {
            fontSize: calculateFontSize()
        }
    },
    credits:{
        enabled: false,
    },
    xAxis: {
      categories: extractedNetworkTrafficData.map(item => item.name),
      labels: {
        style: {
            fontSize: calculateFontSize() // Chamar a função para definir o tamanho da fonte
        }
      },
    },
    yAxis: {
      title: {
        text: 'Velocidade [B/s]',
        style: {
            fontSize: calculateFontSize() // Chamar a função para definir o tamanho da fonte
        }
      }
    },
    plotOptions: {
        column: {
            dataLabels: {
                enabled: false,
                style: {
                    fontSize: calculateFontSize() // Definir o tamanho da fonte das séries
                }
            }
        }
    },
    series: [
        {
            name: 'Vel. Download',
            data: extractedNetworkTrafficData.map(item => item.download_speed),
            color: '#494F56',
        },
        {
            name: 'Vel. Upload',
            data: extractedNetworkTrafficData.map(item => item.upload_speed),
            color: '#0f0',
        }
    ],
    
    tooltip: {
      formatter(this: Highcharts.TooltipFormatterContextObject): string {
        const point = this.point as Highcharts.Point;
        const seriesName = point.series.name;
        const value = point.y;
  
        // Obter os valores extras
        const { pid, create_time, last_time_update, name } = extractedNetworkTrafficData[point.index];
  
        // Construir o conteúdo da legenda
        let tooltipContent = `<b>Programa:</b> ${name} | <b>PID: </b>${pid}<br>`;
        tooltipContent += `<b>${seriesName}: </b> `+`${value} Bps<br>`;
        tooltipContent += `<b>Criado em: </b>${create_time}<br>`;
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



    const [isOpen, setIsOpen] = useState(false);
    const [selectedValue, setSelectedValue] = useState('');
  
    const toggleDropdown = () => {
      setIsOpen(!isOpen);
    };
  
    const handleOptionSelect = (value: string) => {
      setSelectedValue(value);
      setIsOpen(false);
      console.log(value) //pega o pid para selecionar os valores a serem exibidos no grafico
    };


  return (
    <>
        <Head>
            <title>nTracker</title>
        </Head>
        
        <div className='h-screen flex flex-col'>  

            <NavBar linkName={['Notificações', 'Tráfego', 'Ajuda', 'Contato']} linkPath={['#', '/traffic', HELP_CONTACT, HELP_CONTACT]} />
            
            <main className='md:col-start-1 md:col-end-5 lg:col-start-2 lg:col-end-5 md:flex md:items-center md:justify-center md:flex-wrap md:flex-col md:flex-1 md:pb-10 md:gap-4'>

                <div className='md:flex justify-center items-center mx-16'>
    
                    <div className='grid lg:grid-cols-2 grid-cols-1 gap-8'>
                        <div className='mt-8 lg:mt-0'>
                            <div className='flex items-center justify-between bg-white rounded-full p-1 gap-4 md:text-2xl'>
                                <input type="text" placeholder='procure aqui um alerta' className='rounded-full text-sm lg:pr-28 sm:pr-28 pr-0'/>
                                <div className='flex items-center justify-center gap-4 mr-2'>
                                    <Link href='/report'>
                                        <button className='flex items-center justify-center' type="submit">
                                            <FaRedo/>
                                        </button>
                                    </Link>
                                    <Link href='/edit'>
                                        <button className='flex items-center justify-center' type="submit">
                                            <FaCog/>
                                        </button>
                                    </Link> 
                                </div>
                            </div>
                            <div className='bg-white rounded-xl p-2 mt-8'>
                                <HighchartsReact highcharts={Highcharts} options={columnChartData}/>
                            </div>
                        </div>

                        <div className='bg-white rounded-xl p-2'>
                            <div className="relative inline-block">
                                <div className="flex items-center text-2xl cursor-pointer" onClick={toggleDropdown}>
                                    <FaChevronDown />
                                </div>
                                {isOpen && (
                                    <ul className="absolute z-10 left-0 w-48 py-2 mt-2 bg-white border border-gray-300 rounded-xl shadow">
                                    {extractedNetworkTrafficData.map((option) => (
                                        <li
                                        key={option.pid}
                                        className="px-4 py-2 cursor-pointer hover:bg-gray-100"
                                        onClick={() => handleOptionSelect(option.pid)}
                                        >
                                        {option.name}
                                        </li>
                                    ))}
                                    </ul>
                                )}
                                {selectedValue && (
                                    <div className="mt-2 text-black hidden">
                                    Valor selecionado: {selectedValue}
                                    </div>
                                )}
                            </div>
                            <div>
                                <HighchartsReact highcharts={Highcharts} options={splineChartData}/>
                            </div>
                        </div>
                    </div>
                    <div>

                    </div>
                    
                </div>

            </main>

            <footer className='flex items-center justify-center text-xs align-baseline text-white'>
                <p>₢ 2023 nTracker | Todos os direitos reservados</p>
            </footer>

        </div>
    </>
  )
}