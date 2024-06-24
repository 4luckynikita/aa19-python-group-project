import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { getUser, getUserReviews } from "../../redux/users";
import { getAlbums } from "../../redux/albums";
import { deleteReview } from "../../redux/reviews";
import ReviewMicrophones from "../ReviewMicrophones/ReviewMicrophones";
import LoadingSpinner from "../LoadingSpinner/LoadingSpinner";
import "./UserProfilePage.css";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import { useModal } from "../../context/Modal";

const DeleteReviewModal = ({ reviewId, id }) => {
  const { closeModal } = useModal();

  const dispatch = useDispatch();
  const handleClick = async (e) => {
    e.preventDefault();

    await dispatch(deleteReview(reviewId)).then(closeModal);
    dispatch(getUserReviews(id));
  };

  const close = (e) => {
    e.preventDefault();
    return closeModal();
  };

  return (
    <div className="delete-modal-container">
      <h1 className="black">Confirm Delete</h1>
      <p className="black">Are you sure you want to delete this review?</p>
      <div className="delete-modal-button-container">
        <button className="delete-modal-delete-button" onClick={handleClick}>
          Delete
        </button>
        <button className="delete-modal-keep-button" onClick={close}>
          Cancel
        </button>
      </div>
    </div>
  );
};

const UserProfilePage = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const loggedInUser = useSelector((state) => state.session.user);
  const user = useSelector((state) => state.users.users[id]);
  const reviews = useSelector((state) => state.users.reviews);
  const albums = useSelector((state) => state.albums.albums);
  const [isLoading, setIsLoading] = useState(true);

  // const loading = useSelector((state) => state.users.loading);
  const error = useSelector((state) => state.users.error);

  useEffect(() => {
    const fetchData = async () => {
      await dispatch(getUser(id));
      await dispatch(getUserReviews(id));
      await dispatch(getAlbums());
      setIsLoading(false);
    };
    fetchData();
  }, [dispatch, id]);

  // const handleDeleteReview = async (reviewId) => {
  //   await dispatch(deleteReview(reviewId));
  //   dispatch(getUserReviews(id));
  // };

  if (error) return <div>Error: {error}</div>;

  return (
    <>
      {isLoading ? (
        <LoadingSpinner />
      ) : (
        <div className="user-everything-container">
          {user && (
            <>
              <h1 className="user-profile-username">{user.username}</h1>
              <div className="user-profile-container">
                <div className="user-profile-container-left">
                  <img
                    src={user.image_url}
                    alt={user.image_url}
                    className="user-profile-picture"
                  />
                  {/* <div className="user-profile-socials-container">
                <a
                  href="https://www.facebook.com"
                  target="_blank"
                  rel="noreferrer"
                >
                  <img
                    src="https://res.cloudinary.com/dkxfjbynk/image/upload/v1716589080/085acd0d-df7a-4317-8df5-6941a1106f09.png"
                    className="user-profile-social-logo"
                  />
                </a>
                <a
                  href="https://www.soundcloud.com"
                  target="_blank"
                  rel="noreferrer"
                >
                  <img
                    src="https://res.cloudinary.com/dkxfjbynk/image/upload/v1716589543/6c2fbc03-c0d4-44f1-91b7-2a347958480c.png"
                    className="user-profile-social-logo"
                  />
                </a>
                <a
                  href="https://www.spotify.com"
                  target="_blank"
                  rel="noreferrer"
                >
                  <img
                    src="https://res.cloudinary.com/dkxfjbynk/image/upload/v1716589564/d599756b-4264-4136-a217-ac49cade5466.png"
                    className="user-profile-social-logo"
                  />
                </a>
                <a
                  href="https://www.instagram.com"
                  target="_blank"
                  rel="noreferrer"
                >
                  <img
                    src="https://res.cloudinary.com/dkxfjbynk/image/upload/v1716589605/eac947d2-b379-4f79-a80a-62b9955114f5.png"
                    className="user-profile-social-logo"
                  />
                </a>
              </div> */}
                </div>
                <div className="user-profile-container-right">
                  <div className="user-profile-container-right-upper">
                    <h1 className="user-profile-firstandlast">{`${user.first_name} ${user.last_name}`}</h1>
                    <p className="user-profile-joindate">
                      Joined on {new Date(user.created_at).toLocaleDateString()}
                    </p>
                  </div>
                  <div>
                    <p className="user-profile-description">
                      {user.description}
                    </p>
                  </div>
                  {loggedInUser && loggedInUser.id === user.id && (
                    <div className="user-profile-edit-container">
                      <button
                        onClick={() => navigate(`/users/${id}/edit`)}
                        className="user-edit-profile-button"
                      >
                        Edit Profile
                      </button>
                    </div>
                  )}
                </div>
              </div>

              <h2 className="user-all-reviews-text">All Reviews</h2>
              <div className="reviews-container">
                {reviews.map((review) => {
                  const filteredAlbums = albums.filter(
                    (album) => album.id === review.album_id
                  );
                  return (
                    <div key={review.id} className="review-container-full">
                      <div className="review-container-leftmost">
                        <div className="review-container-upper">
                          <div>
                            <h3>
                              {review.user["username"]}
                              <br />{" "}
                            </h3>
                            <p>
                              {new Date(
                                review["created_at"]
                              ).toLocaleDateString()}
                            </p>
                          </div>
                          {loggedInUser &&
                            loggedInUser.id === review.user_id && (
                              <div className="editdeletecontainer">
                                <button
                                  onClick={() =>
                                    navigate(`/reviews/${review.id}/edit`)
                                  }
                                  className="review-edit-delete-button"
                                >
                                  <img
                                    src="https://res.cloudinary.com/dkxfjbynk/image/upload/v1716588692/d9d1887d-a603-4456-8c4e-37c2c272364c.png"
                                    className="review-edit-delete-image"
                                  />
                                </button>
                                <button
                                  // onClick={() => handleDeleteReview(review.id)}
                                  className="review-edit-delete-button"
                                >
                                  <OpenModalMenuItem
                                    itemText={
                                      <img
                                        src="https://res.cloudinary.com/dkxfjbynk/image/upload/v1716588777/b616eb42-5250-4686-8288-a1d843e55284.png"
                                        className="review-edit-delete-image"
                                      />
                                    }
                                    modalComponent={
                                      <DeleteReviewModal
                                        reviewId={review.id}
                                        id={id}
                                      />
                                    }
                                  />
                                </button>
                              </div>
                            )}
                        </div>
                        <div className="rating-mic-container">
                          <p>Rating:</p>
                          <ReviewMicrophones stars={review.rating} />
                        </div>
                        <p className="rating-review-text">{review.comment}</p>
                      </div>
                      {filteredAlbums.map((album) => (
                        <div
                          key={album.id}
                          className="review-container-rightmost"
                        >
                          <img
                            src={album.image_url}
                            alt="Album"
                            className="review-album-image"
                          />
                          <div className="review-album-rightmost">
                            <h1>{album.title}</h1>
                            <p>{album.user.name}</p>
                            <div className="nice-line" />
                            <p>{new Date(album.release_date).getFullYear()}</p>

                            <p>
                              {album.songs.length}{" "}
                              {album.songs.length === 1 ? "song" : "songs"}
                            </p>
                          </div>
                        </div>
                      ))}
                    </div>
                  );
                })}
              </div>
            </>
          )}
        </div>
      )}
    </>
  );
};

export default UserProfilePage;
