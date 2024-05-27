import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { editAlbum } from "../../redux/albums";
import AddSongForm from "./AddSong";

const EditAlbumForm = ({ id, data }) => {
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
      alert(`you album has been updated`);
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
          type="text"
          name="imageUrl"
          value={image_url}
          onChange={(e) => setImageUrl(e.target.value)}
          placeholder="Image URL"
        />
        <button type="submit">Update Album</button>
      </form>
      {addSong && (
        <div>
          <AddSongForm />
        </div>
      )}
      <button onClick={handleClick}>add more songs to your album</button>
    </>
  );
};

export default EditAlbumForm;
