import React, { useState, useEffect }from 'react';
import axios from 'axios';
import RecipeCard from './RecipeCard';
import { FaAngleDown, FaSearch } from "react-icons/fa";
import '../styles/components/FeedStyle.css';

function Feed(){
    
    /*
    const description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet purus ac egestas egestas consequat donec aliquam senectus. Senectus varius et ac ac feugiat. Magna aliquam aliquam elit, placerat at. Eu faucibus sed nisl aliquam.'
    const image = 'https://makeyourmeals.com/wp-content/uploads/2019/03/air-fryer-hamburger.jpg';
    <RecipeCard image={image} name='Hamburger' desc={description} rating={4.2} />
    */

    const [sortBy, setSortBy] = useState('Filter Results')
    const sortList = ['Recently Added', 'Most popular'];

    const [recipe, setRecipe] = useState([])
    
    /* Test Mock API */
    useEffect(()=>{
        axios.get('https://f3fad6f8-6516-4627-a8dd-ac467a4107cf.mock.pstmn.io/recipes').then(res => {
        setRecipe(res.data)
        }).catch(error => alert('API ERROR'));
      }, []);

    

    const [search, setSearch] = useState([])

    
    
    const [sorting, setSorting] = useState(false)
    useEffect(()=>{},[sorting])
    
    const sortByRank = () => {
        recipe.sort(function compare(a, b){
            if(a.rating > b.rating) return -1;
            if(a.rating < b.rating) return 1;
            return 0;});
        setSorting(!sorting);
    }

    const sortByMostRecent = () => {
        recipe.sort(function compare(a, b){
            if(a.id > b.id) return -1;
            if(a.id < b.id) return 1;
            return 0;});
        setSorting(!sorting);
    }

    const searchHandler = evt => {
        setSearch(evt.target.value.toLowerCase())
    }
    const filterRecipes = recipe.filter(recipe => 
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

    function Header(){
        return (
            <div className="Header glass">
                <SortByButton></SortByButton>
                <div className="search-box-container">
                    <input type="text" className="search" placeholder="Search" onChange={searchHandler} value={search}/>
                    <FaSearch/>
                </div>
            </div>
        );
    }

    return (
        <div className="Feed">
        <Header/>
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