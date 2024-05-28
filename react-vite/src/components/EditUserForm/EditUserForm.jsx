import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { getUser, updateUser } from "../../redux/users";
import "./EditUserForm.css";

const EditUserForm = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSelector((state) => state.users.users[id]);
  const loading = useSelector((state) => state.users.loading);
  const error = useSelector((state) => state.users.error);

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [isMusician, setIsMusician] = useState(false);
  const [name, setName] = useState("");
  const [genre, setGenre] = useState("");
  const [description, setDescription] = useState("");
  const [imageUrl, setImageUrl] = useState("");

  useEffect(() => {
    if (user) {
      setUsername(user.username || "");
      setEmail(user.email || "");
      setFirstName(user.first_name || "");
      setLastName(user.last_name || "");
      setIsMusician(user.is_musician || false);
      setName(user.name || "");
      setGenre(user.genre || "");
      setDescription(user.description || "");
      setImageUrl(user.image_url || "");
    }
  }, [user]);

  useEffect(() => {
    dispatch(getUser(id));
  }, [dispatch, id]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = {
      email,
      password,
      is_musician: isMusician,
      description,
      image_url: imageUrl,
    };

    if (isMusician) {
      formData.name = name;
      formData.genre = genre;
    } else {
      formData.username = username;
      formData.first_name = firstName;
      formData.last_name = lastName;
    }

    const updatedUser = await dispatch(updateUser(id, formData));
    if (updatedUser) {
      navigate(`/users/${id}/`);
    }
  };

  if (loading) return <h1>Working...</h1>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="edit-user-form-container">
      <h1>Edit User Profile</h1>
      <form onSubmit={handleSubmit} className="edit-user-form">
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

        {isMusician ? (
          <>
            <label className="edit-user-text-container">
              <p className="edit-user-p-tag">Musician/Band Name</p>
              <input
                type="text"
                name="name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Musician/Band Name"
                required
                className="edit-user-textbox"
              />
            </label>
            <label className="edit-user-text-container">
              Genre
              <input
                type="text"
                name="genre"
                value={genre}
                onChange={(e) => setGenre(e.target.value)}
                placeholder="Genre"
                required
                className="edit-user-textbox"
              />
            </label>
          </>
        ) : (
          <>
            <label className="edit-user-text-container">
              <p className="edit-user-p-tag">Username</p>
              <input
                type="text"
                name="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Username"
                required
                className="edit-user-textbox"
              />
            </label>
            <label className="edit-user-text-container">
              <p className="edit-user-p-tag">First Name</p>
              <input
                type="text"
                name="first_name"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                placeholder="First Name"
                required
                className="edit-user-textbox"
              />
            </label>
            <label className="edit-user-text-container">
              <p className="edit-user-p-tag">Last Name</p>
              <input
                type="text"
                name="last_name"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                placeholder="Last Name"
                required
                className="edit-user-textbox"
              />
            </label>
          </>
        )}

        <label className="edit-user-text-container">
          <p className="edit-user-p-tag">Password</p>
          <input
            type="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password (optional)"
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
            required
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
            required
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

export default EditUserForm;
