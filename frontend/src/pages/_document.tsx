import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {

    return (
        <Html>
            <Head>
                <link rel="preconnect" href="https://fonts.googleapis.com" />
                <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;1,700&display=swap" rel="stylesheet" />
                <link rel="icon" href="/favicon.png" />
            </Head>
            <body className='h-screen bg-cover bg-fixed bg-gradient-to-b from-black via-gray-900 to-black'>
                <Main />
                <NextScript />
            </body>
        </Html>
    )
}