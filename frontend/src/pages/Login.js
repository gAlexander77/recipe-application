import React, {useState} from 'react';
import '../styles/LoginStyle.css'
import {Link } from "react-router-dom";
import { FaBeer } from 'react-icons/fa';

function Login () {

    const [hasAccount,setHasAccount] = useState(null)

    function SignUp() {
        return (
            <form>
                <label>Username</label>
                <input className="Username" type="text"></input>
                <label>Password</label>
                <input className="Password" type="password"></input>
                <label>Verify Password</label>
                <input className="Verify Password" type="password"></input>
                <button className="btn btn-primary">Create Account</button>
            </form>
        );
    }

    function SignIn() {
        return (
            <form className="need-validation">
                <div className="form-group">  
                    <label className="form-label">Username</label>
                    <input className="form-control" type="text"></input>
                    <div className="invalid-feedback">
                        Please enter your username
                    </div>
                </div>
                <div className="form-group">
                    <label className="form-label">Password</label>
                    <input className="form-control" type="password" placeholder="Password"></input>
                    <button className="btn btn-primary w-100">Login</button>
                    <div className="invalid-feedback">
                        Please enter your username
                    </div>
                </div>
            </form>
        );
    }

    function LoginOptions() {
        return (
            <div className="login-options">
                <button className="btn-3 btn-size btn-padding" onClick={() => setHasAccount(true)}>Login</button>
                <button className="button-59 btn-size btn-padding create-account-button" onClick={() => setHasAccount(false)}>Create Account</button>    
                <Link to="/">
                <a className="guest" >Continue as a guest</a>
                </Link>
            </div>
        );
    }

    if(hasAccount === null){    
        return(
            <div className="site-body center-items">
                <div> 
                    <h1 className="text-center"></h1>
                    <div className="box-size">  
                        <LoginOptions/>
                    </div> 
                </div>   
            </div>
        );}
    else if(hasAccount === true){
        return(
            <div className="site-body center-items">
                <div>
                    <h1 className="text-center">Title</h1>
                    <div className="box-size"> 
                        <SignIn/>  
                    </div>
                </div>
            </div>
        );
    }
    else if(hasAccount === false){
        return(
            <div className="site-body center-items">
                <div>
                    <h1 className="text-center">Recipes</h1>
                    <div className="box-size"> 
                        <SignUp/>
                    </div>  
                </div>
            </div>
        );
    }
 }

 export default Login;