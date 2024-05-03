import React, { useState } from 'react';
import '../css/Signup.css';
import { Link } from "react-router-dom";
import axios from 'axios';

function Signup() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: ''
  });

  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };


  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        await axios.post('http://localhost:8000/api/signup/', formData);
        setMessage('User created successfully!');
    } catch (error) {
        console.error('Error:', error);
    }
};

  return (
    <div className='body-signin vh-100 d-flex justify-content-center align-items-center'>
        <div>
            <form onSubmit={handleSubmit}>
                <h1 className='text-center mb-4'>Sign Up</h1>
                <div className='form-group'>
                    <input type="text" name="name" className='form-control' placeholder="Username" value={formData.name} onChange={handleChange} required/>
                </div>
                <div className='form-group'>
                    <input type="email" name="email" className='form-control' placeholder="Email" value={formData.email} onChange={handleChange} required/>
                </div>
                <div className='form-group'>
                    <input type="password" name="password" className='form-control' placeholder="Password" value={formData.password} onChange={handleChange} required/>
                </div>
                <button type="submit" className='btn btn-primary btn-block'>Sign Up</button>
                
                {message && <div className="text-center mt-3"><p className="text-success">{message}</p></div>}
                
                <div className='text-center mt-3'>
                    <p>Already have an account? <Link to='/login'>Log In</Link></p>
                </div>
            </form>
        </div>
    </div>
  );
}

export default Signup;
