import React, { useState, useEffect }from 'react';
import axios from 'axios';
import RecipeCard from './RecipeCard';
import { FaAngleDown, FaAngleUp} from "react-icons/fa";
import { BsSearch } from "react-icons/bs";
import '../styles/components/FeedStyle.css';

import hostname from '../hostname';

function Feed(){

    const [sortBy, setSortBy] = useState('Filter Results')
    const sortList = ['Recently Added', 'Most Popular'];

    const [recipes, setRecipes] = useState([])
    
    /* Test Mock API */
    useEffect(()=>{
        axios.get(hostname+'/recipes').then(res => {
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

    function DropdownMenu(props){
        return(props.trigger)?(
            <div className="dropdown-box">
                <div className="dropdown-row" onClick={sortByRank}>{sortList[0]}</div>
                <div className="dropdown-row" onClick={sortByMostRecent}>{sortList[1]}</div>
            </div>
        ):"";
}

    function SortByButton(){
        const [dropdown, setDropdown] = useState(false)
        
        const Angle = () => {
            if (dropdown===false) return(<FaAngleDown className="angle"/>);
            else return (<FaAngleUp className="angle"/>);
        }
        
        return (
            <div className="sort-by-container">
                <button className="filter" onClick={() => setDropdown(!dropdown)}><p className="filter-text">{sortBy}</p><Angle/></button>
                <DropdownMenu trigger={dropdown} setTrigger={setDropdown}/>
            </div>
        );
    }

    return (
        <div className="Feed">
            <div className="Header glass">
                <SortByButton></SortByButton>
                <div className="search-box-container">
                    <BsSearch className="search-icon"/>
                    <input type="text" className="search-box" placeholder="Search" onChange={searchHandler} value={search}/>
                </div>
            </div>
        <div className="content">
        <DropdownMenu/>
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