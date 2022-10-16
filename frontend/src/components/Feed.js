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

    const [sortBy, setSortBy] = useState('recent')
    const sortList = ['Recently Added', 'Most popular'];

    const [recipe, setRecipe] = useState([])
    
    /* Test Mock API */
    useEffect(()=>{
        axios.get('http://localhost:3001/recipes').then(res => {
        setRecipe(res.data)
        }).catch(error => alert('API ERROR'));
      }, []);

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
            {recipe.map(recipe =>{
                return(
                    <RecipeCard
                     key = {recipe.id}
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