import React from 'react';
import Navbar from '../Navbar';
import Hero from './Hero';
import HowItWorks from './HowItWorks';
import KeyFeatures from './KeyFeatures';
import Testimonials from './Testimonials';
import Footer from '../Footer';

export default function HomePage(){
    return(
<div className="bg-gray-100 min-h-screen text-gray-800 ">
      <Navbar />
      <Hero/>
      <HowItWorks />
      <KeyFeatures />
      <Testimonials />
      <Footer />
    </div>
    

)
} 