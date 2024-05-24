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

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Email
        <input
          type="email"
          name="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          required
        />
      </label>

      {isMusician ? (
        <>
          <label>
            Musician/Band Name
            <input
              type="text"
              name="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Musician/Band Name"
              required
            />
          </label>
          <label>
            Genre
            <input
              type="text"
              name="genre"
              value={genre}
              onChange={(e) => setGenre(e.target.value)}
              placeholder="Genre"
              required
            />
          </label>
        </>
      ) : (
        <>
          <label>
            Username
            <input
              type="text"
              name="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Username"
              required
            />
          </label>
          <label>
            First Name
            <input
              type="text"
              name="first_name"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
              placeholder="First Name"
              required
            />
          </label>
          <label>
            Last Name
            <input
              type="text"
              name="last_name"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
              placeholder="Last Name"
              required
            />
          </label>
        </>
      )}

      <label>
        Password
        <input
          type="password"
          name="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
        />
      </label>

      <label>
        Description
        <textarea
          name="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Description"
          required
        />
      </label>
      <label>
        Image URL
        <input
          type="text"
          name="image_url"
          value={imageUrl}
          onChange={(e) => setImageUrl(e.target.value)}
          placeholder="Image URL"
          required
        />
      </label>
      <button type="submit">Update User</button>
    </form>
  );
};

export default EditUserForm;
