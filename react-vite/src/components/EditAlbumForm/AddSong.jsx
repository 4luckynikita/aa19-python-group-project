import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { CreateSong, fetchAlbums, fetchCurrentAlbum } from "../../redux/albums";
import "../EditUserForm/EditUserForm.css"

function AddSongForm() {
  const dispatch = useDispatch();

  const sessionUser = useSelector((state) => state.session.user);
  const [title, setTitle] = useState("");
  const [duration, setDuration] = useState("");
  const { id } = useParams();
  const reset = () => {
    setTitle("");
    setDuration("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = {
      title,
      duration,
    };
    const newSong = await dispatch(CreateSong(formData, id));
    // console.log(createdAlbum)
    if (newSong) {
      console.log("===========>", "yes");
      reset();
      dispatch(fetchAlbums(sessionUser.id));
      dispatch(fetchCurrentAlbum(id));
      //  navigate(`/musicians/${sessionUser.id}/`);
    }
  };

  //   if (loading) return <div>Loading...</div>;
  //   if (error) return <div>Error: {error}</div>;

  return (
    <div className="edit-user-form-container">
      <form onSubmit={handleSubmit} className="edit-user-form">
      <label className="edit-user-text-container">
          <p className="edit-user-p-tag">Title</p>
        <input
          type="text"
          name="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Title"
          required
          className="edit-user-textbox"
        />
        </label>
        <label className="edit-user-text-container">
          <p className="edit-user-p-tag">Duration</p>
        <input
          type="integer"
          name="duration"
          value={duration}
          onChange={(e) => setDuration(e.target.value)}
          placeholder="Duration (In Seconds)"
          required
          className="edit-user-textbox"
        />
        </label>
        <div className="edit-update-button-container">
          <button type="submit" className="edit-user-submit-button">
            Confirm Song Details
          </button>
        </div>
      </form>
    </div>
  );
}

export default AddSongForm;
