import React, { useState }from 'react';
import RecipeCard from './RecipeCard'
import { FaAngleDown, FaSearch } from "react-icons/fa";
import '../styles/components/FeedStyle.css'

function Feed(){
    
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
            <div className="Header">
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
            <RecipeCard/>    
        </div>
        </div>
    );
}

export default Feed;