import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { getUser, updateUser } from "../../redux/users";

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
      username,
      email,
      password,
      first_name: firstName,
      last_name: lastName,
      is_musician: isMusician,
      genre,
      description,
      image_url: imageUrl,
    };
    const updatedUser = await dispatch(updateUser(id, formData));
    if (updatedUser) {
      navigate(`/users/${id}`);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
        required
      />
      <input
        type="email"
        name="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
        required
      />
      <input
        type="password"
        name="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <input
        type="text"
        name="first_name"
        value={firstName}
        onChange={(e) => setFirstName(e.target.value)}
        placeholder="First Name"
      />
      <input
        type="text"
        name="last_name"
        value={lastName}
        onChange={(e) => setLastName(e.target.value)}
        placeholder="Last Name"
      />
      <label>
        Musician
        <input
          type="checkbox"
          name="is_musician"
          checked={isMusician}
          onChange={(e) => setIsMusician(e.target.checked)}
        />
      </label>
      <input
        type="text"
        name="genre"
        value={genre}
        onChange={(e) => setGenre(e.target.value)}
        placeholder="Genre"
      />
      <textarea
        name="description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="Description"
      />
      <input
        type="text"
        name="image_url"
        value={imageUrl}
        onChange={(e) => setImageUrl(e.target.value)}
        placeholder="Image URL"
      />
      <button type="submit">Update User</button>
    </form>
  );
};

export default EditUserForm;
