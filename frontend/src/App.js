import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Account from './pages/Account';
import Recipe from './pages/Recipe';
import Admin from './pages/Admin';
import Error404 from './pages/Error404';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/account" element={<Account/>}/>
        <Route path="/recipe/:id" element={<Recipe/>}/>
        <Route path="/admin" element={<Admin/>}/>
        <Route path="/*" element={<Error404/>}/>
      </Routes>
    </Router>
  );
}

export default App;
