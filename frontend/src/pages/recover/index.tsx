import Link from 'next/link'
import Head from 'next/head'
import React, { useState, useEffect } from 'react'
import { NavBar } from '../../components/NavBar'
import Image from 'next/image'
import logo from '../../assets/logo.png'

const HELP_CONTACT = 'https://github.com/jvoliveirag/Hackathon-Inatel-2023'

export default function Recover() {
    return (
        <>
            <Head>
                <title>Recuperar senha</title>
            </Head>

            <div className='h-screen flex flex-col'>

                <NavBar linkName={['Home', 'Ajuda', 'Contato']} linkPath={['/', HELP_CONTACT, HELP_CONTACT]} />

                <main className='md:flex items-center justify-center flex-wrap flex-col flex-1 pb-10'>
                    <div className='flex flex-col flex-1'>

                        <div className="login-form flex justify-center mt-20">
                            <div className="login-form-card rounded-lg shadow-lg p-6">
                                <form method="POST">
                                    <div className="login-form-inputs flex flex-col gap-2">
                                        <div className='flex justify-center'>
                                            <Image
                                                src={logo}
                                                alt='logo'
                                                width={100}
                                                height={100}
                                            />
                                        </div>
                                        <h1 className='flex justify-center font-bold text-2xl text-left text-black py-2'>Redefinir sua senha</h1>

                                        <input type="password" name="password" placeholder="Senha" className='rounded-3xl' />
                                        <input type="password" name="password" placeholder="Confirmar senha" className='rounded-3xl' />

                                        <button type="submit" className='text-black mt-8 rounded-3xl h-10 text-xl bg-green-400 font-bold hover:bg-black hover:text-white'>Redefinir senha</button>
                                    </div>
                                </form>
                            </div>    
                        </div>
                    </div>
                </main>

                <footer className='flex items-center justify-center text-sm align-baseline text-white'>
                    <p>₢ 2023  | Todos os direitos reservados</p>
                </footer>
            </div>
        </>
    )
}