import React, {useState} from 'react';
import axios from 'axios';
import { motion } from 'framer-motion';
import { BsXLg } from "react-icons/bs";
import { FaPaperPlane } from "react-icons/fa";
import '../styles/components/AddRecipeStyle.css'; 
import hostname from '../hostname';

function AddRecipe(props){
    const [recipeName, setRecipeName] = useState('');
    const [image, setImage] = useState(null);
    const [description, setDescription] = useState('');
    const [instructions, setInstructions] = useState('');
    const [ingredients, setIngredients] = useState(['']);

    const handleRecipeNameChange = (evt) => {
        setRecipeName(evt.target.value);
        console.log(recipeName);
    }

    const [imagePreview, setImagePreview] = useState(null);
    const handleImageChange = (evt) => {
        setImage(evt.target.files[0]);
        setImagePreview(URL.createObjectURL(evt.target.files[0]));
        console.log(evt.target.files[0]);
    } 

    const handleDescriptionChange = (evt) => {
        setDescription(evt.target.value);
    }

    const handleInstructionsChange = (evt) => {
        setInstructions(evt.target.value);
    }

    const handleIngredientChange = (evt, index) => {
        let data = [...ingredients];
        data[index] = evt.target.value;
        setIngredients(data);
    }

    const addIngredient = (evt) => {
        evt.preventDefault();
        let newIngredient = '';
        setIngredients([...ingredients, newIngredient]);
    }

    const removeIngredient = (index) => {
        let deleteIngredient = [...ingredients];
        deleteIngredient.splice(index, 1);
        if(ingredients.length !== 1){
            setIngredients(deleteIngredient);
        }
    }

    const formData = {  
        name: recipeName,
        ingredients: ingredients,
        description: description,
        instructions: instructions,
        image: image
    };

    const postRecipe = () => {
        const request = hostname+'/api/recipes/create'
        axios.post(request, formData)
    }
    const [cannotPost, setCannotPost] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');
    const [posted, setPosted] = useState(false);
    const [stop, setStop] = useState(false);

    const submit = (evt) => {
        evt.preventDefault();
        setCannotPost(false);
        setStop(false)
        setPosted(false);
        console.log(formData);
        if(formData.name === '' || formData.ingredients === '' || formData.description === '' || formData.instructions === '' || formData.image === null)
        {
            setStop(true);
            setErrorMessage('Please fill out all inputs in the form to post your recipe')
            setCannotPost(true);
            setTimeout(() =>{setCannotPost(false);},5000)
            return;
        }
        for(var i = 0; i < formData.instructions.length; i++) {
            if(formData.ingredients[i] === '')
            {
                setStop(true);
                setErrorMessage('Please fill out all ingredient inputs or remove any unneaded inputs')
                setCannotPost(true);
                setTimeout(() =>{setCannotPost(false);},5000)
                return;
            }
        }
        if ( stop === false)
        {
            postRecipe();
            setPosted(true);
            setTimeout(() =>{setPosted(false);},5000)
            setTimeout(()=>{props.setTrigger(false);},5000)
        }
    }

    function PostError() {
        if(cannotPost===true)
        {
            return(
                <div className="post-error-container">
                    <p className="post-error-message">{errorMessage}</p>
                </div>
            );
        }
        else
            return('');
    }

    function Posted() {
        if(posted===true)
        {
            return(
                <div className="post-error-container">
                    <p className="post-error-message">Your post has been posted!</p>
                </div>
            );
        }
        else
            return('');
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
                    <input 
                        className="name-input" 
                        type="text" 
                        placeholder="Name of recipe"
                        value={recipeName}
                        onChange={handleRecipeNameChange}
                        />
                </div>
                <div className="image-input-container">
                    <label className="image-label">Upload Recipe Image</label>
                    <img src={imagePreview} className="image-preview"/>
                    <input 
                        className="image-input" 
                        type="file"
                        accept="image/png, image/jpeg"
                        onChange={handleImageChange}
                        />
                </div>  
                <div className="desc-container">
                    <label className="desc-label">Description</label>
                    <textarea 
                        className="desc-input" 
                        type="text" 
                        placeholder="Description of your Recipe"
                        value={description}
                        onChange={handleDescriptionChange}
                        />
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
                    <textarea 
                        className="inst-input" 
                        type="text" 
                        placeholder="Instructions"
                        value={instructions}
                        onChange={handleInstructionsChange}
                        />
                </div>
                <button className="post-recipe-form-btn" onClick={submit}>Post Recipe<FaPaperPlane className="plane-icon"/></button>
                <PostError/>
                <Posted/>
            </motion.form>
        </div>
    ) : "";   
}

export default AddRecipe;