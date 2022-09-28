import React, {useState} from 'react';

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
            <form>
                <h1>Username</h1>
                <input className="Username" type="text"></input>
                <h1>Password</h1>
                <input className="Password" type="password"></input>
            </form>
        );
    }

    function LoginOptions() {
        return (
            <div> 
                <button onClick={() => setHasAccount(true)}>Login</button>
                <button onClick={() => setHasAccount(false)}>Create Account</button>
                <p>Continue as a guest</p>
            </div>
        );
    }

    if(hasAccount === null){    
        return(
            <div>
                <h1>Recipes</h1>
                <LoginOptions/>
            </div>
        );}
    else if(hasAccount === true){
        return(
            <div>
                <h1>Recipes</h1>
                <SignIn/>  
            </div>
        );
    }
    else if(hasAccount === false){
        return(
            <div>
                <h1>Recipes</h1>
                <SignUp/>  
            </div>
        );
    }


 }

 export default Login;