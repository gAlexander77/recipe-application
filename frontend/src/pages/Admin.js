import React,{ useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from 'axios';
import NavigationBar from '../components/NavigationBar';
import '../styles/AdminStyle.css';
import hostname from '../hostname';

function Admin(){

    const [userType, setUserType] = useState(localStorage.getItem('userType'));
    const [recipes, setRecipes] = useState([]);

    const [notificationMessage, setNotificationMessage] = useState('');
    const [notification, setNotification] = useState(false);

    useEffect(()=>{
        axios.get(hostname+'/api/recipes/').then(res => {
        console.log(res.data.data)
        setRecipes(res.data.data)
        }).catch(error => alert('API ERROR'));
      }, []);

    function Notification(){
        if(notification===true){
            return(
                <div className="notification-popup">  
                    <div className="notification-container">
                        <p className="notification-message">{notificationMessage}</p>
                    </div>
                </div>  
            );
        }
        else
        {
            return('');
        }
    }

    function Recipes(){
        
        function Recipe({recipe, id}){

            const deleteRecipeHandler = () => {
                setRecipes(recipes.filter(recipe=>recipe.id !== id));
                setNotificationMessage(recipe+" was deleted");
                setNotification(true);
                setTimeout(() =>{setNotification(false);},2000)
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
                {recipes.map((recipe, index) =>{
                    return(
                        <Recipe
                        key = {index}
                        recipe={recipe.name} 
                        id = {recipe.id}
                        />
                    );
                })}
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
                <Notification/>
                <Recipes/>
                <Comments/>
            </div>
             
        </div>
    );
}

export default Admin;