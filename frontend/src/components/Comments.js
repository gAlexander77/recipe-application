import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/components/CommentsStyle.css';
import { useLocation} from "react-router-dom";
import hostname from '../hostname';

function Comments(){
    const [comments, setComments] = useState([]);
    const [comment, setComment] = useState();
    const location = useLocation();
    const recipeID = location.state;

    useEffect(()=>{
        axios.get(hostname+'/api/comments/'+recipeID).then(res => {
        setComments(res.data.data)    
        console.log(res.data)
        }).catch(error => console.log("error"));
      }, [recipeID]);

    const inputHandler = (evt) => {
        let num = evt.target.value
        setComment(num);
    }

    const postComment = () => {
        let myComment = {
            username: "TestUsername",
            comment: comment
        }
    }


    function Comment({username,comment}){
        return(
            <div className="comment-container">
                <h1 className="comment-username">{username}</h1>
                <p className="comment-contents"> {comment}</p>
            </div>
        );
    }

    return(
        <div className="Comments">
            <h1 className="comments-header">Comments</h1>
            <div className="comment-input-container">
                <input className="comment-input" placeholder="Write a comment..." onChange={inputHandler}/>
                <button disabled={!comment} className="comment-btn">Comment</button>
            </div>
            {comments.map((comment, index) =>{
                return(
                    <Comment
                    key={index}
                    username={comment.username}
                    comment={comment.comment}
                    />
                );
            })}
        </div>
    );
}

export default Comments;