import React, {useState} from 'react';
import '../styles/LoginStyle.css'
import {Link } from "react-router-dom";

function Login () {

    const [hasAccount,setHasAccount] = useState(null)

    function SignUp() {
        return (
            <form className="need-validation">
                <div className="form-group">
                    <label>Username</label>
                    <input className="Username" type="text"></input>
                </div>
                <div className="form-group">
                    <label>Password</label>
                    <input className="Password" type="password"></input>
                    <label>Verify Password</label>
                    <input className="Verify Password" type="password"></input>
                    <button className="btn btn-primary">Create Account</button>
                </div>      
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
            <div className="container">
                <div className="row p-2">
                    <div className="col" align="center">   
                        <button className="btn btn-primary" id="login-button" onClick={() => setHasAccount(true)}>Login</button>
                    </div> 
                </div>
                <div className="row p-2">
                    <div className="col-md-12" align="center">
                        <button className="btn btn-primary" id="create-account-button" onClick={() => setHasAccount(false)}>Create Account</button>
                    </div>
                </div> 
                <div className="row">
                    <div className="col-md-12" align="center">      
                        <Link to="/">
                        <button className="btn btn-primary"id="guest" >Continue as a guest</button>
                        </Link>
                    </div>  
                </div>
            </div>
        );
    }

    if(hasAccount === null){    
        return(
            <div className="site-body center-items">
                <div> 
                    <h1 className="text-center">Title</h1>
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