import React, { useState } from 'react';
import {BrowserHistory, BrowserRouter} from 'react-router-dom';
import './App.css';
import Header from './components/Header';




const App = () => {
  
  return (
    <BrowserRouter>
      <div className="App">
        <Header/>
      </div>
    </BrowserRouter>
  )
}

export default App;