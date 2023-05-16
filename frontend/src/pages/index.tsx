import Link from 'next/link'
import Image from 'next/image'
import Head from 'next/head'
import { NavBar } from '../components/NavBar'

export default function Home() {

  return (
    <>
      <Head>
        <title>nTracker</title>
      </Head>
        
      <div className='h-screen flex flex-col'>  

        <NavBar linkName={['Notificações', 'Ajuda', 'Contato']} linkPath={['#', '#', '#']} />

        <main className='flex items-center justify-center flex-wrap flex-col flex-1 pb-10'>
          
        </main>

        <footer className='flex items-center justify-center text-xs align-baseline text-white'>
          <p>₢ 2023 nTracker | Todos os direitos reservados</p>
        </footer>

      </div>
    </>
  )
}