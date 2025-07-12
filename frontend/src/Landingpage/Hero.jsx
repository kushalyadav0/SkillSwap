import { useState, useEffect } from 'react';

export default function Hero() {
   // Image URLs for the slider
  const slides = [

    '../src/assets/img3.jpg',
    '../src/assets/img2.jpg',
    '../src/assets/img.jpg',
    
   
    
  ];

  const [currentSlide, setCurrentSlide] = useState(0);

  // Quick hack for auto-slide every 5s
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % slides.length);
    }, 5000);
    return () => clearInterval(timer); // Cleanup
  }, [slides.length]);

  // Handle dot navigation
  const goToSlide = (index) => {
    setCurrentSlide(index);
  };
  
    return (
  
    <>
    
 <div className="@container pt-6 pb-6 pl-4 pr-4 sm:pt-8 sm:pb-8 sm:pl-10 sm:pr-10 md:pl-20 md:pr-20 md:pt-10 md:pb-10">
      <div className="@[480px]:p-10">
        <div
          className="flex bg-no-repeat bg-cover bg-center min-h-[360px] sm:min-h-[480px] flex-col gap-6 items-center justify-center p-4 sm:p-6 @[480px]:gap-8 @[480px]:rounded-xl transition-all duration-500 relative"
          style={{ backgroundImage: `linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.4)), url('${slides[currentSlide]}')` }}
        >
          <div className="flex flex-col gap-2 text-center">
            <h1 className="text-3xl sm:text-4xl md:text-5xl text-white font-black tracking-[-0.033em] leading-tight">
              Swap skills. Grow together.
            </h1>
            <h2 className="text-white font-normal text-xs sm:text-sm md:text-base leading-normal">
              Connect with a community of learners and experts to exchange skills and knowledge.
            </h2>
          </div>
          <div className="justify-center flex flex-wrap gap-3">
            <button className="h-8 px-3 sm:h-10 sm:px-4 md:h-12 md:px-5 flex min-w-[84px] max-w-[480px] items-center justify-center bg-[#2094f3] text-slate-50 text-xs sm:text-sm md:text-base font-bold rounded-xl cursor-pointer overflow-hidden tracking-[0.015em]">
              <span className="truncate">Join Now</span>
            </button>
            <button className="h-8 px-3 sm:h-10 sm:px-4 md:h-12 md:px-5 flex min-w-[84px] max-w-[480px] items-center justify-center bg-[#e7eef4] text-[#0d151c] text-xs sm:text-sm md:text-base font-bold rounded-xl cursor-pointer overflow-hidden tracking-[0.015em]">
              <span className="truncate">Browse Skills</span>
            </button>
          </div>
          {/* Navigation dots for slider */}
          <div className="bottom-4 gap-2 absolute flex">
            {slides.map((_, idx) => (
              <button
                key={idx}
                onClick={() => goToSlide(idx)}
                className={`h-2 w-2 sm:h-3 sm:w-3 rounded-full transition-opacity duration-300 ${currentSlide === idx ? 'bg-white' : 'bg-white/50'}`}
                aria-label={`Slide ${idx + 1}`}
              />
            ))}
          </div>
        </div>
      </div>
      {/* TODO: Add swipe support for mobile */}
    </div>
    
    
    </>
  );
}