import "./LoadingSpinner.css";

const LoadingSpinner = () => {
  return (
    <div className="loading-container">
      <img
        src="/beatratespinner.png"
        alt="Loading..."
        className="beatspinner"
      />
    </div>
  );
};

export default LoadingSpinner;
