import { useState } from "react";
import { Bars3Icon, XMarkIcon } from "@heroicons/react/24/outline";
import { Link } from "react-router-dom";

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-gradient-to-r from-[#f5f9ff] via-[#d4ecff] to-[#f5f9ff] border-b border-[#e0eaf2] px-4 sm:px-10 py-3 shadow-sm">
      <div className="flex justify-between items-center">
        {/* Logo */}
        <div className="flex items-center gap-2 text-[#0d151c]">
          <div className="w-5 h-5">
            <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                fillRule="evenodd"
                clipRule="evenodd"
                d="M24 0.757355L47.2426 24L24 47.2426L0.757355 24L24 0.757355ZM21 35.7574V12.2426L9.24264 24L21 35.7574Z"
                fill="currentColor"
              />
            </svg>
          </div>
          <h2 className="text-lg font-bold tracking-tight">SkillSwap</h2>
        </div>

        {/* Desktop Links */}
        <nav className="hidden sm:flex items-center gap-6 text-sm font-medium text-[#0d151c]">
          <a href="#" className="hover:underline">Browse</a>
          <a href="/skillswap" className="hover:underline">Learn</a>
          <a href="#" className="hover:underline">Teach</a>
        </nav>

        {/* Desktop Buttons */}
<div className="hidden sm:flex gap-2">
  <Link to="/signup">
    <button className="h-10 px-4 rounded-xl bg-[#2094f3] text-white text-sm font-semibold shadow hover:bg-[#127ddb] transition">
      Sign Up
    </button>
  </Link>
  <Link to="/login">
    <button className="h-10 px-4 rounded-xl bg-[#e7eef4] text-[#0d151c] text-sm font-semibold hover:bg-[#dce4eb] transition">
      Log In
    </button>
  </Link>
</div>


        {/* Mobile Menu Toggle */}
        <button
          onClick={() => setIsOpen(!isOpen)}
          className="sm:hidden text-[#0d151c] focus:outline-none"
        >
          {isOpen ? <XMarkIcon className="w-6 h-6" /> : <Bars3Icon className="w-6 h-6" />}
        </button>
      </div>
{/* Mobile Dropdown */}
<div className="sm:hidden mt-3 flex flex-col gap-3 px-2 text-center">
  <a href="#" className="text-[#0d151c] text-sm font-medium hover:underline">Browse</a>
  <a href="#" className="text-[#0d151c] text-sm font-medium hover:underline">Learn</a>
  <a href="#" className="text-[#0d151c] text-sm font-medium hover:underline">Teach</a>
  
  <Link to="/signup">
    <button className="mt-2 h-10 rounded-xl bg-[#2094f3] text-white text-sm font-semibold">
      Sign Up
    </button>
  </Link>
  <Link to="/login">
    <button className="h-10 rounded-xl bg-[#e7eef4] text-[#0d151c] text-sm font-semibold">
      Log In
    </button>
  </Link>
</div>

    </header>
  );
}
