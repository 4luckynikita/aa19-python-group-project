import CreateSongForm from "./SongForm";
// import { useState } from "react";

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
    <>
      <h1>Add Songs To Your Album</h1>
      <h3>Start by adding your first song</h3>
      <CreateSongForm />
      {/* {songsArray.map((arr)=>{
        return <div>{arr}</div>
      })} */}
      {/* <button onClick={createSong}>Submit</button> */}
    </>
  );
}

export default CreateSongPage;
