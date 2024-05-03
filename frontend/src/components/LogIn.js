import React, { useState } from 'react';
import '../css/Login.css';
import { Link } from 'react-router-dom';


function Login() {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

 

  return (
    <div className='body-login vh-100 d-flex justify-content-center align-items-center'>
        <div>
            <form>
                <h1 className='text-center mb-4'>Log In</h1>
                <div className='form-group'>
                    <input type="name" name="name" className='form-control' placeholder="Username" value={formData.name} onChange={handleChange} required/>
                </div>
                <div className='form-group'>
                    <input type="password" name="password" className='form-control' placeholder="Password" value={formData.password} onChange={handleChange} required/>
                </div>
                <Link to='/generatestory'><button type="submit" className='btn btn-primary btn-block'>Log In</button></Link>
                <div className='text-center mt-3'>
                    <p>Don't have an account? <Link to='/signup'>Sign Up</Link></p>
                </div>
            </form>
        </div>
    </div>
  );
}

export default Login;