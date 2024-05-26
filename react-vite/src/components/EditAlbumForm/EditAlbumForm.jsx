import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useLocation, useParams } from "react-router-dom";
// import { getUser, updateUser } from "../../redux/users";
import { editAlbum, fetchAlbums } from "../../redux/albums";
// import SongsComponent from "../MusicianProfilePage/song";
import CreateSongForm from "../SongsComponent/SongForm";
import { MdDelete } from "react-icons/md";
import { deleteSong } from "../../redux/albums";
// import DeleteSongModal from "../MusicianProfilePage/deleteSongModal";

const EditAlbumForm = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSelector((state) => state.session.user);
  const [title, setTitle] = useState("");
  const [release_date, setRelease_date] = useState("");
  const [description, setDescription] = useState("");
  const [image_url, setImageUrl] = useState("");
  const [addSong, setAddsong] = useState(false);
  const location = useLocation();
  const data = location.state;
  const [songsArray, setSongsArray] = useState([]);
  const currentUser = useSelector((state) => state.session.user);

  //   console.log(data)
  // const id = data.id
  // console.log(data)
  // // console.log(data.release_date)
  // let day = new Date(data.release_date).getDate()
  // day.length < 2? day= day.padStart(2, 0) : day= day
  // const year = new Date(data.release_date).getFullYear()
  // let month = new Date(data.release_date).getMonth()
  // month.length < 2? month= month.padStart(2, 0) : month= month
  // const newDate = `${year}-${month}-${day}`
  // // console.log(newDate)
  useEffect(() => {
    setSongsArray(data.songs);
  }, [data]);

  useEffect(() => {
    if (data) {
      setTitle(data.title || "");
      setDescription(data.description || "");
      setImageUrl(data.image_url || "");
    }
  }, [data]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = {
      title,
      release_date,
      description,
      image_url,
    };
    const updatedAlbum = await dispatch(editAlbum(id, formData));

    if (updatedAlbum) {
      dispatch(fetchAlbums(user.id));
    }
  };

  const redirect = (e) => {
    // console.log('hi')
    e.preventDefault();
    navigate(`/musicians/${user.id}/`);
  };

  const handleClick = (e) => {
    // console.log('hi')
    e.preventDefault();
    setAddsong(true);
  };
  console.log(addSong);
  //   if (loading) return <div>Loading...</div>;
  //   if (error) return <div>Error: {error}</div>;

  const handleDelete = async (id) => {
    // e.preventDefault()
    const deletedSong = await dispatch(deleteSong(id, currentUser.id));
    if (deletedSong) {
      console.log(data.songs);
      setSongsArray(data.songs);
    }
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="title"
          required
        />
        <input
          type="date"
          name="release_date"
          value={release_date}
          onChange={(e) => setRelease_date(e.target.value)}
          placeholder="Release Date"
          required
        />
        <textarea
          name="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Description"
        />
        <input
          type="text"
          name="imageUrl"
          value={image_url}
          onChange={(e) => setImageUrl(e.target.value)}
          placeholder="Image URL"
        />
        <button type="submit">Update Album</button>
      </form>
      {songsArray.map((song) => (
        <ol key={song.id}>
          <li>
            {song.title}{" "}
            <MdDelete
              onClick={(e) => {
                e.preventDefault();
                handleDelete(song.id);
              }}
            />
          </li>
        </ol>
      ))}
      {addSong && (
        <div>
          <CreateSongForm />
        </div>
      )}
      <button onClick={handleClick}>add more songs to your album</button>
      <button onClick={redirect}>done</button>
    </>
  );
};

export default EditAlbumForm;
