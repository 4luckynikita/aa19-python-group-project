import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { getUser, getUserReviews } from "../../redux/users";
import { getAlbums } from "../../redux/albums";
import { deleteReview } from "../../redux/reviews";
// import "./UserProfilePage.css";

const UserProfilePage = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const loggedInUser = useSelector((state) => state.session.user);
  const user = useSelector((state) => state.users.users[id]);
  const reviews = useSelector((state) => state.users.reviews);
  const albums = useSelector((state) => state.albums.albums);

  const loading = useSelector((state) => state.users.loading);
  const error = useSelector((state) => state.users.error);

  useEffect(() => {
    dispatch(getUser(id));
    dispatch(getUserReviews(id));
    dispatch(getAlbums());
  }, [dispatch, id]);

  const handleDeleteReview = async (reviewId) => {
    await dispatch(deleteReview(reviewId));
    dispatch(getUserReviews(id));
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  if (!user) return <div>User not found</div>;

  return (
    <div>
      {user && (
        <>
          <div>
            <img src={user.image_url} alt={user.image_url} />
            <div>
              <div>
                <h1>{`${user.first_name} ${user.last_name}`}</h1>
                <p>
                  Joined in {new Date(user.created_at).toLocaleDateString()}
                </p>
              </div>
              <div>
                <p>{user.description}</p>
              </div>
              {loggedInUser && loggedInUser.id === user.id && (
                <div>
                  <button onClick={() => navigate(`/users/${id}/edit`)}>
                    Edit Profile
                  </button>
                </div>
              )}
            </div>
          </div>
          <h2>All Reviews</h2>
          <div className="reviews">
            {reviews.map((review) => {
              const filteredAlbums = albums.filter(
                (album) => album.id === review.album_id
              );
              return (
                <div key={review.id} className="review">
                  {loggedInUser && loggedInUser.id === review.user_id && (
                    <div>
                      <button
                        onClick={() => navigate(`/reviews/${review.id}/edit`)}
                      >
                        Edit Review
                      </button>
                      <button onClick={() => handleDeleteReview(review.id)}>
                        Delete Review
                      </button>
                    </div>
                  )}
                  <h3>{review.user["username"]}</h3>
                  <p>{new Date(review["created_at"]).toLocaleDateString()}</p>
                  <p>Rating: {review.rating}</p>
                  <p>{review.comment}</p>
                  {filteredAlbums.map((album) => (
                    <div key={album.id} className="album">
                      <img src={album.image_url} alt="Album" />
                      <p>{album.title}</p>
                      <p>{album.user.name}</p>
                      <p>{new Date(album.release_date).getFullYear()}</p>
                      <div>
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
  );
};

export default UserProfilePage;
