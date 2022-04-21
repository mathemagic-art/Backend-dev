import NavLink from "../Components/NavLink";
import Darkmode from "darkmode-js";
import { ReactComponent as Logo } from "../Files/svgs/Logo.svg";
import { ReactComponent as Bucket } from "../Files/svgs/bucket.svg";
import { ReactComponent as Search } from "../Files/svgs/search.svg";
import { Link } from "react-router-dom";
const Navbar = ({ toggle }) => {
  // Darkmode Setup
  const options = {
    top: "unset",
    bottom: "32px", // default: '32px'
    right: "32px", // default: '32px'
    left: "unset", // default: 'unset'
    time: "0.5s", // default: '0.3s'
    mixColor: "#fff", // default: '#fff'
    backgroundColor: "#100f2c",
    light: "#fff", // default: '#fff'
    buttonColorDark: "#fff", // default: '#100f2c'
    buttonColorLight: "#000", // default: '#fff'
    saveInCookies: true, // default: true,
    label: "💡", // default: ''
    autoMatchOsTheme: false, // default: true
  };
  const darkmode = new Darkmode(options);

  return (
    <div className="flex flex-row items-center text-white text-2xl">
      <div className="mx-10">
        <button onClick={toggle}>
          <Bucket className="fill-white" />
        </button>
      </div>
      <div className="flex flex-row p-10 space-x-10 items-center m-auto gap-20">
        <NavLink text={"TEST YOURSELF"} />
        <NavLink text={"CHEATSHEETS"} />
        <Link to="/">
          <h1 className="text-4xl font-semibold text-center flex flex-row">
            <Logo className="mr-3" />
            MATHEMAGICS
          </h1>
        </Link>
        <NavLink text={"LEARNING MATERIALS"} />
        <NavLink text={"ABOUT"} />
        <Search />
        <span>{darkmode.showWidget()}</span>
      </div>
    </div>
  );
};

export default Navbar;
