import { MdDelete } from "react-icons/md";
import { deleteSong, fetchAlbums, fetchCurrentAlbum } from "../../redux/albums";
import { useDispatch, useSelector } from "react-redux";
import "../EditUserForm/EditUserForm.css"

function DeleteSong({ songsArray, id }) {
  const currentUser = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const handleDelete = async (songId, title) => {
    // alert(`you have deleted the song titled ${title}`);
    const deletedSong = await dispatch(deleteSong(songId, currentUser.id));
    if (deletedSong) {
      dispatch(fetchAlbums(currentUser.id));
      dispatch(fetchCurrentAlbum(id));
    }
  };

  return (
    <>
      {songsArray && (
        <ol className="edit-user-text-container">
          <p className="edit-user-p-tag underlined-p">Song List</p>
          {songsArray.map((song) => (
            <li key={song.id} className="song-list-li">
              {song.title}
              <MdDelete
                onClick={(e) => {
                  e.preventDefault();
                  handleDelete(song.id, song.title);
                }}
                style={{cursor: "pointer"}}
              />
            </li>
          ))}
          {!songsArray.length && <p>This album has no songs</p>}
        </ol>
      )}
    </>
  );
}

export default DeleteSong;
