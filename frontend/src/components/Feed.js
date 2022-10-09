import React, { useState }from 'react';
import RecipeCard from './RecipeCard'
import { FaAngleDown, FaSearch } from "react-icons/fa";
import '../styles/components/FeedStyle.css'

function Feed(){
    
    const description = 'A hamburger, or simply burger, is a food consisting of fillings—usually a patty of ground meat, typically beef—placed inside a sliced bun or bread roll. Hamburgers are often served with cheese, lettuce, tomato, onion, pickles, bacon, or chilis; condiments such as ketchup, mustard, mayonnaise, relish, or a "special sauce", often a variation of Thousand Island dressing; and are frequently placed on sesame seed buns.'
    const image = 'https://makeyourmeals.com/wp-content/uploads/2019/03/air-fryer-hamburger.jpg';

    const [setSortBy, sortBy] = useState('recent')
    const sortList = ['Recently Added', 'Most popular'];

    const Sort = () => {
        return (
            <div className="Sort">
                Recently Added
            </div>
        );
    }

    function Header(){
        return (
            <div className="Header glass">
                <div className="sort-by-container">
                    Recently Added<FaAngleDown/>
                </div>
                <div className="search-box-container">
                    <input type="text" className="search" placeholder="Search"/>
                    <FaSearch/>
                </div>
            </div>
        );
    }

    return (
        <div className="Feed">
        <Header/>
        <div className="content">
            <RecipeCard image={image} name='Hamburger' desc={description} rating={5} />
            <RecipeCard/>
            <RecipeCard/>
            <RecipeCard/>
            <RecipeCard/>
            <RecipeCard/>
            <RecipeCard/>
            <RecipeCard/>
            <RecipeCard/>
            <RecipeCard/>
            <RecipeCard/>
            <RecipeCard/>
            <RecipeCard/>
            <RecipeCard/>
            <RecipeCard/>
            <RecipeCard/>    
        </div>
        </div>
    );
}

export default Feed;