import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import { fetchCurrentMusician } from "../../redux/musicians";
import AlbumComponent from "./album";
import "./MusicianProfilePage.css";
import "../UserProfilePage/UserProfilePage.css";

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
    <div className="user-everything-container">
      <h1 className="user-profile-username">Musician Profile</h1>

      <div className="user-profile-container">
        <div className="user-profile-container-left">
          <img
            className="user-profile-picture"
            src={
              musician && musician.image_url
                ? `${musician.image_url}`
                : "/beatratespeechbubble.jpg"
            }
            alt="artist's/band's photo"
          />
          {/* <div className="user-profile-socials-container">
            <a href="https://www.facebook.com" target="_blank" rel="noreferrer">
              <img
                src="https://res.cloudinary.com/dkxfjbynk/image/upload/v1716589080/085acd0d-df7a-4317-8df5-6941a1106f09.png"
                className="user-profile-social-logo"
              />
            </a>
            <a
              href="https://www.soundcloud.com"
              target="_blank"
              rel="noreferrer"
            >
              <img
                src="https://res.cloudinary.com/dkxfjbynk/image/upload/v1716589543/6c2fbc03-c0d4-44f1-91b7-2a347958480c.png"
                className="user-profile-social-logo"
              />
            </a>
            <a href="https://www.spotify.com" target="_blank" rel="noreferrer">
              <img
                src="https://res.cloudinary.com/dkxfjbynk/image/upload/v1716589564/d599756b-4264-4136-a217-ac49cade5466.png"
                className="user-profile-social-logo"
              />
            </a>
            <a
              href="https://www.instagram.com"
              target="_blank"
              rel="noreferrer"
            >
              <img
                src="https://res.cloudinary.com/dkxfjbynk/image/upload/v1716589605/eac947d2-b379-4f79-a80a-62b9955114f5.png"
                className="user-profile-social-logo"
              />
            </a>
          </div> */}
        </div>
        <div className="user-profile-container-right">
          <div className="user-profile-container-right-upper">
            <h2 className="user-profile-firstandlast">
              {musician && musician.name}
            </h2>

            <p className="user-profile-joindate">
              Joined on {new Date(musician?.created_at).toLocaleDateString()}
            </p>
          </div>
          <p className="user-profile-description">
            {musician && musician.description}
          </p>
        </div>
      </div>
      {showButton && (
        <div className="user-profile-edit-container2">
          <button
            onClick={() => navigate(`/albums/new`)}
            className="user-edit-profile-button"
          >
            add album
          </button>
          <button
            onClick={() => navigate(`/musicians/${id}/edit`)}
            className="user-edit-profile-button"
          >
            edit profile
          </button>
        </div>
      )}
      <AlbumComponent id={id} key={id} />
    </div>
  );
}

export default MusicianProfilePage;
