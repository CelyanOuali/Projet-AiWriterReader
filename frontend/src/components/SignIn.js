import React, { useState } from 'react';
// import '../css/SignIn.css';

function SignupPage() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

//   const handleSubmit = (e) => {
//     e.preventDefault();
//     // Envoyer les données du formulaire à votre backend
//     console.log(formData);
//     // Réinitialiser le formulaire
//     setFormData({ name: '', email: '', password: '' });
//   };

  return (
    <div className='wrapper'>
        <form action=''>
            <h1>Sign In</h1>
            <div className='input-box'>
                <input type="text" name="name" placeholder="Username" value={formData.name} onChange={handleChange} required/>
            </div>
            <div className='input-box'>
                <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} required/>
            </div>
            <div className='input-box'>
                <input type="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} required/>
            </div>
            <button type="submit" className='btn'>Sign In</button>
            <div className='register-link'>
                <p>Already have an account ?<a href='#'> Log In</a></p>
            </div>
        </form>
    </div>
  );
}

export default SignupPage;
