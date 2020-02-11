import React, { useState } from 'react';
import './App.css';
import Chorizo from './components/Chorizo';
import Thegame from './components/Thegame';
import CIALOGO from './components/images/logo.jpg';


function App() {
  let texto = "thegame trevisan";
  const [thegame, setThegame] = useState(false);
  if (thegame) {
    texto = "CHICHO FERRIO";
  }
  function handleClick() {
    setThegame(!thegame);
  }
  return (
    <div className="App">
      <h1>{texto}</h1>
      <button onClick={handleClick}>hola</button>
      <Thegame />
      <Chorizo />
      <img src={CIALOGO} alt="LACIABRO" className="logo" />
    </div>
  )
}

export default App;
