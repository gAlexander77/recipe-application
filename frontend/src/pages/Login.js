import React, {useState} from 'react';
import '../styles/LoginStyle.css'
import {Link } from "react-router-dom";
import { FaUser,FaLock } from "react-icons/fa"
import { BsXLg } from "react-icons/bs";

function Login () {

    const [hasAccount,setHasAccount] = useState(null)

    function SignUp() {
        return (
            <form className="box-size center">
                <BsXLg className="form-exit" onClick={()=>setHasAccount(null)}/>
                <div className="content-box center">
                    <div className="">
                        <FaUser/>
                        <input className="Username" placeholder="Username" type="text"></input>
                    </div>
                    <div>
                    <FaLock/>
                        <input className="Password" placeholder="Password" type="password"></input>
                        </div>
                    <div>
                        <FaLock/>
                        <input className="Verify Password" placeholder="Verify Password" type="password"></input>
                    </div>
                    <button className="btn btn-primary">Create Account</button>
                </div>
            </form>
        );
    }

    function SignIn() {
        return (
            <form className="box-size center">
                <BsXLg className="form-exit" onClick={()=>setHasAccount(null)}/>
                <div className="content-box center">
                    <div className="">  
                        <FaUser/>
                        <input className="" type="text" placeholder="Username"></input>

                    </div>
                    <div className="">
                        <FaLock/>
                        <input className="" type="password" placeholder="Password"></input>
                    </div>
                        <button className="">Login</button>
                </div>
            </form>
        );
    }

    function LoginOptions() {
        return (
            <div className="box-size stack">
                <button className="btn-login-options" onClick={() => setHasAccount(true)}>Login</button>
                <button className="btn-login-options" onClick={() => setHasAccount(false)}>Create Account</button>    
                <Link to="/">
                <a className="guest" >Continue as a guest</a>
                </Link>
            </div>
        );
    }

    if(hasAccount === null){    
        return(
            <div className="Login center">
                <LoginOptions/> 
            </div>
        );
    }
    else if(hasAccount === true){
        return(
            <div className="Login center">
                <SignIn/>  
            </div>
        );
    }
    else if(hasAccount === false){
        return(
            <div className="Login center">
                <div>
                    <SignUp/>
                </div>
            </div>
        );
    }
 }

 export default Login;