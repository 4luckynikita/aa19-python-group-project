import { useState } from "react";
import { useDispatch, useSelector} from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import { CreateSong, fetchAlbums } from "../../redux/albums";


function CreateSongForm(){
 const dispatch = useDispatch();
 const navigate = useNavigate();
 const sessionUser = useSelector((state) => state.session.user);
 const [title, setTitle] = useState("");
 const [duration, setDuration] = useState("");
 const [image_url, setImageUrl] = useState("");
 const { id } = useParams();
 const reset = () => {
     setTitle("");
     setDuration("");
     setImageUrl("");
   }

 const handleSubmit = async (e) => {
   e.preventDefault();
   const formData = {
    title,
    duration,
    image_url
   };
   const newSong = await dispatch (CreateSong(formData, id));
   // console.log(createdAlbum)
   if (newSong) {
     console.log('===========>',"yes")
     reset()
     dispatch(fetchAlbums(sessionUser.id))
     navigate(`/musicians/${sessionUser.id}/`);
   }
 };

//   if (loading) return <div>Loading...</div>;
//   if (error) return <div>Error: {error}</div>;

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
       type="integer"
       name="duration"
       value={duration}
       onChange={(e) => setDuration(e.target.value)}
       placeholder="duration"
       required
     />
     <input
       type="url"
       name="imageUrl"
       value={image_url}
       onChange={(e) => setImageUrl(e.target.value)}
       placeholder="Image URL"
     />
     <button type="submit">Submit</button>
   </form>
   </>
 )
}

export default CreateSongForm
