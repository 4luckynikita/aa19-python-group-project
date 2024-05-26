import { useState } from "react";
import { useDispatch, useSelector} from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import { CreateSong, fetchAlbums, fetchCurrentAlbum } from "../../redux/albums";


function AddSongForm(){
 const dispatch = useDispatch();
 const navigate = useNavigate();
 const sessionUser = useSelector((state) => state.session.user);
 const [title, setTitle] = useState("");
 const [duration, setDuration] = useState("");
 const { id } = useParams();
 const reset = () => {
     setTitle("");
     setDuration("");
   }

 const handleSubmit = async (e) => {
   e.preventDefault();
   const formData = {
    title,
    duration,
   };
   const newSong = await dispatch (CreateSong(formData, id));
   // console.log(createdAlbum)
   if (newSong) {
     console.log('===========>',"yes")
     reset()
     dispatch(fetchAlbums(sessionUser.id))
     dispatch(fetchCurrentAlbum(id))
    //  navigate(`/musicians/${sessionUser.id}/`);
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
     <button type="submit">Submit</button>
   </form>
   </>
 )
}

export default AddSongForm
