function SongsComponent({ songs }) {
  // //console.log(songs)
  return (
    <>
      <h1>Songs</h1>
      <ol>
        {songs &&
          songs.map((song) => {
            return (
              <>
                <li>
                  <div className="songList">
                    <p>{song.title}</p>
                    <p>{song.duration} seconds</p>
                  </div>
                </li>
              </>
            );
          })}
      </ol>
    </>
  );
}

export default SongsComponent;
