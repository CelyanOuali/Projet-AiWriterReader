// App.js
import React from 'react';
import LogIn from './components/LogIn';
import SignIn from './components/SignIn';
import GenerateStory from './components/GenerateStory';

import './App.css';

function App() {
  return (
      <div>
        <GenerateStory/>
      
      {/*
      <div className="App">
      <h1 className='title'>AIStoryWriter</h1>
      <hr></hr>
      <GenerateStory />
      <GenerateButton />
      <StoryDisplay />
      <SaveButton />
      */}
      </div>
  );
}

export default App;
