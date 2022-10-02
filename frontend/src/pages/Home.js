import React, {useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBar from '../components/NavigationBar';
import '../styles/HomeStyle.css'

function Home(){
    let navigate = useNavigate();
    let userType = localStorage.getItem('userType');

    useEffect(()=>{ 
        userType = localStorage.getItem('userType')
        if (userType ===null){
            navigate('/login');
        }
    },[])

    return (
        <div className="site-body">
            <NavigationBar {...{userType}}/>
            <h1>Header</h1>
            <h2>Feed</h2>
        </div>
    );
}

export default Home;