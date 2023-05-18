import Link from 'next/link'
import Image from 'next/image'
import Head from 'next/head'
import axios from 'axios'
import { useEffect } from 'react';
import { NavBar } from '../components/NavBar'
import { FaPlay } from "react-icons/fa"

const HELP_CONTACT = 'https://github.com/jvoliveirag/Hackathon-Inatel-2023'

export default function Home() {

  return (
    <>
      <Head>
        <title>nTracker</title>
      </Head>
        
      <div className='h-screen flex flex-col'>  

        <NavBar linkName={['Notificações', 'Ajuda', 'Contato']} linkPath={['#', HELP_CONTACT, HELP_CONTACT]} />
        
        <main className='flex items-center justify-center flex-wrap flex-col flex-1 pb-10'>
          <Link href='/report'>
            <button className='bg-green-400 rounded-full p-10 flex items-center justify-center text-9xl'>
              <FaPlay className='pl-6'/>
            </button>
          </Link>
        </main>

        <footer className='flex items-center justify-center text-xs align-baseline text-white'>
          <p>₢ 2023 nTracker | Todos os direitos reservados</p>
        </footer>

      </div>
    </>
  )
}