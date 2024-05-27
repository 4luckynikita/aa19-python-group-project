import CreateSongForm from "./SongForm";
// import { useState } from "react";
import "../EditUserForm/EditUserForm.css"

function CreateSongPage() {
  // const [songsArray, setSongsArray] = useState([])

  //   const handleclick = (e) =>{
  //     e.preventDefault()
  //     setSongsArray([songsArray, <CreateSongForm/>])
  //   }

  // const createSong =(e) =>{
  //   e.preventDefault()
  // }

  return (
    <div className="edit-user-form-container">
      <h1>Add Songs To Your Album</h1>
      <h2>Start by adding your first song</h2>
      <CreateSongForm />
      {/* {songsArray.map((arr)=>{
        return <div>{arr}</div>
      })} */}
      {/* <button onClick={createSong}>Submit</button> */}
    </div>
  );
}

export default CreateSongPage;
