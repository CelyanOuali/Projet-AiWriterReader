import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import GenerateStory from './components/GenerateStory';
import Favorites from './components/Favorites';


function App() {
  return (
      <div>
        {/* <Favorites /> */}
        <BrowserRouter>
          <Routes>
            <Route index element={<Signup />} />
            <Route path="/login" element={<Login />} /> 
            <Route path="/generatestory" element={<GenerateStory />} /> 
            <Route index element={<Login />} />
            <Route path="/signup" element={<Signup />} />
          </Routes>
        </BrowserRouter>
      </div>
  );
}

export default App;
