import React, {useEffect, useRef, useState} from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBar from '../components/NavigationBar';
import Feed from '../components/Feed';
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
        <div className="Home">
            <NavigationBar {...{userType}}/>
            <Feed className="Feed"/>
        </div>
    );
}

export default Home;