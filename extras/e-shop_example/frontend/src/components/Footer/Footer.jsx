import React from 'react'
import { FaFacebook, FaInstagram, FaLinkedin } from 'react-icons/fa6';
import { FaLocationArrow } from 'react-icons/fa6';
import { FaMobileAlt } from 'react-icons/fa';

const FooterLinks = [
    {
        title: "Home",
        link: "/#"
    },
    {
        title: "About",
        link: "/#"
    },
    {
        title: "Contact",
        link: "/#"
    },
    {
        title: "Blog",
        link: "/#"
    },
];

const Footer = () => {
  return (
    <div className='dark:bg-gray-950'>
        <div className='container'>
            <div className="grid md:grid-cols-3 pb-20 pt-5">
                {/* company details  */}
                <div className='py-8 px-4'>
                    <a href="#" 
                    className="text-primary font-semibold tracking-tight text-2xl sm:text-3xl">
                        Vendora
                    </a>
                    <p className='text-gray-600 dark:text-white/70 lg:pr-24 pt-3'>
                        Your business is our business. 
                        Made to improve leads and increase sales. 
                        Welcome to Vendora!
                    </p>
                    <p className="text-gray-400 mt-4 mb-3">
                        Made by Tradix - The Company
                    </p>
                    <a
                    href="https://github.com/tradixcodes"
                    target="_blank"
                    className="inline-block bg-myGrey dark:bg-primary text-white py-2 px-4 text-sm rounded-full">Visit my Page</a>
                </div>
                
                {/* Footer links  */}
                <div className='col-span-2 grid grid-cols-2 sm:grid-cols-3 md:pl-10
                '>
                    <div className='py-8 px-4'>
                        <h1 className='text-xl font-bold sm:text-left mb-3'>Important Links</h1>
                        <ul className='space-y-3'> 
                            {
                                FooterLinks.map((data , index) => (
                                    <li key={index}>
                                        <a href={data.link} 
                                        className='text-gray-600 hover:dark:text-white dark:text-gray-400
                                         hover:text-black
                                        duration-300'>{data.title}</a>
                                    </li>                                
                            ))}
                        </ul>
                    </div>
                    {/* Second Columns links  */}
                    <div className='py-8 px-4'>
                        <h1 className='text-xl font-bold sm:text-left mb-3'>Quick Links</h1>
                        <ul className='space-y-3'> 
                            {
                                FooterLinks.map((data , index) => (
                                    <li key={index}>
                                        <a href={data.link} 
                                        className='text-gray-600 hover:dark:text-white dark:text-gray-400
                                         hover:text-black
                                        duration-300'>{data.title}</a>
                                    </li>                                
                            ))}
                        </ul>
                    </div>
                    {/* Company Address */}
                    <div className='py-8 px-4 col-span-2 sm:col-auto'>
                        <h1 className='text-xl font-bold sm:text-left mb-3'>Address</h1>
                        <div>
                            <div className="flex items-center gap-3">
                                <FaLocationArrow />
                                <p>Nairobi, Kenya</p>                            
                            </div>
                            <div className="flex items-center gap-3 mt-6">
                                <FaMobileAlt />
                                <p>+254747466852</p>
                                {/* <p>Kenya</p> */}
                            </div>
                            {/* Social links */}
                            <div className='flex item-center gap-3 mt-6'>
                                <a href="#">
                                    <FaInstagram className="text-3xl hover:text-myGrey
                                     dark:hover:text-primary duration-300" />
                                </a>
                                <a href="#">
                                    <FaFacebook className="text-3xl hover:text-myGrey
                                     dark:hover:text-primary duration-300" />
                                </a>
                                <a href="#">
                                    <FaLinkedin className="text-3xl hover:text-myGrey
                                     dark:hover:text-primary duration-300" />
                                </a>
                            </div>
                        </div>
                    </div>                   
                </div>                
            </div>                    
        </div>
    </div>
  )
}

export default Footer