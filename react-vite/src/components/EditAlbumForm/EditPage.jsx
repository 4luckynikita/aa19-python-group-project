import { useLocation, useNavigate, useParams } from "react-router-dom";
import EditAlbumForm from "./EditAlbumForm";
import DeleteSong from "./deleteSongs";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { fetchCurrentAlbum } from "../../redux/albums";

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
  console.log(albums);
  const allAlbums = albums && albums.songs;

  const redirect = (e) => {
    // console.log('hi')
    e.preventDefault();
    navigate(`/musicians/${user.id}/`);
  };
  //    console.log(allAlbums)
  return (
    <>
      <h1>edit</h1>
      <EditAlbumForm data={data} id={id} />
      <DeleteSong songsArray={allAlbums} id={id} />
      <button onClick={redirect}>done</button>
    </>
  );
}

export default EditPage;
