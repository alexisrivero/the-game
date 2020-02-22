import React from 'react';
import { BrowserRouter} from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import Footer from './components/Footer';
import Contenido from './components/Contenido'



const App = () => {
  
  return (
    <BrowserRouter>
      <div className="App">
        <Header/>
        <Contenido />
        <Footer />
      </div>
    </BrowserRouter>
  )
}

export default App;