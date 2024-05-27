import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { useEffect, useState } from "react";
import StarModalComponent from "./StarModalComponent";
import { createReview } from "../../redux/reviews"; // Import the createReview thunk
import "./CreateReviewModal.css";
import { fetchAlbums } from "../../redux/albums";

const CreateAReview = ({ albumId, musicianId }) => {
  const { closeModal } = useModal();
  const dispatch = useDispatch();
  // const currentUser = useSelector(state => state.session.user?.id);

  const [stars, setStars] = useState(0);
  const [review, setReview] = useState("");
  const [errors, setErrors] = useState({});
  // const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    const errorsObj = {};
    if (review.length < 10)
      errorsObj.review = "Review must be at least 10 characters";
    if (!stars) errorsObj.stars = "Please rate the album 1-5";
    setErrors(errorsObj);
  }, [review, stars]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    // setSubmitted(true);

    if (Object.values(errors).length === 0) {
      const reviewData = {
        rating: stars,
        comment: review,
      };
      const result = await dispatch(createReview(albumId, reviewData));
      if (result) {
        console.log(musicianId);
        dispatch(fetchAlbums(musicianId));
        closeModal();
      }
    }
  };

  return (
    <div className="review-modal-container">
      <form onSubmit={handleSubmit}>
        <h1>{`Add Your Review for ${albumId}`}</h1>
        {errors.review && <p className="errors-mess">{errors.review}</p>}
        <textarea
          type="text"
          value={review}
          onChange={(e) => setReview(e.target.value)}
          placeholder="Type your review here"
        />

        {errors.stars && <p className="errors-mess">{errors.stars}</p>}
        <StarModalComponent setStars={setStars} stars={stars} />

        <button
          type="submit"
          className="delete-review-button"
          disabled={Object.values(errors).length > 0}
        >
          Submit Your Review
        </button>
      </form>
    </div>
  );
  //(<div className="review-modal-container">
  //         <form >
  //             <h1>{`Add Your Review for ${albumId}`}</h1>
  //             {errors.review && <p className="errors-mess">{errors.review}</p>}
  //             <textarea
  //                 type="text"
  //                 value={review}
  //                 onChange={(e) => setReview(e.target.value)}
  //                 placeholder="Type your review here" />

  //             {errors.stars && <p className="errors-mess">{errors.stars}</p>}
  //             <StarModalComponent setStars={setStars} stars={stars} />

  //             <button
  //                 type="submit"
  //                 className="delete-review-button"
  //                 disabled={Object.values(errors).length > 0}>
  //                 Submit Your Review
  //             </button>

  //         </form>
  // </div>)
};

export default CreateAReview;
