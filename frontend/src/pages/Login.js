import React, {useState} from 'react';
import '../styles/LoginStyle.css'

function Login () {

    const [hasAccount,setHasAccount] = useState(null)

    function SignUp() {
        return (
            <form>
                <h1>Username</h1>
                <input className="Username" type="text"></input>
                <h1>Password</h1>
                <input className="Password" type="password"></input>
                <h1>Verify Password</h1>
                <input className="Verify Password" type="password"></input>
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
                    <p className="text-center" id="guest" >Continue as a guest</p>
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
                <h1>Recipes</h1>
                <SignUp/>  
            </div>
        );
    }


 }

 export default Login;