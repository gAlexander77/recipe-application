import React, {useState} from 'react';
import { motion } from 'framer-motion';
import { BsXLg } from "react-icons/bs";
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
                    <label className="desc-lable">Description</label>
                    <textarea className="desc-input" type="text" placeholder="Description of your Recipe"></textarea>
                </div>
                <div className="ingr-container">
                    <label className="ingr-label">Ingredients <button onClick={addIngredient}>+</button></label>
                    {ingredients.map((form, index)=>{
                        return (
                            <div className="ingredient" key={index}>
                                <input 
                                className="ingr-input"
                                type="text"
                                placeholder="Ingredient"
                                onChange={(evt) => handleIngredientChange(evt, index)}
                                value = {form.ingredient}
                                />
                                <button onClick={()=>removeIngredient(index)}>-</button>
                            </div>
                        );
                    })}
                </div>
                <div className="inst-container">
                    <label className="inst-lable">Instructions</label>
                    <textarea className="inst-input" type="text" placeholder="Instructions"></textarea>
                </div>
                <button className="post-recipe-form-btn" onClick={submit}>Post Recipe</button>
            </motion.form>
        </div>
    ) : "";   
}

export default AddRecipe;