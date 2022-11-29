import React, {useState} from 'react';
import NavigationBar from '../components/NavigationBar';
import '../styles/Error404Style.css';

function Error404() {
    
    const [userType, setUserType] = useState(localStorage.getItem('userType'));

    return(
        <div className="Error404">
            <NavigationBar {...{userType}}/>
            <div className="error404-message-container">
                <h1 className="error404-title">404</h1>
                <p className="error404-message">This page does not exist</p>
            </div>
        </div>
    );
}

export default Error404;