import React, {useState} from 'react';
import { motion } from 'framer-motion';
import { BsXLg } from "react-icons/bs";
import { FaPaperPlane } from "react-icons/fa";
import '../styles/components/AddRecipeStyle.css'; 

function AddRecipe(props){
    const [ingredients, setIngredients] = useState(['']);
    
    const handleIngredientChange = (evt, index) => {
        let data = [...ingredients];
        data[index] = evt.target.value;
        setIngredients(data);
    }

    const addIngredient = () => {
        let newIngredient = '';
        setIngredients([...ingredients, newIngredient]);
    }

    const removeIngredient = (index) => {
        let deleteIngredient = [...ingredients];
        deleteIngredient.splice(index, 1);
        if(ingredients.length !== 1)
            setIngredients(deleteIngredient);
    }

    const submit = (evt) => {
        evt.preventDefault();
        console.log(ingredients);
    }

    return(props.trigger)?(
        <div className="popup">
            <motion.form className="popup-inner" onSubmit={submit}
            initial={{ opacity: 0, y: "300px" }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0 }}
            transition={{ opacity: 0.2, y: 0.3 }}
            >
                <BsXLg className="exit" onClick={() => props.setTrigger(false)}/>
                <div className="name-container">  
                    <label className="name-label">Name of Recipe</label>
                    <input className="name-input" type="text" placeholder="Name of recipe"></input>
                </div>  
                <div className="desc-container">
                    <label className="desc-label">Description</label>
                    <textarea className="desc-input" type="text" placeholder="Description of your Recipe"></textarea>
                </div>
                <div className="ingr-container">
                    <div className="ingr-label-container">
                    <label>Ingredients</label>
                    <button className="add-btn" onClick={addIngredient}>+</button>
                    </div>
                    {ingredients.map((form, index)=>{
                        if(index === 0){
                            return(
                                <div className="ingredient" key={index}>
                                <input 
                                className="ingr-input"
                                type="text"
                                placeholder="Ingredient"
                                onChange={(evt) => handleIngredientChange(evt, index)}
                                value = {form.ingredient}
                                />
                                <button className="remove-btn" onClick={()=>removeIngredient(index)}>-</button>
                            </div>
                            );
                        } 
                        else{
                            return (
                                <motion.div className="ingredient" key={index}
                                    initial = {{x:-200}}
                                    animate={{x:0}}
                                    >
                                    <input 
                                    className="ingr-input"
                                    type="text"
                                    placeholder="Ingredient"
                                    onChange={(evt) => handleIngredientChange(evt, index)}
                                    value = {form.ingredient}
                                    />
                                    <button className="remove-btn" onClick={()=>removeIngredient(index)}>-</button>
                                </motion.div>
                            );
                        }
                    })}
                </div>
                <div className="inst-container">
                    <label className="inst-label">Instructions</label>
                    <textarea className="inst-input" type="text" placeholder="Instructions"></textarea>
                </div>
                <button className="post-recipe-form-btn" onClick={submit}>Post Recipe<FaPaperPlane className="plane-icon"/></button>
            </motion.form>
        </div>
    ) : "";   
}

export default AddRecipe;