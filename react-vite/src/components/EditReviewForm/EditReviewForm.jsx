import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { getReview, updateReview } from "../../redux/reviews";
import LoadingSpinner from "../LoadingSpinner/LoadingSpinner";
import "./EditReview.css";
import StarModalComponent from "../CreateReviewModal/StarModalComponent";

const EditReviewForm = () => {
  const { reviewId } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const reviews = useSelector((state) => state.users.reviews);
  const review = reviews.find((r) => r.id === parseInt(reviewId));
  const user = useSelector((state) => state.session.user);

  const [isLoading, setIsLoading] = useState(true);
  const [rating, setRating] = useState(review?.rating || 0);
  const [comment, setComment] = useState(review?.comment || "");
  const [stars, setStars] = useState(review?.rating || 0);

  //console.log("zzzzzzzzzzzzzzzzzzzzzzzzz", review);

  useEffect(() => {
    const fetchReview = async () => {
      setIsLoading(true);
      await dispatch(getReview(reviewId));
      setIsLoading(false);
    };

    fetchReview();
  }, [dispatch, reviewId]);

  useEffect(() => {
    if (review) {
      setRating(review?.rating);
      setComment(review?.comment);
      setIsLoading(false);
    }
  }, [review]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    const updatedReview = {
      ...review,
      rating: stars,
      comment,
    };
    await dispatch(updateReview(reviewId, updatedReview));
    setIsLoading(false);
    navigate(`/users/${user && user.id}`);
  };

  if (isLoading) return <LoadingSpinner />;

  return (
    <div className="edit-review-container">
      <h1>
        Edit Your Review for <br></br> {review?.album && review?.album?.title}
      </h1>
      <form onSubmit={handleSubmit} className="edit-review-form">
        <StarModalComponent
          setStars={setStars}
          stars={stars}
          defaultRating={rating}
          bigMode="true"
        />
        <label className="edit-review-comment-container">
          <p className="edit-review-p-tag">Comment:</p>
          <textarea
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            className="edit-review-textbox"
          />
        </label>
        <div className="edit-review-lower-button-container">
          <button type="submit" className="edit-review-submit-button">
            Update Review
          </button>
          <button
            className="edit-review-cancel-button"
            onClick={() => navigate(`/users/${user?.id}`)}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default EditReviewForm;
