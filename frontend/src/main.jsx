
import './index.css'
import App from './App.jsx'
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom';
import  Loginpage from "./Loginpage/Loginpage.jsx"

createRoot(document.getElementById('root')).render(
  <BrowserRouter>
  
  <Routes>
<Route path='/' element={<App/>}></Route>
<Route path='/login' element={<Loginpage/>}></Route>
<Route path='/signup' element={<signup/>}></Route>


  </Routes>
  </BrowserRouter>
  
  ,
)
