import { Link, useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { thunkLogin } from "../../redux/session";
import "./LandingPage.css";
import { useState, useEffect } from "react";

const LandingPage = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (sessionUser) {
      if (sessionUser.is_musician) {
        navigate(`/musicians/${sessionUser.id}`);
      } else {
        navigate("/");
      }
    }
  }, [sessionUser, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const serverResponse = await dispatch(thunkLogin({ email, password }));
    if (serverResponse && serverResponse.errors) {
      setErrors(serverResponse.errors);
    }
  };

  const handleDemoUser = async () => {
    const serverResponse = await dispatch(
      thunkLogin({ email: "demo@aa.io", password: "password" })
    );
    if (serverResponse && serverResponse.errors) {
      setErrors(serverResponse.errors);
    }
  };

  const handleDemoMusician = async () => {
    const serverResponse = await dispatch(
      thunkLogin({ email: "demo@musician.com", password: "password" })
    );
    if (serverResponse && serverResponse.errors) {
      setErrors(serverResponse.errors);
    }
  };

  return (
    <div className="landing-page">
      <div className="content-container">
        <div className="image-container">
          <img
            src="/landingpage.jpg"
            alt="BeatRate"
            className="landing-image"
          />
        </div>
        <div className="login-container">
          <h1>Back for an Encore !?</h1>
          <form onSubmit={handleSubmit}>
            <label>
              <input
                placeholder="Email / Username"
                type="text"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </label>
            <label>
              <input
                placeholder="Password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </label>
            <button type="submit">Login</button>
          </form>
          {errors.email && <p>{errors.email}</p>}
          {errors.password && <p>{errors.password}</p>}
          <p>Don&apos;t want to create an account?</p>
          <button onClick={handleDemoUser}>Login as Demo User</button>
          {" | "}
          <button onClick={handleDemoMusician}>Login as Demo Musician</button>
          <p>Or</p>
          <p>Ready to Rock? Sign up as</p>
          <Link to="/signup?type=user">User</Link>
          {" | "}
          <Link to="/signup?type=musician">Musician</Link>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
