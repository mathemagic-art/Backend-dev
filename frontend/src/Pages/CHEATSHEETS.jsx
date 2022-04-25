import React from 'react'
import Navbar from '../Layouts/Navbar'
import FunctionsMenu from '../Layouts/FunctionsMenu';

const Cheatsheets = ({toggle, isOpen}) => {
    return ( 
        <div >
        <Navbar toggle={toggle} />
        {isOpen ? <FunctionsMenu /> : ""} 
        <h1 className = "text-center text-white text-5xl" > This is < span > Cheatsheets </span> Page</h1 >
        </div>
    )
};

export default Cheatsheets