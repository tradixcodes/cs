import React from 'react'

const Hero = () => {

    const settings = {
        dots: false,
        arrows: false,
        infinite: true,
        speed: 800,
        slidesToScroll: 1,
        //autoplay: true,
        autoplaySpeed: 4000,
        cssEase: "ease-in-out",
        pauseOnHover: false,
        pauseOnFocus: true,
      };
  return (
    <div>
        {/* Hero Section */}
        <Slider></Slider>
    </div>
  )
}

export default Hero