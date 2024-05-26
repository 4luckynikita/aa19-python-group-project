import { MdDelete } from "react-icons/md";
import { deleteSong, fetchAlbums, fetchCurrentAlbum } from "../../redux/albums";
import { useDispatch, useSelector } from "react-redux";

function DeleteSong({ songsArray, id }) {
  const currentUser = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const handleDelete = async (songId, title) => {
    alert(`you have deleted the song titled ${title}`);
    const deletedSong = await dispatch(deleteSong(songId, currentUser.id));
    if (deletedSong) {
      dispatch(fetchAlbums(currentUser.id));
      dispatch(fetchCurrentAlbum(id));
    }
  };

  return (
    <>
      {songsArray && (
        <ol>
          {songsArray.map((song) => (
            <li key={song.id}>
              {song.title}
              <MdDelete
                onClick={(e) => {
                  e.preventDefault();
                  handleDelete(song.id, song.title);
                }}
              />
            </li>
          ))}
        </ol>
      )}
    </>
  );
}

export default DeleteSong;
