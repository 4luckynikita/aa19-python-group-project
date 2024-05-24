import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { getUser, updateUser } from "../../redux/users";

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

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Name"
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
      <button type="submit">Update Musician</button>
    </form>
  );
};

export default EditMusicianForm;
