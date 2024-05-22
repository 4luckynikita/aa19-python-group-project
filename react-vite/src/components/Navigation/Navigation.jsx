import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <ul className="navbar">
      <li className="navbar-home">
        <NavLink to="/">
          <img
            src="https://res.cloudinary.com/dkxfjbynk/image/upload/v1716365874/beatratespeechbubblenoback_aifesi.png"
            className="navbar-logo"
          />
        </NavLink>
      </li>
      <li className="navbar-right">
        <ProfileButton className={"navbar-profile-button"} />
      </li>
    </ul>
  );
}

export default Navigation;
