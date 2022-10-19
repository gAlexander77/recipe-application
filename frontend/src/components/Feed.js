import React, { useState, useEffect }from 'react';
import axios from 'axios';
import RecipeCard from './RecipeCard';
import { FaAngleDown, FaSearch } from "react-icons/fa";
import '../styles/components/FeedStyle.css';

function Feed(){

    const [sortBy, setSortBy] = useState('Filter Results')
    const sortList = ['Recently Added', 'Most popular'];

    const [recipes, setRecipes] = useState([])
    
    /* Test Mock API */
    useEffect(()=>{
        axios.get('https://f3fad6f8-6516-4627-a8dd-ac467a4107cf.mock.pstmn.io/recipes').then(res => {
        setRecipes(res.data)
        }).catch(error => alert('API ERROR'));
      }, []);

    

    const [search, setSearch] = useState([]);
    
    
    const [sorting, setSorting] = useState(false)
    useEffect(()=>{console.log("Sorting Activated useEffect");},[sorting])
    
    const sortByRank = () => {
        recipes.sort(function compare(a, b){
            if(a.rating > b.rating) return -1;
            if(a.rating < b.rating) return 1;
            return 0;});
        setSorting(!sorting);
        console.log("Sorting By Rank");
    }

    const sortByMostRecent = () => {
        recipes.sort(function compare(a, b){
            if(a.id > b.id) return -1;
            if(a.id < b.id) return 1;
            return 0;});
        setSorting(!sorting);
        console.log("Sorting by Most Recent");
    }

    const searchHandler = (evt) => {
        setSearch(evt.target.value.toLowerCase())
    }
    const filterRecipes = recipes.filter(recipe => 
        recipe.recipe_name.toLowerCase().includes(search)    
    );

    function SortOpitons(){
        <div className="sort-options-box">  
            <button onClick={() => setSortBy(sortList[0])}>{sortList[0]}</button>
            <button onClick={() => setSortBy(sortList[1])}>{sortList[1]}</button>
        </div>
    }

    function SortByButton(){
        return (
            <div className="sort-by-container">
                <button>{sortBy}<FaAngleDown/></button>
                <button onClick={sortByRank}>Rank</button>
                <button onClick={sortByMostRecent}>Most Recent</button>
            </div>
        );
    }

    return (
        <div className="Feed">
            <div className="Header glass">
                <SortByButton></SortByButton>
                <div className="search-box-container">
                    <input type="text" className="search" placeholder="Search" onChange={searchHandler} value={search}/>
                    <FaSearch/>
                </div>
            </div>
        <div className="content">
            {filterRecipes.map((recipe, index) =>{
                return(
                    <RecipeCard
                     key = {index}
                     id = {recipe.id}
                     image={recipe.image} 
                     name={recipe.recipe_name} 
                     desc={recipe.description} 
                     rating={recipe.rating}
                    />
                );
            }
            )}
        </div>
        </div>
    );
}

export default Feed;