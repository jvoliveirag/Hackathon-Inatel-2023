import Link from 'next/link'
import Head from 'next/head'
import { NavBar } from '../../components/NavBar'
import { FaPlay } from "react-icons/fa"

const HELP_CONTACT = 'https://github.com/jvoliveirag/Hackathon-Inatel-2023'

export default function Edit() {

  var userLogged = true //logica para verificar estado de userLogged
  var navbarName = ''
  var navbarLink = ''
  userLogged ? (navbarName = 'Notificações', navbarLink = '#') : (navbarName = 'Login', navbarLink = '/login')

  return (
    <>
      <Head>
        <title>nTracker</title>
      </Head>
        
      <div className='h-screen flex flex-col'>  

        <NavBar linkName={[navbarName, 'Ajuda', 'Contato']} linkPath={[navbarLink, HELP_CONTACT, HELP_CONTACT]} />
        
        <main className='flex items-center justify-center flex-wrap flex-col flex-1 pb-10'>

        </main>

        <footer className='flex items-center justify-center text-xs align-baseline text-white'>
          <p>₢ 2023 nTracker | Todos os direitos reservados</p>
        </footer>

      </div>
    </>
  )
}