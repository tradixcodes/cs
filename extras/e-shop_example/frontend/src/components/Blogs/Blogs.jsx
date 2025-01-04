import React from 'react'
import Heading from '../Shared/Heading'

//import images
import Img1 from "../../assets/blogs/blog-1.jpg";
import Img2 from "../../assets/blogs/blog-2.jpg";
import Img3 from "../../assets/blogs/blog-3.jpg";

const BlogData = [
    {
        title:"How to choose perfect smartwatch",
        subtitle:"The issue we have to deal with the market is we can only buy what is currently available. So, we have to get out of the fit-in mentality and actually chase our dreams/dream situation",
        published:"Jan 4th, 2025 by Tradix",
        image: Img1,
    },
    {
        title:"How to choose perfect gadget",
        subtitle:"It heavily depends with the user's needs. We don't see to see how much we are being ripped off from such simple intelligence from goods that can actually choose to fail us tomorrow. Nothing in business is special, it's just the one that exists and serves the purpose you need",
        published:"Jan 4th, 2025 by Kanyagia",
        image: Img2,
    },
    {
        title:"How to choose perfect VR Headset",
        subtitle:"I don't know much about VR Headsets, but the fact you are buying this means you have alot of skill/money or you live in a rich country",
        published:"Jan 4th, 2025 by John",
        image: Img3,
    },
]

const Blogs = () => {
  return (
    <div className='my-12'>
        <div className='container'>
            {/* Header section */}
            <Heading title="Recent News"
            subtitle={"Explore Our Blogs"}/>

            {/* Blog section */}
            <div className='grid grid-cols-1 sm:grid-cols-2 
            md:grid-cols-3 gap-6 gap-y-8 sm:gap-4 md:gap-7'>
                {/* {Blog Card } */}
                {BlogData.map((data) => (
                    <div key= {data.title} className='bg-white dark:bg-gray-900'>
                        {/* {image section } */}
                        <div className="overflow-hidden rounded-2xl mb-2">
                            <img src={data.image} alt=""
                            className='w-full h-[220px] object-cover rounded-2xl
                            hover:scale-105 duration-500'/>
                        </div>
                        {/* {content section } */}
                        <div className='space-y-2'>
                            <p className='text-xs text-gray-500'>{data.published}</p>
                            <p className='font-bold line-clamp-1'>{data.title}</p>
                            <p className='line-clamp-2 text-sm text-gray-600
                            dark:text-gray-400'>{data.subtitle}</p>
                        </div>
                    </div>
                                           
                ))}
            </div>
        </div>

    </div>
  )
}

export default Blogs