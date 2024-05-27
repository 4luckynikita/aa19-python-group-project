import { useState } from "react";

const StarModalComponent = ({
  stars,
  setStars,
  defaultRating = 0,
  bigMode = false,
}) => {
  const [CurrentRating, setCurrentRating] = useState(defaultRating);

  const bigModeStyling = { fontSize: "30px" };
  const bigModeStylingReturn = { fontSize: "30px" };

  const handleRatingClick = (rating) => {
    setCurrentRating(rating);
    setStars(rating);
  };

  const renderStars = () => {
    const starArr = [];
    for (let i = 1; i <= 5; i++) {
      starArr.push(
        <div
          key={i}
          onClick={() => handleRatingClick(i)}
          onMouseEnter={() => setCurrentRating(i)}
          onMouseLeave={() => setCurrentRating(stars)}
        >
          {bigMode ? (
            <i
              className={`fa-${
                CurrentRating >= i ? "solid" : "regular"
              } fa-star`}
              style={bigModeStyling}
            ></i>
          ) : (
            <i
              className={`fa-${
                CurrentRating >= i ? "solid" : "regular"
              } fa-star`}
            ></i>
          )}
        </div>
      );
    }
    return starArr;
  };

  return (
    <>
      {bigMode ? (
        <div className={`stars-container`} style={bigModeStylingReturn}>
          {renderStars()} Stars
        </div>
      ) : (
        <div className={`stars-container`}>{renderStars()} Stars</div>
      )}
    </>
  );
};

export default StarModalComponent;
