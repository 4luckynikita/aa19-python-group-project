import { NavLink, useLocation } from "react-router-dom";
import { useState } from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchMusicians } from "../../redux/musicians";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  const [isOpen, setIsOpen] = useState(false);
  const dispatch = useDispatch();
  const location = useLocation();
  const showProfileButton = location.pathname !== "/landing";

  useEffect(() => {
    dispatch(fetchMusicians());
  }, [dispatch]);

  let artists = useSelector((state) => state.musician.musicians);

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  console.log(artists);

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
        <div className="dropdown">
          <button onClick={toggleDropdown} className="dropdown-button">
            Musicians
            <img
              src="https://res.cloudinary.com/dkxfjbynk/image/upload/v1716497519/32ee20be-0055-4208-aa59-ad09ccd5d540.png"
              className="musicians-button-arrow"
            />
          </button>
          {isOpen && (
            <ul className="dropdown-menu">
              {artists &&
                artists?.map((artist) => (
                  <li key={artist.id} className="artist-dropdown-li">
                    <NavLink
                      to={`/musicians/${artist?.id}`}
                      onClick={toggleDropdown}
                    >
                      {artist?.name}
                    </NavLink>
                  </li>
                ))}
            </ul>
          )}
        </div>

        {showProfileButton && (
          <li className="navbar-right">
            <ProfileButton className={"navbar-profile-button"} />
          </li>
        )}
      </li>
    </ul>
  );
}

export default Navigation;
