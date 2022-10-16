import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Account from './pages/Account';
import Recipe from './pages/Recipe';
import RecipeCard from './components/RecipeCard';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/account" element={<Account/>}/>
        <Route path="/recipe/:id" element={<Recipe/>}/>
        <Route path="/recipecard" element={<RecipeCard/>}/>
      </Routes>
    </Router>
  );
}

export default App;
