
import './index.css'
import App from './App.jsx'
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom';
import  Loginpage from "./LoginpageAndSignup/Loginpage.jsx"
import Signup from './LoginpageAndSignup/Signup.jsx';
import SkillSwapPage from './SkillSwapPage/SkillSwap.jsx';


createRoot(document.getElementById('root')).render(
  <BrowserRouter>
  
  <Routes>
<Route path='/' element={<App/>}></Route>
<Route path='/login' element={<Loginpage/>}></Route>
<Route path='/signup' element={<Signup/>}></Route>
<Route path='/SkillSwap' element={<SkillSwapPage/>}></Route>

  </Routes>
  </BrowserRouter>
  
  ,
)
