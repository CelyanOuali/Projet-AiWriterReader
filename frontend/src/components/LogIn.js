import React, { useState } from 'react';
import '../css/LogIn.css';

function LoginPage() {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // const handleSubmit = (e) => {
  //   e.preventDefault();
  //   // Envoyer les données du formulaire à votre backend
  //   console.log(formData);
  //   // Réinitialiser le formulaire
  //   setFormData({ email: '', password: '' });
  // };

  return (
    <div className='wrapper'>
        <form action=''>
            <h1>Log In</h1>
            <div className='input-box'>
                <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} required/>
            </div>
            <div className='input-box'>
                <input type="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} required/>
            </div>
            <button type="submit" className='btn'>Login</button>
            <div className='register-link'>
                <p>Don't have an account ? <a href='#'> Sign In</a></p>
            </div>
        </form>
    </div>
  );
}

export default LoginPage;