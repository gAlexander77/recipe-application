import React, {useState} from 'react';
import { Link } from "react-router-dom";
import { FaHome } from "react-icons/fa";
import AddRecipe from "./AddRecipe";
import '../styles/components/NavigationBarStyle.css'

function NavigationBar({userType}){  

    const [recipePopUp, setRecipePopUp] = useState(false);

    const recipePopUpHandler = () => {
        setRecipePopUp(!recipePopUp)
        console.log(recipePopUp)
    }


    const User = () => {
        if (userType === 'user'){
            return(
                <div className="user-account">
                    <button onClick={recipePopUpHandler}>Post A Recipe</button>
                    <Link to="/account">
                    My Account
                    </Link>
                </div>
            );
        }
        else{
            return(
                <div className="user-account">
                    <Link to="/login">
                    Create Account
                    </Link>
                </div>    
            );
        }
    
    }

    const AddRecipePopUp = () => {
        if (recipePopUp === true){ 
            return(
                <AddRecipe></AddRecipe>
            );}
    }

    return (
        <div className="NavigationBar">
            
            <Link to="/" className="icon-link">
                <FaHome className="icon"/>
            </Link>
            
            <User/>

            <AddRecipePopUp/>
        </div>
    );
}

export default NavigationBar;