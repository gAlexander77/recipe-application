import React,{useState} from "react";
import { Link } from "react-router-dom";
import NavigationBar from '../components/NavigationBar';
import '../styles/AdminStyle.css';

function Admin(){

    const [userType, setUserType] = useState(localStorage.getItem('userType'));

    function Recipes(){
        
        function Recipe({recipe, id}){

            const deleteRecipeHandler = () => {
                console.log("Recipe "+id+" has been deleted")
            }

            return (
                <div className="moderate-recipe-container">
                    <Link className="recipe-name-link" to={"/recipe/"+id} state={id} onClick={() => console.log("clicked "+id)}>
                        {recipe}
                    </Link>
                    <button className="admin-delete-recipe-btn" onClick={deleteRecipeHandler}> Delete Recipe</button>
                </div>
            );
        }
        
        return(
            <div className="moderate-recipes-container">
                <h1 className="moderate-recipes-header">Moderate Recipes</h1>
                <Recipe recipe="Recipe 1" id={1}/>
                <Recipe recipe="Recipe 2" id={2}/>
                <Recipe recipe="Recipe 3" id={3}/>
                <Recipe recipe="Recipe 4" id={4}/>
                <Recipe recipe="Recipe 5" id={5}/>
                <Recipe recipe="Recipe 6" id={6}/>
                <Recipe recipe="Recipe 7" id={7}/>
            </div>
        );
    }

    function Comments(){

        function Comment({commentID,username,comment}){

            const deleteCommentHandler = () => {
                        console.log("Comment "+commentID+" has been deleted")
                    }

            return (
                <div className="moderate-comment-container">
                    <h1 className="username-commented">{username} commented: </h1>
                    <p className="admin-comment">{comment}</p>
                    <button className="admin-comment-recipe-btn" onClick={deleteCommentHandler}>Delete Comment</button>
                </div>
            );
        }

        return(
            <div className="moderate-comments-container">
                <h1 className="moderate-comments-header">Moderate Comments</h1>
                <Comment username="username" commentID={1} comment="example"/>
                <Comment username="username" commentID={2} comment="example"/>
                <Comment username="username" commentID={3} comment="example"/>
                <Comment username="username" commentID={4} comment="example"/>
                <Comment username="username" commentID={5} comment="example"/>
                <Comment username="username" commentID={6} comment="example"/>
                <Comment username="username" commentID={7} comment="example"/>
            </div>
        );
    }

    return (
        <div className="Admin">
            <div className="navbar">
                <NavigationBar {...{userType}}/>
            </div>
            <div className="admin-body"> 
                <h1 className="admin-title">Admin Dashboard</h1>
                <Recipes/>
                <Comments/>
            </div>   
        </div>
    );
}

export default Admin;