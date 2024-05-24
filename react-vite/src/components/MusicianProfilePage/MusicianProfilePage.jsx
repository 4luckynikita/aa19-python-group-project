import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import { fetchCurrentMusician } from "../../redux/musicians";
import { FaFacebook } from "react-icons/fa";
import { FaSoundcloud } from "react-icons/fa";
import { FaSpotify } from "react-icons/fa";
import { FaInstagram } from "react-icons/fa";
import { FaMicrophoneAlt } from "react-icons/fa";
import AlbumComponent from "./album";
import "./MusicianProfilePage.css";

function MusicianProfilePage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const sessionUser = useSelector((state) => state.session.user);
  const { id } = useParams();

  useEffect(() => {
    dispatch(fetchCurrentMusician(id));
  }, [dispatch, id]);

  const musician = useSelector((state) => state.musician.musician);
  // console.log(musician)

  let showButton = false;
  if (musician) {
    if (sessionUser.id == id && sessionUser.is_musician == true) {
      // console.log(id)
      showButton = true;
    }
  }

  return (
    <>
      <h1 className="centred">{musician && musician.name}</h1>
      <div>
        <div className="bio-page_grid">
          <div className="photocard">
            <img
              className="musician-photo"
              src={
                musician && musician.image_url
                  ? `${musician.image_url}`
                  : "/beatratespeechbubble.jpg"
              }
              alt="artist's/band's photo"
            />
            <div>
              <span onClick={() => alert("feature coming soon")}>
                <FaFacebook />
              </span>
              <span onClick={() => alert("feature coming soon")}>
                <FaSoundcloud />
              </span>
              <span onClick={() => alert("feature coming soon")}>
                <FaSpotify />
              </span>
              <span onClick={() => alert("feature coming soon")}>
                <FaInstagram />
              </span>
            </div>
          </div>
          <h2 className="musician-name centred">
            about {musician && musician.name}
          </h2>
          <p className="musician-description centred">
            {musician && musician.description}
          </p>
          <p className="star-rating">
            <FaMicrophoneAlt />
            <FaMicrophoneAlt />
            <FaMicrophoneAlt />
            <FaMicrophoneAlt />
            <FaMicrophoneAlt />
          </p>
          <div className="recommended-music">
            <img
              className="placeholder-image photocard"
              src="https://res.cloudinary.com/dv9oyy79u/image/upload/v1716377358/placeholder_yc2w6u.png"
              alt=""
            />
            <p>check out other music in this genre</p>
          </div>
        </div>
        {showButton && (
          <div className="musician-buttons">
            <button onClick={() => navigate(`/albums/new`)}>add album</button>
            <button onClick={() => navigate(`/musicians/${id}/edit`)}>
              edit profile
            </button>
          </div>
        )}
      </div>
      <hr />
      <AlbumComponent id={id} key={id} />
    </>
  );
}

export default MusicianProfilePage;
