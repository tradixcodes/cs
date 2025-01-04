import React from "react";
import Navbar from "./components/Navbar/Navbar";
import Hero from "./components/Hero/Hero";
import Category from "./components/Category/Category";
import Category2 from "./components/Category/Category2";
import Services from "./components/Services/Services"; 
import Banner from "./components/Banner/Banner";
import Products from "./components/Products/Products";

import headphones from "../src/assets/hero/headphone.png"
import smartwatch2 from "../src/assets/category/smartwatch2-removebg-preview.png"

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

const BannerData2 = {
  discount: "30% OFF",
  title: "Happy Hours",
  date: "14th Jan to 28th Jan",
  image: smartwatch2,
  title2: "Smart Solo",
  title3: "Christmas Sale",
  title4: "Up to 60% OFF",
  bgColor: '#2DCC6F',
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
      <Products/>
      <Banner data={BannerData2}/>
    </div>
  )
}

export default App
