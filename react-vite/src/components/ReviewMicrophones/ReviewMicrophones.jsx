import "./ReviewMicrophones.css";

const ReviewMicrophones = ({ stars }) => {
  let starsArr = [false, false, false, false, false];
  for (let i = 0; i < stars; i++) {
    starsArr[i] = true;
  }
  console.log(starsArr);

  return (
    <div className="stars-component-container">
      {starsArr &&
        starsArr.map((star, index) => {
          return (
            <img
              key={index}
              src={`${
                star
                  ? "https://res.cloudinary.com/dkxfjbynk/image/upload/v1716585708/79fd5b87-0692-498d-b0f2-6aed85802645.png"
                  : "https://res.cloudinary.com/dkxfjbynk/image/upload/v1716585728/19369b26-1427-4931-929a-f653a3c5076c.png"
              }`}
              alt="Star"
              className="stars-microphone-icon"
            />
          );
        })}
    </div>
  );
};

export default ReviewMicrophones;
