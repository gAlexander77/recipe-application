import React, {useState, useEffect} from 'react';
import '../styles/LoginStyle.css'
import { Link } from "react-router-dom";
import { FaUser,FaLock } from "react-icons/fa"
import { BsXLg } from "react-icons/bs";

function Login () {

    const guestHandler = () => {
        localStorage.setItem('userType', 'guest')
    }

    const [hasAccount,setHasAccount] = useState(null)

    function SignUp() {

        const [data, setData] = useState({
            username: "",
            password: "",
            verifyPassword: ""
        });
        
        const [passwordVerified, setPasswordVerified] = useState(false);
        useEffect(()=>{
            if(data.password==="" || data.verifyPassword==="")
                setPasswordVerified(null);
            else if(data.password===data.verifyPassword)
                setPasswordVerified(true);
            else if(data.password!==data.verifyPassword)
                setPasswordVerified(false);
        },[data])

        const changeValueHandler = (evt) => {
            const newData={...data};
            newData[evt.target.id] = evt.target.value;
            setData(newData);
        }

        function DoPasswordsMatch() {
            if(passwordVerified===true)
                return(
                    <div>Passwords Match</div>
                );
            else if(passwordVerified===false)
                return(
                    <div>Passwords Do Not Match</div>
                );
        }

        return (
            <form className="box-size center">
                <BsXLg className="form-exit" onClick={()=>setHasAccount(null)}/>
                <div className="content-box center">
                    <div className="input-row">
                        <FaUser className="input-logo"/>
                        <input 
                            className="inpt Username" 
                            placeholder="Username" 
                            type="text"
                            id="username" 
                            value={data.username}
                            onChange={(evt)=>changeValueHandler(evt)}
                            />
                    </div>
                    <div className="input-row">
                        <FaLock className="input-logo"/>
                        <input 
                            className="inpt Password" 
                            placeholder="Password" 
                            type="password"
                            id="password" 
                            value={data.password}
                            onChange={(evt)=>changeValueHandler(evt)}
                            />
                        </div>
                    <div className="input-row">
                        <FaLock className="input-logo"/>
                        <input 
                            className="inpt verify-password" 
                            placeholder="Verify Password" 
                            type="password"
                            id="verifyPassword" 
                            value={data.verifyPassword}
                            onChange={(evt)=>changeValueHandler(evt)}
                            />
                    </div>
                    <DoPasswordsMatch/>
                    <button className="btn-hover btn">Create Account</button>
                </div>
            </form>
        );
    }

    function SignIn() {

        const [data, setData] = useState({
            username: "",
            password: ""
        });

        const changeValueHandler = (evt) => {
            const newData={...data};
            newData[evt.target.id] = evt.target.value;
            setData(newData);
        }

        return (
            <form className="box-size center">
                <BsXLg className="form-exit" onClick={()=>setHasAccount(null)}/>
                <div className="content-box center">
                    <div className="input-row">  
                        <FaUser className="input-logo"/>
                        <input 
                            className="inpt" 
                            type="text" 
                            placeholder="Username" 
                            id="username" 
                            value={data.username}
                            onChange={(evt)=>changeValueHandler(evt)}
                            />
                    </div>
                    <div className="input-row">
                        <FaLock className="input-logo"/>
                        <input 
                            className="inpt" 
                            type="password" 
                            placeholder="Password" 
                            id="password" 
                            value={data.password}
                            onChange={(evt)=>changeValueHandler(evt)}
                            />
                    </div>
                        <button className="btn-hover btn">Login</button>
                </div>
            </form>
        );
    }

    function LoginOptions() {
        return (
            <div className="box-size stack">
                <button className="btn-hover btn" onClick={() => setHasAccount(true)}>Login</button>
                <button className="btn-hover btn" onClick={() => setHasAccount(false)}>Create Account</button>    
                <Link to="/" onClick={guestHandler}>
                    Continue as a guest
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