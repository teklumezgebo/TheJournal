import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Landing from './pages/Landing';
import SignUpForm from './features/authentication/SignUpForm';
import LoginForm from './features/authentication/LoginForm';

function App() {
  return (
      <Routes>
         <Route path='/' element={<Landing />} />
         <Route path='/signup' element={<SignUpForm />} />
         <Route path='/login' element={<LoginForm />} />
      </Routes>
  );
}

export default App;