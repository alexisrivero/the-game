import React, { useState } from 'react';
import {BrowserHistory, BrowserRouter} from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import Contenido from './components/Contenido'



const App = () => {
  
  return (
    <BrowserRouter>
      <div className="App">
        <Header/>
        <Contenido />
      </div>
    </BrowserRouter>
  )
}

export default App;