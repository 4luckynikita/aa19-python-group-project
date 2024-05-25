import { useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
// import { getUser, updateUser } from "../../redux/users";
import { createAnAlbum } from "../redux/albums";

const CreateAlbumForm = () => {
  // const { id } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  //   const new_album = useSelector((state) => state.musicianalbums);
  //   const loading = useSelector((state) => state.users.loading);
  //   const error = useSelector((state) => state.users.error);

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
      console.log("===========>", "yes");
      reset();
      // navigate(`/musicians/${user.id}/`);
      navigate(`/albums/${createdAlbum.id}/songs`);
    }
  };

  //   if (loading) return <div>Loading...</div>;
  //   if (error) return <div>Error: {error}</div>;

  return (
    <>
      <h1>Add an Album</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="title"
          required
        />
        <input
          type="date"
          name="release_date"
          value={release_date}
          onChange={(e) => setRelease_date(e.target.value)}
          onFocus={(e) => e.target.showPicker()}
          placeholder="Release Date"
          required
        />
        <textarea
          name="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Description"
        />
        <input
          type="url"
          name="imageUrl"
          value={image_url}
          onChange={(e) => setImageUrl(e.target.value)}
          placeholder="Image URL"
        />
        <button type="submit">Create Album</button>
      </form>
    </>
  );
};

export default CreateAlbumForm;
