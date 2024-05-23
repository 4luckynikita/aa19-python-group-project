import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { fetchAlbums } from "../../redux/albums";
import SongsComponent from "./song";
import ReviewsComponent from "./reviews";

function AlbumComponent({ id }) {
  const dispatch = useDispatch();

  const [albumID, setAlbumID] = useState("");
  let reviews = [];
  // console.log(id)

  useEffect(() => {
    dispatch(fetchAlbums(id));
  }, [dispatch, id]);

  const albums = useSelector((state) => state.albums.albums);

  const handleClick = (id) => {
    setAlbumID(id);
  };

  if (!albums || albums.length === 0) {
    return <p>No albums added yet!</p>;
  }

  return (
    <>
      <h1>albums</h1>
      <div className="all-albums-grid">
        {albums &&
          albums.map((album) => {
            reviews.push(...album.reviews);

            return (
              <>
                <div
                  key={album.id}
                  className="album-container"
                  onClick={() => {
                    handleClick(album.id);
                  }}
                >
                  <div className="album-image-container">
                    <img
                      className="album-image"
                      src={
                        album.image_url
                          ? `${album.image_url}`
                          : "aa19-python-group-project/react-vite/public/placeholder.png"
                      }
                      alt="artist's/band's photo"
                    />
                  </div>
                  <div className="album-details-container">
                    <h2 className="album-name">{album.title}</h2>
                    <hr className="line" />
                    <p className="album-year">
                      {album.release_date.split(" ")[3]}
                    </p>
                    <div className="number-and-review">
                      <p className="number-of-songs">
                        {album.songs.length == 1
                          ? `${album.songs.length} song`
                          : `${album.songs.length} songs`}
                      </p>
                      <button className="review-button">add review</button>
                    </div>
                    <SongsComponent songs={album.songs} />
                  </div>
                </div>
              </>
            );
          })}
      </div>
      <hr />
      <ReviewsComponent reviews={reviews && reviews} id={albumID} />
    </>
  );
}

export default AlbumComponent;
