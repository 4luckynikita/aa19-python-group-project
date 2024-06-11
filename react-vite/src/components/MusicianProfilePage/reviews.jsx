import { NavLink } from "react-router-dom";
import ReviewMicrophones from "../ReviewMicrophones/ReviewMicrophones";

function ReviewsComponent({ reviews, id, title }) {
  //   //console.log(reviews);
  let reviewTitle;

  if (id) {
    reviews = reviews.filter((review) => {
      return review.album_id == id;
    });

    reviewTitle = title;
  }
  // //console.log("=====================", reviews);

  return (
    <>
      {id ? (
        <h1 className="bigger-h1">Reviews for {reviewTitle}</h1>
      ) : (
        <h1 className="bigger-h1">All Reviews</h1>
      )}
      {reviews &&
        reviews.map((review) => {
          // //console.log(review.created_at.split(" "))
          return (
            <div key={review.id} className="musician-review-div">
              <h2>{review.album.title}</h2>
              <NavLink to={`/users/${review.user.id}`}>
                {review.user.username}
              </NavLink>
              <p>{new Date(review.created_at).toLocaleDateString()}</p>
              <p className="text-aligned-ptag">
                Review: <ReviewMicrophones stars={review.rating} />
              </p>
              <p className="padded-ass-p">&quot;{review.comment}&quot;</p>
            </div>
          );
        })}
    </>
  );
}

export default ReviewsComponent;
