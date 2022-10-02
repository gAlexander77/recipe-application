import React, {useEffect, useRef, useState} from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBar from '../components/NavigationBar';
import '../styles/HomeStyle.css'

function Home(){
    let navigate = useRef(useNavigate());
    const [userType, setUserType] = useState(localStorage.getItem('userType'));

    useEffect(()=>{ 
        setUserType(localStorage.getItem('userType'));
        console.log(userType)
        if (userType === null){
            navigate.current('/login');
        }
    },[userType]);

    return (
        <div className="site-body">
            <NavigationBar {...{userType}}/>
            <h1>Header</h1>
            <h2>Feed</h2>
        </div>
    );
}

export default Home;