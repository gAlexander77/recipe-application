import React, { useEffect, useRef, useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import axios from 'axios';
import { BsXCircle, BsCaretLeftSquareFill, BsCaretRightSquareFill } from "react-icons/bs";
import { TbTrash } from "react-icons/tb";
import NavigationBar from '../components/NavigationBar';
import '../styles/AccountStyle.css';

import hostname from '../hostname';

function Account() {

    let navigate = useRef(useNavigate());
    const [userType, setUserType] = useState(localStorage.getItem('userType'));
    const [username, setUsername] = useState(localStorage.getItem('username'));

    useEffect(()=>{ 
        setUserType(localStorage.getItem('userType'));
        if (userType !== 'user'){
            navigate.current('/login');
        }
        if (username === 'admin'){
            navigate.current('/admin')
        }
    },[userType])

    const logout = () => {
        localStorage.removeItem('userType');
        localStorage.removeItem('userID');
        localStorage.removeItem('username');
        setUserType(localStorage.getItem('userType')); 
        navigate.current('/login');       
    }

    function AccountInfo() {
        return(
            <div className="account-information">
                <div className="circle">
                    <h1 className="letter">{username[0].toUpperCase()}</h1>
                </div>
                <h1 className="account-username">@{username}</h1>
                <button className="logout-btn" onClick={logout}>Logout</button>
            </div>
        );
    }

    function MyRecipes() {

        const [recipes, setRecipes] = useState([])
        const [isDeleting, setIsDeleting] = useState(false);
        
        useEffect(()=>{
            axios.get(hostname+'/api/recipes').then(res => {
            setRecipes(res.data.data)
            }).catch(error => console.log('API ERROR'));
        }, []);

        /*
        useEffect(()=>{
            axios.get(hostname+'/api/recipes').then(res => {
            setRecipes(res.data)
            }).catch(error => console.log('API ERROR'));
        }, []);
        */

        function AccountRecipeCard({image, name, id}) {

            const deleteRecipeHandler = () => {
                setRecipes(recipes.filter(recipe=>recipe.id !== id));
            }

            const RecipeImage = () => {
                if(isDeleting === true) {
                return(
                    <motion.img src={image} className="box"
                            animate={{
                                rotate: [0,2,0,-2,0],
                            }}
                            transition={{
                                duration: 0.25,
                                repeat: Infinity
                            }}/>
                );}
                else
                return(<img src={image} className="box"/>);
            };

            return (
                <div>
                    <BsXCircle className={`${isDeleting ? "delete-recipe-btn ": "hidden"}`} onClick={deleteRecipeHandler}/>
                    <BsXCircle className={`${isDeleting ? "hidden": "hide-delete-recipe-btn"}`}/>
                    <div className="box-container">
                        <Link to={"/recipe/"+id} state={id} onClick={() => console.log("clicked "+id)}> 
                            <RecipeImage/>
                        </Link>
                        <p className="my-recipe-name">{name}</p>
                    </div>
                </div>
            );
        }
        
        const EmptyRow = () => {
            if(recipes.length === 0)
            return(
                <div className="empty-row">
                <p className="empty-text">You haven't posted any recipes</p>
                </div>
            );
        };

        const myRef = useRef();
        
        const slideLeft = () => {
            myRef.current.scrollLeft += -500;
        };

        const slideRight = () => {
            myRef.current.scrollLeft += 500;
        };
        
        return(
            <div className="my-recipes-container">
                <div className="row-container">
                    <div className="row-header">
                        <h1 className="row-title">My Recipes</h1>
                        <TbTrash className={`${isDeleting ? "trash-icon-active": "trash-icon"}`} onClick={()=> setIsDeleting(!isDeleting)}/>
                    </div>
                    <div className="recipe-row-container">
                        <BsCaretLeftSquareFill className="left-btn" onClick={slideLeft}/>
                        <div className="recipe-row" id="container" ref={myRef}>    
                            {recipes.map((recipe,index) =>{
                                return(
                                    <AccountRecipeCard
                                    key = {index}
                                    id = {recipe.id}
                                    image={hostname+"/"+recipe.image} 
                                    name={recipe.name} 
                                    />
                                );
                            })}
                        <EmptyRow/>    
                        </div>
                        <BsCaretRightSquareFill className="right-btn" onClick={slideRight}/>
                    </div>    
                </div>
            </div>
        );
    }

    function MyComments() {

        const [comments, setComments] = useState([])
        
        
        useEffect(()=>{
            axios.get(hostname+'/comments').then(res => {
            setComments(res.data)
            }).catch(error => console.log('API ERROR'));
        }, []);
        
        
        /*
        useEffect(()=>{
            axios.get(hostname+'/api/comments').then(res => {
            setComments(res.data)
            }).catch(error => console.log('API ERROR'));
        }, []);
        */

        function MyComment({id,username,comment}){

            const removeComment = (evt) => {
                let commentID = evt;    
                setComments(comments.filter(comment=>comment.id !== commentID));
            }

            return(
             <div className="my-comment-container">
                <h1 className="my-comment-title">Commented on {username}'s post:</h1>
                <p className="my-comment">{comment}</p>
                <button className="delete-comment-btn" onClick={()=>removeComment(id)}>Delete Comment</button>
             </div>   
            );
        }

        const NoComments = () => {
            if(comments.length === 0)
            return(
                <div className="no-comments">
                <p className="no-comments-text">You haven't posted any comments</p>
                </div>
            );
        };

        return(
            <div className="my-comments">
                <h1 className="my-comments-title">My Comments</h1>
                {comments.map((comment, index) =>{
                    return(
                        <MyComment
                        key={index}
                        id={comment.id}
                        username={comment.username}
                        comment={comment.comment}
                        />
                    );
                })}
                <NoComments/>
            </div>
        );
    }

    function MyRatings(){
        
        const [ratings, setRatings] = useState([])
    
        useEffect(()=>{
            axios.get(hostname+'/ratings').then(res => {
            setRatings(res.data)
            }).catch(error => console.log('API ERROR'));
        }, []);

        function MyRating({id,recipe,username,rating}){

            const removeRating = (evt) => {
                let ratingID = evt;    
                setRatings(ratings.filter(rating=>rating.id !== ratingID));
            }

            return(
             <div className="my-rating-container">
                <p className="my-rating-text">You rated {username}'s {recipe} recipe {rating} stars</p>
                <button className="delete-rating-btn" onClick={()=>removeRating(id)}>Delete Rating</button>
             </div>   
            );
        }

        const NoRatings = () => {
            if(ratings.length === 0)
            return(
                <div className="no-comments">
                <p className="no-comments-text">You haven't rated any recipes</p>
                </div>
            );
        };

        return(
            <div className="my-ratings">
                <h1 className="my-comments-title">My Ratings</h1>
                {ratings.map((rating, index) =>{
                    return(
                        <MyRating
                        key={index}
                        id={rating.id}
                        recipe={rating.recipe_name}
                        username={rating.username}
                        rating={rating.rating}
                        />
                    );
                })}
                <NoRatings/>
            </div>
        );
    }

    return(
        <div className="Account">
            <div className="navbar">
                <NavigationBar {...{userType}}/>
            </div>
            <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            >
                <AccountInfo/>
                <MyRecipes/>
                <MyComments/>
                <MyRatings/>
            </motion.div>
        </div>
    );
}

export default Account;