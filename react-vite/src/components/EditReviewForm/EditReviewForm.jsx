import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { getReview, updateReview } from "../../redux/reviews";

const EditReviewForm = () => {
  const { reviewId } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const reviews = useSelector((state) => state.users.reviews);
  const review = reviews.find((r) => r.id === parseInt(reviewId));
  const user = useSelector((state) => state.session.user);

  const [rating, setRating] = useState(review?.rating || 0);
  const [comment, setComment] = useState(review?.comment || "");

  // console.log("zzzzzzzzzzzzzzzzzzzzzzzzz", review);

  useEffect(() => {
    dispatch(getReview(reviewId));
  }, [dispatch, reviewId]);

  useEffect(() => {
    if (review) {
      setRating(review.rating);
      setComment(review.comment);
    }
  }, [review]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const updatedReview = {
      ...review,
      rating,
      comment,
    };
    await dispatch(updateReview(reviewId, updatedReview));
    navigate(`/users/${user && user.id}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Rating:
        <select value={rating} onChange={(e) => setRating(e.target.value)}>
          {[1, 2, 3, 4, 5].map((rate) => (
            <option key={rate} value={rate}>
              {rate}
            </option>
          ))}
        </select>
      </label>
      <label>
        Comment:
        <input
          type="text"
          value={comment}
          onChange={(e) => setComment(e.target.value)}
        />
      </label>
      <button type="submit">Update Review</button>
    </form>
  );
};

export default EditReviewForm;
