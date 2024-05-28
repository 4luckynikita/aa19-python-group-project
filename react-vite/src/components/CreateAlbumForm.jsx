import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { createAnAlbum, fetchAlbums, fetchCurrentAlbum } from "../redux/albums";
import "./EditUserForm/EditUserForm.css";
import { useNavigate } from "react-router-dom";
// import { getUser, updateUser } from "../../redux/users";

const CreateAlbumForm = () => {
  // const { id } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const user = useSelector((state) => state.session.user);

  const [title, setTitle] = useState("");
  const [release_date, setRelease_date] = useState("");
  const [description, setDescription] = useState("");
  const [image_url, setImageUrl] = useState("");

  const reset = () => {
    setTitle("");
    setRelease_date("");
    setDescription("");
    setImageUrl("");
  };

  //   useEffect(() => {
  //     dispatch(getUser(id));
  //   }, [dispatch, id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = {
      title,
      release_date,
      description,
      image_url,
    };
    const createdAlbum = await dispatch(createAnAlbum(formData));
    console.log(createdAlbum);
    if (createdAlbum) {
      // console.log("===========>", "yes");
      reset();
      dispatch(fetchCurrentAlbum(createdAlbum.id));
      dispatch(fetchAlbums(user.id));

      navigate(`/albums/${createdAlbum.id}/songs`);
    }
  };

  //   if (loading) return <div>Loading...</div>;
  //   if (error) return <div>Error: {error}</div>;

  return (
    <div className="edit-user-form-container">
      <h1>Add an Album</h1>
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
            type="url"
            name="imageUrl"
            value={image_url}
            onChange={(e) => setImageUrl(e.target.value)}
            placeholder="Image URL"
            className="edit-user-textbox"
          />
        </label>
        <div className="edit-update-button-container">
          <button type="submit" className="edit-user-submit-button">
            Add Songs
          </button>
          <button
            type="button"
            className="edit-user-cancel-button"
            onClick={() => navigate(`/musicians/${user?.id}`)}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default CreateAlbumForm;
