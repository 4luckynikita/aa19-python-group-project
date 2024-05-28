import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { editAlbum } from "../../redux/albums";
import AddSongForm from "./AddSong";
import "../EditUserForm/EditUserForm.css"
import DeleteSong from "./deleteSongs";

const EditAlbumForm = ({ id, data, songsArray=null }) => {
  const dispatch = useDispatch();

  const [title, setTitle] = useState("");
  const [release_date, setRelease_date] = useState("");
  const [description, setDescription] = useState("");
  const [image_url, setImageUrl] = useState("");
  const [addSong, setAddsong] = useState(false);

  useEffect(() => {
    if (data) {
      setTitle(data.title || "");
      setDescription(data.description || "");
      setImageUrl(data.image_url || "");
      setRelease_date(
        data.release_date
          ? new Date(data.release_date).toISOString().split("T")[0]
          : ""
      );
    }
  }, [data, id]);

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
      alert(`Your album has been updated`);
      setTitle(updatedAlbum.title || "");
      setDescription(updatedAlbum.description || "");
      setImageUrl(updatedAlbum.image_url || "");
      setRelease_date(
        updatedAlbum.release_date
          ? new Date(updatedAlbum.release_date).toISOString().split("T")[0]
          : ""
      );
    }
  };

  const handleClick = (e) => {
    // console.log('hi')
    e.preventDefault();
    setAddsong(true);
  };

  return (
    <>
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
          <p className="edit-user-p-tag">Release Date</p>
          <input
            type="date"
            name="release_date"
            value={release_date}
            onChange={(e) => setRelease_date(e.target.value)}
            onFocus={(e) => e.target.showPicker()}
            placeholder="Release Date"
            required
            className="edit-user-textbox"
          />
        </label>
        <label className="edit-user-text-container">
          <p className="edit-user-p-tag">Description</p>
          <textarea
            name="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Description"
            className="edit-user-textbox"
          />
        </label>
        <label className="edit-user-text-container">
          <p className="edit-user-p-tag">Image URL</p>
          <input
            type="text"
            name="imageUrl"
            value={image_url}
            onChange={(e) => setImageUrl(e.target.value)}
            placeholder="Image URL"
            className="edit-user-textbox"
          />
        </label>
        <div className="edit-update-button-container">
          <button type="submit" className="edit-user-submit-button">
            Save Album Changes
          </button>
        </div>

      </form>
      <div className="padded-white-line" />
      <DeleteSong songsArray={songsArray} id={id} />
      {addSong && (
        <AddSongForm />
      )}
      {!addSong && (
        <button onClick={handleClick} className="edit-user-submit-button">Add songs to your album</button>
      )}
      
    </>
  );
};

export default EditAlbumForm;
