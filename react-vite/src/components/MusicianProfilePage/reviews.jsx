import { NavLink } from "react-router-dom";

function ReviewsComponent({ reviews, id }) {
  //   console.log(reviews);
  if (id) {
    reviews = reviews.filter((review) => {
      return review.album_id == id;
    });
  }
  //   console.log("=====================", reviews);

  return (
    <>
      <h1>Reviews</h1>
      {reviews &&
        reviews.map((review) => {
          // console.log(review.created_at.split(" "))
          return (
            <div key={review.id}>
              <NavLink to={`/users/${review.user.id}`}>
                {review.user.username}
              </NavLink>
              <p>{new Date(review.created_at).toLocaleDateString()}</p>
              <p>{review.rating}</p>
              <p>{review.comment}</p>
            </div>
          );
        })}
    </>
  );
}

export default ReviewsComponent;
