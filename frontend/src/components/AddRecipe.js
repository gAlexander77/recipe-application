import React from 'react';
import { BsXLg } from "react-icons/bs";
import '../styles/components/AddRecipeStyle.css'; 

function AddRecipe(){
    return(
        <div className="popup">
            <form className="popup-inner">
                <BsXLg/>
                <label>Name of Recipe: </label>
                <input type="text" placeholder="Name of recipe"></input>
                <label>Description: </label>
                <input type="text" placeholder="Description of your Recipe"></input>
                <label>Instructions: </label>
                <input type="text" placeholder="Instructions"></input>
                <button>Post Recipe</button>
            </form>
        </div>
    );   
}

export default AddRecipe;