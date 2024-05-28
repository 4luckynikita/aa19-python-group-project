import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
// import { fetchCurrentMusician } from "../../redux/musicians";
import { deleteAlbum, fetchAlbums } from "../../redux/albums";
import "../UserProfilePage/UserProfilePage.css"

const DeleteSongModal = ({ album }) => {
  const { closeModal } = useModal();
  const currentUser = useSelector((state) => state.session.user);
  const id = album && album.id;
  const dispatch = useDispatch();

  const handleClick = async (e) => {
    e.preventDefault();

    await dispatch(deleteAlbum(id)).then(closeModal);
    dispatch(fetchAlbums(currentUser.id));
  };

  const close = (e) => {
    e.preventDefault();
    return closeModal();
  };

  return (
    <div className="delete-modal-container">
      <h1>Confirm Delete</h1>
      <p>Are you sure you want to delete this song?</p>
      <div className="delete-modal-button-container">
        <button className="delete-modal-delete-button" onClick={handleClick}>
          Delete
        </button>
        <button className="delete-modal-keep-button" onClick={close}>
          Cancel
        </button>
      </div>
    </div>
  );
};

export default DeleteSongModal;
