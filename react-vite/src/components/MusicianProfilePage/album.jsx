import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import OpenModalButton from "../OpenModalButton/OpenModalButton";
import CreateReviewModal from "../CreateReviewModal/CreateReviewModal";
import { fetchAlbums } from "../../redux/albums";
import SongsComponent from "./song";
import ReviewsComponent from "./reviews";
import { MdDelete } from "react-icons/md";
// import { MdDeleteForever } from "react-icons/md";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import DeleteAlbumModal from "./DeleteAlbumModal";
import { FaPencil } from "react-icons/fa6";
import { Link } from "react-router-dom";

function AlbumComponent({ id }) {
  const dispatch = useDispatch();
  const [albumTitle, setAlbumTitle] = useState("");

  const [albumID, setAlbumID] = useState("");
  let reviews = [];
  // console.log(id)

  useEffect(() => {
    dispatch(fetchAlbums(id));
  }, [dispatch, id]);

  const albums = useSelector((state) => state.musicianalbums.albums);
  const currentUser = useSelector((state) => state.session.user);
  const handleClick = (id, title) => {
    setAlbumID(id);
    setAlbumTitle(title);
  };
  // let showReviewButton = true;
  let showDeleteButton = false;
  if (currentUser) {
    if (currentUser.id == id) {
      // console.log(id)
      // showReviewButton = false;
    }
  }
  if (currentUser) {
    if (currentUser.id == id) {
      // console.log(id)
      showDeleteButton = true;
    }
  }

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
                    handleClick(album.id, album.title);
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
                      {/* {showReviewButton && (
                        <button className="review-button">add review</button>
                      )} */}
                      <div>
                        {showDeleteButton && (
                          <OpenModalMenuItem
                            itemText={<MdDelete />}
                            modalComponent={<DeleteAlbumModal album={album} />}
                          />
                        )}
                        {/* <MdDeleteForever /> */}
                        {showDeleteButton && (
                          <Link to={`/albums/${album.id}/update`} state={album}>
                            <FaPencil />
                          </Link>
                        )}
                      </div>
                      <OpenModalButton
                        className="post-review-button"
                        modalComponent={
                          <CreateReviewModal albumId={album.id} />
                        }
                        buttonText="Add Your Review!"
                      />
                    </div>
                    <SongsComponent songs={album.songs} />
                  </div>
                </div>
              </>
            );
          })}
      </div>
      <hr />
      <ReviewsComponent
        reviews={reviews && reviews}
        id={albumID}
        title={albumTitle}
      />
    </>
  );
}

export default AlbumComponent;
