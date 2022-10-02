import React, {useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/HomeStyle.css'

function Home(){
    let navigate = useNavigate();

    useEffect(()=>{ 
        let userType = localStorage.getItem('userType')
        if (userType ===null){
            navigate('/login');
        }
    },[])

    return (
        <div className="site-body">
            <h1>Header</h1>
            <h2>Feed</h2>
        </div>
    );
}

export default Home;