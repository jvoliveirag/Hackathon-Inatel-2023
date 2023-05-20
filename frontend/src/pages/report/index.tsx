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

    const trafficSpeedAverages = {
        "traffic_speed_averages": [
        {
        "average_download_speed": 83.35,
        "average_upload_speed": 0,
        "create_time": "19/05/2023, 13:20:47",
        "downloads": [
            66, 66, 66, 66, 66, 74, 66, 66, 66, 66, 156, 123, 74, 101, 66, 75, 66, 160, 112, 66
        ],
        "last_time_update": "19/05/2023, 18:17:49",
        "name": "chrome",
        "pid": "3242",
        "uploads": [
            37, 127, 172, 59, 87, 103, 14, 182, 96, 101, 154, 11, 45, 193, 72, 83, 32, 26, 185, 68
        ]
        },
        {
        "average_download_speed": 101,
        "average_upload_speed": 0,
        "create_time": "19/05/2023, 16:17:36",
        "downloads": [
            66, 66, 66, 66, 66,66,66, 66, 54, 54, 54, 54, 54, 898, 54, 54, 54, 54, 54, 54
        ],
        "last_time_update": "19/05/2023, 18:17:44",
        "name": "code",
        "pid": "9925",
        "uploads": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
        ]
        },
        {
        "average_download_speed": 81.85,
        "average_upload_speed": 0,
        "create_time": "19/05/2023, 16:17:36",
        "downloads": [
            139, 97, 161, 78, 123, 56, 71, 48, 17, 8, 53, 141, 64, 183, 108, 192, 91, 188, 4, 120
        ],
        "last_time_update": "19/05/2023, 18:17:47",
        "name": "code",
        "pid": "9926",
        "uploads": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
        ]
        },
        {
        "average_download_speed": 141,
        "average_upload_speed": 78,
        "create_time": "19/05/2023, 13:20:32",
        "downloads": [
        233,
        233,
        233,
        233,
        145,
        145,
        145,
        145,
        145,
        145,
        145,
        145,
        91,
        91,
        91,
        91,
        91,
        91,
        91,
        91
        ],
        "last_time_update": "19/05/2023, 18:17:43",
        "name": "teams",
        "pid": "544",
        "uploads": [
            125, 55, 38, 140, 186, 97, 177, 26, 90, 41, 165, 77, 4, 116, 59, 134, 83, 13, 124, 154
        ]
        },
        {
        "average_download_speed": 66,
        "average_upload_speed": 0,
        "create_time": "19/05/2023, 13:20:33",
        "downloads": [
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66
        ],
        "last_time_update": "19/05/2023, 18:15:59",
        "name": "NetworkManager",
        "pid": "606",
        "uploads": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
        ]
        },
        {
        "average_download_speed": 54,
        "average_upload_speed": 97,
        "create_time": "19/05/2023, 16:17:38",
        "downloads": [
        57,
        54,
        54,
        54,
        54,
        54,
        54,
        54,
        54,
        54,
        54,
        54,
        54,
        54,
        54,
        54,
        54,
        54,
        54,
        54,
        54
        ],
        "last_time_update": "19/05/2023, 18:15:46",
        "name": "discord",
        "pid": "10010",
        "uploads": [
            71, 164, 79, 22, 160, 11, 150, 173, 37, 195, 143, 115, 93, 42, 30, 98, 187, 133, 119, 141
        ]
        },
        {
        "average_download_speed": 66,
        "average_upload_speed": 0,
        "create_time": "19/05/2023, 13:20:42",
        "downloads": [
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66,
        66
        ],
        "last_time_update": "19/05/2023, 17:20:56",
        "name": "goa-daemon",
        "pid": "1644",
        "uploads": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
        ]
        },
        ]
    }

    interface TrafficSpeedAverages {
        name: string,
        average_download_speed: number,
        average_upload_speed: number,
        pid: string,
        create_time: string,
        last_time_update: string,
        downloads: number[],
        uploads: number[]
    }

    function extractTrafficData(trafficSpeedAverages: {"traffic_speed_averages": TrafficSpeedAverages[]}): { 
        name: string, pid: string, download_speed: number, upload_speed: number, create_time: string, last_time_update: string, downloads: number[],uploads: number[] }[] {
        
        const data = trafficSpeedAverages["traffic_speed_averages"];

        return data.map((item: TrafficSpeedAverages) => ({
          name: item.name,
          download_speed: item.average_download_speed,
          upload_speed: item.average_upload_speed,
          last_time_update: item.last_time_update,
          create_time: item.create_time,
          pid: item.pid,
          downloads: item.downloads,
          uploads: item.uploads
        }));
    }

    let extractedTrafficData = extractTrafficData(trafficSpeedAverages)

    useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await axios.get('../api');
            console.log(response.data);
            console.log(response.data.traffic_speed_averages[0])
            extractedTrafficData = response.data.traffic_speed_averages
            console.log(extractTrafficData)
          } catch (error) {
            console.error('Failed to fetch data:', error);
          }
        };
    
        fetchData();
    }, []);
    
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


    const [isOpen, setIsOpen] = useState(false);
    const [selectedValue, setSelectedValue] = useState('');
  
    const toggleDropdown = () => {
        setIsOpen(!isOpen);
    };
  
    const handleOptionSelect = (value: string) => {
        setSelectedValue(value);
        setIsOpen(false);
        console.log(value)
    };

    function findObjectPosition(searchString: string): number {
        const averages = trafficSpeedAverages["traffic_speed_averages"];
      
        for (let i = 0; i < averages.length; i++) {
          const obj = averages[i];
          if (obj.pid === searchString) {
            return i;
          }
        }
      
        return 0;
    }
      
    const searchString = selectedValue; //code [1]
    let position = findObjectPosition(searchString);
      
    if (position !== null) {
        console.log(`A posição do objeto com a string "${searchString}" é: ${position}`);
    } else {
        console.log(`O objeto com a string "${searchString}" não foi encontrado.`);
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
        text: `Download x Upload: ${extractedTrafficData[position].name.toUpperCase()}`,
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
        max: 20, // Define o valor máximo do eixo X
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
                data: extractedTrafficData[position].downloads,
                color: '#0f0'
            },
            {
                name: 'Uploads',
                data: extractedTrafficData[position].uploads,
                color: '#494F56',
            },
        ],
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
        categories: extractedTrafficData.map(item => item.name),
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
                data: extractedTrafficData.map(item => item.download_speed),
                color: '#0f0',
            },
            {
                name: 'Vel. Upload',
                data: extractedTrafficData.map(item => item.upload_speed),
                color: '#494F56',
            }
        ],
        
        tooltip: {
        formatter(this: Highcharts.TooltipFormatterContextObject): string {
            const point = this.point as Highcharts.Point;
            const seriesName = point.series.name;
            const value = point.y;
    
            // Obter os valores extras
            const { pid, create_time, last_time_update, name } = extractedTrafficData[point.index];
    
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
                                    <Link href='/report/'>
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
                                    {extractedTrafficData.map((option) => (
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