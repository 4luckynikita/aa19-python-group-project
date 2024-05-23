function SongsComponent({ songs }) {
  // console.log(songs)
  return (
    <>
      <h1>songsList</h1>
      <ol>
        {songs &&
          songs.map((song) => {
            return (
              <>
                <li>
                  <div className="songList">
                    <p>{song.title}</p>
                    <p>{song.duration}</p>
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
