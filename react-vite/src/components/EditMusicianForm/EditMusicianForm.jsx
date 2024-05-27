import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { getUser, updateUser } from "../../redux/users";
import "../EditUserForm/EditUserForm.css"

const EditMusicianForm = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const musician = useSelector((state) => state.musician.musician);
  const loading = useSelector((state) => state.users.loading);
  const error = useSelector((state) => state.users.error);

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [isMusician, setIsMusician] = useState(false);
  const [genre, setGenre] = useState("");
  const [description, setDescription] = useState("");
  const [imageUrl, setImageUrl] = useState("");

  useEffect(() => {
    if (musician) {
      setName(musician.name || "");
      setEmail(musician.email || "");
      setIsMusician(true);
      setGenre(musician.genre || "");
      setDescription(musician.description || "");
      setImageUrl(musician.image_url || "");
    }
  }, [musician]);

  useEffect(() => {
    dispatch(getUser(id));
  }, [dispatch, id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = {
      name,
      email,
      is_musician: isMusician,
      genre,
      description,
      image_url: imageUrl,
    };
    const updatedUser = await dispatch(updateUser(id, formData));
    if (updatedUser) {
      navigate(`/musicians/${id}/`);
    }
  };

  if (loading) return <h1>Working...</h1>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="edit-user-form-container">
      <h1>Edit Musician Profile</h1>
      <form onSubmit={handleSubmit} className="edit-user-form">

        <label className="edit-user-text-container">
          <p className="edit-user-p-tag">Name</p>
          <input
            type="text"
            name="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Name"
            required
            className="edit-user-textbox"
          />
        </label>
        <label className="edit-user-text-container">
          <p className="edit-user-p-tag">Email</p>
          <input
            type="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
            required
            className="edit-user-textbox"
          />
        </label>
        <label className="edit-user-text-container">
          <p className="edit-user-p-tag">Genre</p>
          <input
            type="text"
            name="genre"
            value={genre}
            onChange={(e) => setGenre(e.target.value)}
            placeholder="Genre"
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
            name="image_url"
            value={imageUrl}
            onChange={(e) => setImageUrl(e.target.value)}
            placeholder="Image URL"
            className="edit-user-textbox"
          />
        </label>
        <div className="edit-update-button-container">
          <button type="submit" className="edit-user-submit-button">
            Update
          </button>
          <button
            type="button"
            className="edit-user-cancel-button"
            onClick={() => navigate(`/landing`)}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default EditMusicianForm;
