import React, { useState, useEffect } from 'react';
import '../css/Favorites.css';

function Favorites() {
    const [favoriteStories, setFavoriteStories] = useState([]);
    
    useEffect(() => {
        
    }, []);
    
    return (
        <div className='body-generate-story container'>
            <header className='header'>
                <h1>StoryCraft</h1>
                <nav className='nav-links'>
                    <a href='#' className='nav-link'>Home</a>
                    <a href='#' className='nav-link'>Favorites</a>
                    <a href='#' className='nav-link'>Community</a>
                    <button className='btn btn-primary btn-sm'>DECONNEXION</button>
                </nav>
            </header>
            <div className='favorites-page'>
                <h2>My Favorites</h2>

                {favoriteStories === 0 ? (
                    <p>No favorites yet !</p>
                ) : (
                    <ul>
                        {favoriteStories.map((story, index) => (
                            <li key={index}>{story}</li>
                        ))} 
                    </ul>
                )}
                
            </div>
        </div>
    );
}

export default Favorites;
