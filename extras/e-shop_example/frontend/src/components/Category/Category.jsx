import React from 'react'
import Image1 from '../../assets/category/earphone.png'
import Image2 from '../../assets/category/watch.png'
import Image3 from '../../assets/category/macbook.png'
import Button from '../Shared/Button.jsx'

const Category = () => {
  return (
    <div className='py-8'>
        <div className='container'>
            <div className='grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8'>
                {/* first column */}
                <div className='py-10 pl-5 bg-gradient-to-br from-black/90
                 to-black/70 text-white rounded-3xl relative h-[320px]
                 flex items-end'>
                    <div>
                        <div className='mb-4'>
                            <p className='mb-[2px] text-gray-400'>Enjoy</p>
                            <p className='text-2xl font-semibold mb-[2px]'>With</p>
                            <p className='text-4xl xl:text-5xl font-bold opacity-20 mb-2'>Earphones</p>
                            <Button
                            text="Browse"
                            bgColor={"bg-myGrey dark:bg-primary"}
                            textColor={"text-white"}
                            />
                        </div>
                    </div>
                    <img src={Image1} alt=""
                    className='w-[320px] absolute bottom-0'/>
                </div>
                {/* second column */}
                <div className='py-10 pl-5 bg-gradient-to-br from-brandYellow
                 to-brandYellow/90 text-white rounded-3xl relative h-[320px]
                 flex items-end'>
                    <div>
                        <div className='mb-4'>
                            <p className='mb-[2px] text-white'>Enjoy</p>
                            <p className='text-2xl font-semibold mb-[2px]'>With</p>
                            <p className='text-4xl xl:text-5xl font-bold opacity-40 mb-2'>Gadgets</p>
                            <Button
                            text="Browse"
                            bgColor={"bg-white"}
                            textColor={"text-brandYellow"}
                            />
                        </div>
                    </div>
                    <img src={Image2} alt=""
                    className='w-[320px] absolute -right-4 lg:top-[40px]'/>
                </div>
                {/* third column (long) */}
                <div className='col-span-2 py-10 pl-5 bg-gradient-to-br from-brandRed
                 to-brandRed/90 text-white rounded-3xl relative h-[320px]
                 flex items-end'>
                    <div>
                        <div className='mb-4'>
                            <p className='mb-[2px] text-white'>Enjoy</p>
                            <p className='text-2xl font-semibold mb-[2px]'>With</p>
                            <p className='text-4xl xl:text-5xl font-bold opacity-50 mb-2'>Laptops</p>
                            <Button
                            text="Browse"
                            bgColor={"bg-white"}
                            textColor={"text-brandRed"}
                            />
                        </div>
                    </div>
                    <img src={Image3} alt=""
                    className='w-[350px] absolute top-1/2 -translate-y-1/2 -right-0'/>
                </div>
            </div>
        </div>
    </div>
  )
}

export default Category