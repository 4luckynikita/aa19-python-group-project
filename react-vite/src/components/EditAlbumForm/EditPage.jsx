import { useLocation, useNavigate, useParams } from "react-router-dom";
import EditAlbumForm from "./EditAlbumForm";

import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { fetchCurrentAlbum } from "../../redux/albums";
import "../EditUserForm/EditUserForm.css";

function EditPage() {
  const { id } = useParams();
  const location = useLocation();
  const dispatch = useDispatch();
  const data = location.state;
  const navigate = useNavigate();
  // const [songsArray, setSongsArray] = useState(data.songs);
  const user = useSelector((state) => state.session.user);

  useEffect(() => {
    dispatch(fetchCurrentAlbum(id));
  }, [id, dispatch]);
  const albums = useSelector((state) => state.musicianalbums.currentAlbum[0]);
  //console.log(albums);
  const allAlbums = albums && albums.songs;

  const redirect = (e) => {
    // //console.log('hi')
    e.preventDefault();
    navigate(`/musicians/${user.id}/`);
  };
  //    //console.log(allAlbums)
  return (
    <div className="edit-user-form-container">
      <h1>Edit Your Album</h1>
      <h2>
        Make and save changes on any parts, and then click &quot;Submit&quot; to
        apply them!
      </h2>
      <EditAlbumForm data={data} id={id} songsArray={allAlbums} />
      {/* <DeleteSong songsArray={allAlbums} id={id} /> */}
      <div className="padded-white-line" />
      <button onClick={redirect} className="edit-user-submit-button">
        Submit
      </button>
    </div>
  );
}

export default EditPage;
