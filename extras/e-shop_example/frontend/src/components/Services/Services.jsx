import React from 'react'
import {
    FaCarSide,
    FaHeadphonesAlt,
    FaWallet,
    FaRegCheckCircle,
} from "react-icons/fa";

const ServiceData = [
    {
        id:1,
        icon:<FaCarSide className='text-4xl md:text-5xl text-myGrey dark:text-yellowGold'/>,
        title:"Free Shipping",
        description:"Free Shipping Worldwide",
    },
    {
        id:2,
        icon:<FaHeadphonesAlt className='text-4xl md:text-5xl text-myGrey  dark:text-yellowGold'/>,
        title:"24/7 Support",
        description:"Quality Support",
    },
    {
        id:3,
        icon:<FaWallet className='text-4xl md:text-5xl text-myGrey  dark:text-yellowGold'/>,
        title:"Safe Transactions",
        description:"30 Days Money Back Guarantee",
    },
    {
        id:4,
        icon:<FaRegCheckCircle className='text-4xl md:text-5xl text-myGrey  dark:text-yellowGold'/>,
        title:"Excellent Service",
        description:"Happy Customers",
    },
]

const Services = () => {
  return (
    <div>
        <div className='container mt-14 md:my-20'>
            <div className='grid grid-cols-2 lg:grid-cols-4 gap-4
            gap-y-8'>
                {ServiceData.map((data) => (
                    <div className='flex flex-col items-start sm:flex-row
                    gap-4'> 
                        {data.icon}
                        <div > 
                        <h1 className='lg:text-xl font-bold'>{data.title}</h1>
                        <h1 className='text-gray-400 text-sm'>{data.description}</h1>                             

                        </div>                            
                    </div>                        
                ))}
            </div>
        </div>
    </div>
  )
}

export default Services