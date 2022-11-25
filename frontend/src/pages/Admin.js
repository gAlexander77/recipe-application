import React,{useState} from "react";
import { Link } from "react-router-dom";
import NavigationBar from '../components/NavigationBar';

function Admin(){

    const [userType, setUserType] = useState(localStorage.getItem('userType'));

    function Recipes(){
        
        function Recipe({recipe, id}){

            const deleteRecipeHandler = () => {
                console.log("Recipe has been deleted")
            }

            return (
                <div className="moderate-recipe-container">
                    <h1>{recipe}</h1>
                    <Link to={"/recipe/"+id} state={id} onClick={() => console.log("clicked "+id)}>
                        <button>View Recipe</button>
                    </Link>
                    <button onClick={deleteRecipeHandler}> Delete Recipe</button>
                </div>
            );
        }
        
        return(
            <div className="moderate-recipes-container">
                <h1>Moderate Recipes</h1>
                <Recipe recipe="recipe" id={1}/>
            </div>
        );
    }

    function Comments(){

        function Comment({commentID,username,comment}){

            const deleteCommentHandler = () => {
                        console.log("Recipe has been deleted")
                    }

            return (
                <div className="moderate-comment-container">
                    <h1>{username} commented: </h1>
                    <p>{comment}</p>
                    <button>Delete Comment</button>
                </div>
            );
        }

        return(
            <div className="moderate-comments-container">
                <h1>Moderate Comments</h1>
                <Comment username="username" comment="example"/>
            </div>
        );
    }

    return (
        <div className="Admin">
            <div className="navbar">
                <NavigationBar {...{userType}}/>
            </div>
            <Recipes/>
            <Comments/>
        </div>
    );
}

export default Admin;