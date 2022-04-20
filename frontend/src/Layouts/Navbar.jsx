import React from "react";
import NavLink from "../Components/NavLink";
import Darkmode from "darkmode-js";
import {ReactComponent as Logo} from "../Files/svgs/Logo.svg"
import {ReactComponent as Bucket} from "../Files/svgs/bucket.svg"
import {ReactComponent as Search} from "../Files/svgs/search.svg"

const Navbar = () => {
  const options = {
    top: 'unset',
    bottom: '32px', // default: '32px'
    right: '32px', // default: '32px'
    left: 'unset', // default: 'unset'
    time: '0.5s', // default: '0.3s'
    mixColor: 'unset', // default: '#fff'
    backgroundColor: '#100f2c', 
    light: '#fff', // default: '#fff'
    buttonColorDark: '#fff',  // default: '#100f2c'
    buttonColorLight: '#000', // default: '#fff'
    saveInCookies: true, // default: true,
    label: '', // default: ''
    autoMatchOsTheme: false // default: true
  }
  const darkmode = new Darkmode(options)
  
  return (
  <div className="flex flex-row items-center">
    <div className="mx-10">
      <button><Bucket className="fill-white"/></button>
    </div>
    <div className="flex flex-row p-10 space-x-10 items-center m-auto gap-20">
      <NavLink text={"TEST"} />
      <NavLink text={"CHEATSHEETS"} />
      <h1 className="text-4xl font-semibold text-center flex flex-row"> <Logo className="mr-3"/>MATHEMAGICS</h1>
      <NavLink text={"LEARNIGN MATERIALS"} />
      <NavLink text={"ABOUT"} />   
      <Search />

      <span>{darkmode.showWidget()}</span>
    </div>


  </div>
  );
};

export default Navbar;
