import React, {useState} from 'react';
import { Link } from "react-router-dom";
import { FaHome, FaPaperPlane } from "react-icons/fa";
import AddRecipe from "./AddRecipe";
import '../styles/components/NavigationBarStyle.css'

function NavigationBar({userType}){  

    const [recipePopUp, setRecipePopUp] = useState(false);

    const recipePopUpHandler = () => {
        setRecipePopUp(true)
        console.log(recipePopUp)
    }

    const User = () => {
        if (userType === 'user'){
            return(
                <div className="user-account">
                    <button className="post-btn" onClick={recipePopUpHandler}>
                        Post Recipe <FaPaperPlane className="post-btn-icon"/>
                    </button>
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

    return (
        <div className="NavigationBar">
            <Link to="/" className="icon-link">
                <FaHome className="icon"/>
            </Link>
                
            <User/>

            <AddRecipe trigger={recipePopUp} setTrigger={setRecipePopUp}/>
        </div>
    );
}

export default NavigationBar;