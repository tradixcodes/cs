import React from "react";
import Navbar from "./components/Navbar/Navbar";
import Hero from "./components/Hero/Hero";
import Category from "./components/Category/Category";
import Category2 from "./components/Category/Category2";
import Services from "./components/Services/Services"; 
import Banner from "./components/Banner/Banner";

import headphones from "../src/assets/hero/headphone.png"

const BannerData = {
  discount: "30% OFF",
  title: "Fine Smile",
  date: "10th Jan to 28th Jan",
  image: headphones,
  title2: "Air Solo Bass",
  title3: "Christmas Sale",
  title4: "Up to 50% OFF",
  bgColor: '#A41045',
};

const App = () => {
  return (
    <div className="bg-white dark:bg-gray-900 dark:text-white 
    duration-200 overflow-hidden">
      <Navbar/>
      <Hero/>
      <Category/>
      <Category2/>
      <Services/>
      <Banner data={BannerData}/>
    </div>
  )
}

export default App
