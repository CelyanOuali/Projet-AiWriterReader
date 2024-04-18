//generateStory.js

import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios'; 
import questions from '../questions';
import '../App.css';
import communauteImage from '../img/communaute.jpg';
import favImage from '../img/fav.png';

function GenerateStoryForm() {
  const [answers, setAnswers] = useState(new Array(questions.length).fill(''));
  const [generatedStory, setGeneratedStory] = useState('');
  const textareaRef = useRef(null);

  const handleInputChange = (index, event) => {
    const newAnswers = [...answers];
    newAnswers[index] = event.target.value;
    setAnswers(newAnswers);
  };

  
  const generateStory = () => {
    const initialStory = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed leo risus, euismod a lobortis at, dictum mattis mauris. Pellentesque eu sem nibh. Nullam ac leo dui. Fusce ac lectus sem. Ut sit amet accumsan libero. Morbi eget ante rhoncus felis luctus bibendum. Sed porttitor, augue vitae gravida aliquam, velit ex posuere enim, ac tristique augue libero sed quam. Vivamus fermentum vulputate augue, eget fringilla enim accumsan et. Nulla quis tempor odio. Donec feugiat dignissim gravida. Fusce sit amet pellentesque augue. Sed id risus rhoncus, viverra neque quis, facilisis lorem. Proin vitae odio nunc. Suspendisse ut felis pretium, molestie libero id, pharetra purus. Ut nec porta nibh, dapibus aliquam massa. Morbi scelerisque egestas dignissim. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean tempor viverra condimentum. Cras luctus et erat ut finibus. Sed tristique bibendum enim, fermentum pharetra nunc. Curabitur viverra lectus ac velit auctor, a dictum sem lacinia. Vestibulum nec nisl vitae elit aliquet rhoncus. Aliquam faucibus mi at urna placerat, nec pharetra enim posuere. Mauris pulvinar suscipit est, eget ultricies est accumsan sed. Curabitur bibendum leo sapien, vitae consectetur arcu pharetra vitae. Suspendisse libero neque, laoreet ut ultrices in, laoreet nec nulla. In et enim maximus sapien gravida tincidunt. Aliquam erat volutpat. Suspendisse sagittis purus vitae erat interdum ornare. Etiam aliquam risus vel ullamcorper euismod. Praesent non dui ipsum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam dapibus, tortor vitae interdum auctor, eros nibh tristique lorem, sed ornare felis erat sit amet diam. Phasellus tempus ligula erat, at dignissim eros tempus varius. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Proin nec dui massa. Phasellus commodo tortor sed felis sollicitudin vulputate sit amet a turpis. Nullam nibh ex, sodales eu massa a, mattis malesuada quam. Morbi sit amet quam eget nibh dignissim cursus. Integer sed venenatis ex. Sed tincidunt arcu sed felis posuere viverra. ";
    let index = 0;
    let story = "";
    const timer = setInterval(() => {
      story += initialStory[index];
      setGeneratedStory(story);
      index++;
      if (index === initialStory.length) {
        clearInterval(timer);
      }
    }, 30); 
  };
  
  /*
  const generateStory = async () => {
    try {
      const response = await axios.post('http://localhost:8000/generate-story/', { answers });
      setGeneratedStory(response.data); // Assuming the response directly contains the generated story
      console.log('Story generated successfully:', response.data);
    } catch (error) {
      console.error('Error generating story:', error);
    }
  };
  */
  




  // Défielment auto pendant la generation de l'histoire
  useEffect(() => {
    textareaRef.current.scrollTop = textareaRef.current.scrollHeight;
  }, [generatedStory]);

  const handleSubmit = (event) => {
    event.preventDefault();
    generateStory();
  };

  return (
    
    <div className='box'>
      <header className="header">
        <h1>AIStoryWriter</h1>
        <button className="logout-button">DECONNEXION</button>
      </header>
        <div className="question-box">
          {questions.map((question, index) => (
            <div key={index} className="question-item">
              <label>
                {question}
                {index === 0 || index === 2 || index === 3 || index === 4 || index === 6 || index === 7 || index === 8 || index === 9 || index === 10 || index === 12  ? (
                  <select value={answers[index]}  onChange={(event) => handleInputChange(index, event)}>
                    
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
                  />
                )}
              </label>
            </div>
          ))}
          
          {/* Génération histoir à partir des réponses utilisateur */}
          <button className="generate-button" type="submit" onClick={handleSubmit}
          style={{
            marginRight: '10px',
            padding: '5px 9px',
            border: '2px solid #333',
            borderRadius: '5px',
            backgroundColor: 'rgb(226, 220, 212)',
            color: 'black',
            fontSize: '15px',
            cursor: 'pointer'
          }}>Generate User Prompt</button>
        </div>

        
        <div className='story-generated'>
          <form >
            <textarea 
              ref={textareaRef} 
              className='generated' 
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

          <div className='btn'>
            <button className='play-button'
            style={{
              marginRight: '10px',
              padding: '5px 9px',
              border: '2px solid #333',
              borderRadius: '5px',
              backgroundColor: 'rgb(226, 220, 212)',
              color: 'black',
              fontSize: '15px',
              cursor: 'pointer',
            }}>Play</button>

            <button className='save-button'
            style={{
              marginRight: '10px',
              padding: '5px 9px',
              border: '2px solid #333',
              borderRadius: '5px',
              backgroundColor: 'rgb(226, 220, 212)',
              color: 'black',
              fontSize: '15px',
              cursor: 'pointer',
            }}>Save</button>
            <button className='fav-button'
            style={{
              marginRight: '10px',
              padding: '5px 9px',
              border: '2px solid #333',
              borderRadius: '5px',
              backgroundColor: 'rgb(226, 220, 212)',
              color: 'black',
              fontSize: '15px',
              cursor: 'pointer',
            }}>Add to favs</button>
          </div>
        </div>



        {/*Générer une histoire sur des paramètres aléatoires*/}
        <div className='story-generated'>
          <form >
            <textarea 
              ref={textareaRef} 
              className='generated' 
              // value={generatedStory}
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
          
          <div>
            <button className='random-button'
            style={{
              marginRight: '10px',
              padding: '5px 9px',
              border: '2px solid #333',
              borderRadius: '5px',
              backgroundColor: 'rgb(226, 220, 212)',
              color: 'black',
              fontSize: '15px',
              cursor: 'pointer',
            }}>Generate Random Prompt</button>
            <button className='play-button'
            style={{
              marginRight: '10px',
              padding: '5px 9px',
              border: '2px solid #333',
              borderRadius: '5px',
              backgroundColor: 'rgb(226, 220, 212)',
              color: 'black',
              fontSize: '15px',
              cursor: 'pointer',
            }}>Play</button>
            <button className='save-button'
            style={{
              marginRight: '10px',
              padding: '5px 9px',
              border: '2px solid #333',
              borderRadius: '5px',
              backgroundColor: 'rgb(226, 220, 212)',
              color: 'black',
              fontSize: '15px',
              cursor: 'pointer',
            }}>Save</button>
            <button className='fav-button'
            style={{
              marginRight: '10px',
              padding: '5px 9px',
              border: '2px solid #333',
              borderRadius: '5px',
              backgroundColor: 'rgb(226, 220, 212)',
              color: 'black',
              fontSize: '15px',
              cursor: 'pointer',
            }}>Add to favs</button>
          </div>
        </div>
        
        <div>
          <div>
          <h4 className='leave-comment'>Leave comment below !</h4>
          <form >
            <textarea 
              ref={textareaRef} 
              className='comment'
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
          <button className='send-button'>Send</button>
          </div>
          

          <div className="projet">
            <a href="#" target="_blank">
              <img src={favImage} alt="communauté"/>
              <h3>Your favorite stories</h3>
            </a>
          </div>

          <div className="projet">
            <a href="#" target="_blank">
              <img src={communauteImage} alt="communauté"/>
              <h3>Community</h3>
            </a>
          </div>
        </div>
    </div>
  );
}

export default GenerateStoryForm;
