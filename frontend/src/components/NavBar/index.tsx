import React, { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import logoImg from '../../assets/logo.png'
import { FaChevronRight, FaChevronDown } from "react-icons/fa"

type NavBarProps = {
  linkName: string[];
  linkPath: string[];
};

const NavBar: React.FC<NavBarProps> = ({ linkName, linkPath }) => {

    let userLogged = true //criar a logica para verificar se o user esta logado
    userLogged ? linkPath[0] : linkPath[0] = '/login'
    userLogged ? linkPath[1] : linkPath[1] = '/login'

    const [isOpen, setIsOpen] = useState(false);

    const toggleDropdown = () => {
      setIsOpen(!isOpen);
    };

    return (
        <nav className='bg-green-400 backdrop-filter backdrop-blur-sm'>
            <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-3">
                <Link href="/" className="flex items-center">
                    <Image
                        src={logoImg} 
                        height={40}
                        width={40}
                        alt="PickMe Logo"
                    />
                    <span className="ml-4 self-center text-2xl font-semibold whitespace-nowrap text-black">nTracker</span>
                </Link>

                <button data-collapse-toggle="navbar-solid-bg" type="button" className="inline-flex items-center p-2 ml-3 text-sm text-black rounded-lg md:hidden hover:bg-white focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="navbar-solid-bg" aria-expanded="false">
                    <span className="sr-only">Menu</span>
                    <svg className="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clipRule="evenodd"></path></svg>
                </button>

                <div className="hidden w-full md:block md:w-auto" id="navbar-solid-bg">
                    <ul className="flex flex-col font-semibold text-xl rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-transparent dark:bg-gray-800 md:dark:bg-transparent dark:border-gray-700">
                        <li className="relative" onClick={toggleDropdown}>
                            <a href={linkPath[0]} className="flex justify-center items-center py-2 pl-3 pr-4 text-black rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-gray-800 md:p-0 md:hover:underline md:hover:underline-offset-8 duration-200 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">
                                {isOpen ? (
                                    <FaChevronDown className="transition-transform duration-300 transform rotate-270 text-base mr-2" />
                                    ) : (
                                    <FaChevronRight className="transition-transform duration-300 text-base mr-2" />
                                )}
                                {linkName[0]}
                            </a>
                            {isOpen && (
                                <ul className="absolute bg-gray-400 bg-opacity-70 mt-2 border-green-400 space-y-2 px-2 py-2 border rounded-md shadow-lg text-white">
                                {/* Conteúdo do dropdown */}
                                <p>Lorem ipsum ipsum</p>
                                </ul>
                            )}
                        </li>
                        <li>
                            <a href={linkPath[1]} className="block py-2 pl-3 pr-4 text-black rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-gray-800 md:p-0 md:hover:underline md:hover:underline-offset-8 duration-200 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">{linkName[1]}</a>
                        </li>
                        <li>
                            <a href={linkPath[2]} className="block py-2 pl-3 pr-4 text-black rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-gray-800 md:p-0 md:hover:underline md:hover:underline-offset-8 duration-200 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">{linkName[2]}</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
};

export { NavBar };
