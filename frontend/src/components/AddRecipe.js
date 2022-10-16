import React, {useState} from 'react';
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
            <form className="popup-inner" onSubmit={submit}>
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
            </form>
        </div>
    ) : "";   
}

export default AddRecipe;