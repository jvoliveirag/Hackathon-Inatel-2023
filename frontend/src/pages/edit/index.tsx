import Link from 'next/link'
import Head from 'next/head'
import { NavBar } from '../../components/NavBar'
import { FaPlay } from "react-icons/fa"
import Image from 'next/image'
import logo from '../../assets/logo.png'

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
          <div className='flex flex-col flex-1'>


              <div className="login-form flex justify-center mt-11">
                  <div className="login-form-card rounded-lg shadow-lg p-6">
                      <form method="POST">
                          <div className="login-form-inputs flex flex-col gap-1">
                              <div className='flex justify-center'>
                                  <Image
                                      src={logo}
                                      alt='logo'
                                      width={100}
                                      height={100}
                                  />
                              </div>
                              <h1 className='flex justify-center font-bold text-2xl text-left text-black py-2'>Configurar um alerta</h1>

                              <input type="text" name="alert" placeholder="Nome do alerta" className='rounded-3xl'/>
                              <input type="text" name="email" placeholder="Programa" className='rounded-3xl'/>
                              <input type="text" name="password" placeholder="Limite" className='rounded-3xl'/>
                              <input type="text" name="password" placeholder="Confirmar email" className='rounded-3xl'/>
                              <button type="submit" className='text-black mt-4 rounded-3xl h-10 text-xl bg-green-400 font-bold hover:bg-black hover:text-white'>Criar alerta</button>
                          </div>
                      </form>
                  </div>
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