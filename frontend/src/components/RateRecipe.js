import React, {useState}from 'react';
import { motion } from 'framer-motion';
import { BsXLg } from "react-icons/bs";
import { ImStarFull} from "react-icons/im";
import '../styles/components/RateRecipeStyle.css';

function RateRecipe(props){
    const [rating, setRating] = useState(0);
    const [tempRating, setTempRating] = useState(0);

    const rateRecipe = () => {
        console.log(rating);
        props.setTrigger(false);
    }

    const setRatingHandler = (evt) => {
        setRating(evt)
        setTempRating(evt)
        console.log(rating);
        console.log(tempRating);
    }

    function MouseOver(event,star) {
        //event.target.style.color = 'red';
        event.target.style.transform = 'scale(1)';
        console.log(star);
        setTempRating(star);
    }
    function MouseOut(event){
        event.target.style.color="";
        event.target.style.transform = 'scale(1)';
        setTempRating(rating)
    }

    return(props.trigger)?(
        <div className="rate-recipe-popup">
            <motion.div className="rate-recipe-inner"
            initial={{ opacity: 0, y: "300px" }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0 }}
            transition={{ opacity: 0.2, y: 0.3 }}
            >
                <BsXLg className="exit-rate-recipe" onClick={() => props.setTrigger(false)}/>
                <h1>What do you rate this recipe?</h1>
                <div>
                    <ImStarFull className={1 <= tempRating ? "star-on r-star":"star-off r-star"} 
                    onMouseOver={(event)=>MouseOver(event,1)} onMouseOut={MouseOut}
                    onClick={()=>setRatingHandler(1)}
                    />
                    <ImStarFull className={2 <= tempRating ? "star-on r-star":"star-off r-star"} 
                    onMouseOver={(event)=>MouseOver(event,2)} onMouseOut={MouseOut}
                    onClick={()=>setRatingHandler(2)}
                    />
                    <ImStarFull className={3 <= tempRating ? "star-on r-star":"star-off r-star"} 
                    onMouseOver={(event)=>MouseOver(event,3)} onMouseOut={MouseOut}
                    onClick={()=>setRatingHandler(3)}
                    />
                    <ImStarFull className={4 <= tempRating ? "star-on r-star":"star-off r-star"} 
                    onMouseOver={(event)=>MouseOver(event,4)} onMouseOut={MouseOut}
                    onClick={()=>setRatingHandler(4)}
                    />
                    <ImStarFull className={5 <= tempRating ? "star-on r-star":"star-off r-star"} 
                    onMouseOver={(event)=>MouseOver(event,5)} onMouseOut={MouseOut}
                    onClick={()=>setRatingHandler(5)}
                    />
                </div>
                <p>{rating}/5 Stars</p>
                <button className="submit-rating-btn" onClick={rateRecipe}>Submit Rating</button>
            </motion.div>
        </div>
    ):"";
}

export default RateRecipe;