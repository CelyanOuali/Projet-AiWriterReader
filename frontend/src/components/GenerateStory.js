import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios'; 
import questions from '../questions';
import '../App.css';
import communauteImage from '../img/communaute.jpg';
import favImage from '../img/fav.png';
import { Link } from 'react-router-dom';

function GenerateStory() {
  const [answers, setAnswers] = useState(new Array(questions.length).fill(''));
  const [generatedStory, setGeneratedStory] = useState('');
  const textareaRef = useRef(null);

  const handleInputChange = (index, event) => {
    const newAnswers = [...answers];
    newAnswers[index] = event.target.value;
    setAnswers(newAnswers);
  };

  const addToFavorites = () => {
    
  };


  
  
  const generateStory = async () => {
    try {
      const response = await axios.post('http://localhost:8000/generate-story/', { answers });
      setGeneratedStory(response.data); 
      console.log('Story generated successfully:', response.data);
    } catch (error) {
      console.error('Error generating story:', error);
    }
  };
  
  




  // Défielment auto pendant la generation de l'histoire
  useEffect(() => {
    textareaRef.current.scrollTop = textareaRef.current.scrollHeight;
  }, [generatedStory]);

  const handleSubmit = (event) => {
    event.preventDefault();
    generateStory();
  };

  return (
    
    <div className='body-generate-story container'>
      <header className="header">
        <h1>StoryCraft</h1>
        <a href='#' className='nav-link'>Home</a>
        <a href='#' className='nav-link'>Favorites</a>
        <a href='#' className='nav-link'>Community</a>
        <Link to='/login'><button className="btn btn-primary btn-sm" style={{ marginLeft: 'auto' }}>DECONNEXION</button></Link>
      </header>
        <div className="question-box">
          {questions.map((question, index) => (
            <div key={index} className="question-item">
              <label>
                {question}
                {index === 0 || index === 2 || index === 3 || index === 4 || index === 6 || index === 7 || index === 8 || index === 9 || index === 10 || index === 12  ? (
                  <select value={answers[index]}  onChange={(event) => handleInputChange(index, event)} className="form-select">
                    
                    {index === 0 && [1, 2, 3, 4].map((num) => (
                      <option key={num} value={num}>{num}</option>
                    ))}
                    {index === 2 && ["Fantasy", "Science Fiction", "Mystery", "Adventure"].map((type) => (
                      <option key={type} value={type}>{type}</option>
                    ))}
                    {index === 3 && ["Past", "Present", "Future", "Urban", "Prehistoric", "Medieval"].map((type) => (
                      <option key={type} value={type}>{type}</option>
                    ))}
                    {index === 4 && ["Yes", "No"].map((type) => (
                      <option key={type} value={type}>{type}</option>
                    ))}
                    {index === 6 && ["Yes", "No"].map((type) => (
                      <option key={type} value={type}>{type}</option>
                    ))}
                    {index === 7 && ["Yes", "No"].map((type) => (
                      <option key={type} value={type}>{type}</option>
                    ))}
                    {index === 8 && ["Yes", "No"].map((type) => (
                      <option key={type} value={type}>{type}</option>
                    ))}
                    {index === 9 && ["Yes", "No"].map((type) => (
                      <option key={type} value={type}>{type}</option>
                    ))}
                    {index === 10 && [0, 1, 2, 3, 4].map((num) => (
                      <option key={num} value={num}>{num}</option>
                    ))}
                    {index === 12 && ["Monarchy", "Democracy", "Anarchy", "Dictatorship", "Managed Democracy"].map((type) => (
                      <option key={type} value={type}>{type}</option>
                    ))}

                  </select>
                ) : (
                  <input
                    type="text"
                    value={answers[index]}
                    onChange={(event) => handleInputChange(index, event)}
                    className="form-control"
                  />
                )}
              </label>
            </div>
          ))}
          
          {/* Génération histoir à partir des réponses utilisateur */}
          <button className="btn btn-primary btn-sm" type="submit" onClick={handleSubmit}>Generate User Prompt</button>
        </div>

        
        <div className='story-generated'>
          <form >
            <textarea 
              ref={textareaRef} 
              className='generated form-control' 
              value={generatedStory} 
              readOnly 
              style={{ 
                fontSize: '15px',
                fontFamily: 'Georgia',
                backgroundColor: 'rgb(226, 220, 212, 0.8)',
                color: '#333', 
                lineHeight: '1.5',
                padding: '25px',
                border: 'none',
                outline: 'none'
              }}
            />
          </form>

          <div className='btn button-container1'>
            <button className='btn btn-primary btn-sm' 
            >Play</button>

            <button className='btn btn-success btn-sm'
            >Save</button>
            <button onClick={addToFavorites} className='btn btn-warning btn-sm'
            >Add to favs</button>
          </div>
        </div>



        {/*Générer une histoire sur des paramètres aléatoires*/}
        <div className='story-generated'>
          <form >
            <textarea 
              ref={textareaRef} 
              className='generated form-control' 
              onChange={(event) => setGeneratedStory(event.target.value)}
              style={{ 
                fontSize: '15px',
                fontFamily: 'Georgia',
                backgroundColor: 'rgb(226, 220, 212, 0.8)',
                color: '#333', 
                lineHeight: '1.5',
                padding: '25px',
                border: 'none',
                outline: 'none'
              }}
            />
          </form>
          
          <div className="button-container2">
            <button className='btn btn-primary btn-sm'
            >Generate Random Prompt</button>
            <button className='btn btn-primary btn-sm'
            >Play</button>
            <button className='btn btn-success btn-sm'
            >Save</button>
            <button onClick={addToFavorites} className='btn btn-warning btn-sm'
            >Add to favs</button>
          </div>
        </div>
        
        <div className='comment-form'>
          <h4 className='leave-comment'>Leave comment below !</h4>
          <form >
            <textarea 
              ref={textareaRef} 
              className='comment form-control'
              style={{ 
                fontSize: '13px',
                fontFamily: 'Georgia', 
                backgroundColor: 'rgb(226, 220, 212, 0.8)',
                color: '#333', 
                lineHeight: '1.5',
                padding: '25px',
                border: 'none',
                outline: 'none'
              }}
            />
          </form>
          <button className='button-container3 btn btn-primary btn-sm'>Send</button>
        </div>
        
        <div className='commu-fav'>
          <div className="fav">
            <a href="#" target="_blank">
              <img src={favImage} alt="communauté"/>
              <h3>My favorite stories</h3>
            </a>
          </div>

          <div className="commu">
            <a href="#" target="_blank">
              <img src={communauteImage} alt="communauté"/>
              <h3>Community</h3>
            </a>
          </div>
        </div>
    </div>
  );
}

export default GenerateStory;
