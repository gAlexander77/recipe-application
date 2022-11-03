import React, { useState } from 'react';

import hostname from '../hostname';

function Comments(){

    const [comments, setComments] = useState();

    useEffect(()=>{
        axios.get(hostname+'/comments').then(res => {
        setComments(res.data)
        }).catch(error => alert('API ERROR'));
      }, []);

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