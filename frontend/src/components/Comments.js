import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/components/CommentsStyle.css';

import hostname from '../hostname';

function Comments(){

    const [comments, setComments] = useState([]);
    const [comment, setComment] = useState();

    useEffect(()=>{
        axios.get(hostname+'/api/comments/').then(res => {
        	if(!res.data.ok)
				alert(res.data.data);
			alert(res.data.data)
			//setComments(res.data.data)
        }).catch(error => alert('API ERROR'));
      }, []);

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
