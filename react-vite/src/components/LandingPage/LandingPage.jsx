import { Link, useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { thunkLogin } from "../../redux/session";
import "./LandingPage.css";
import { useState, useEffect } from "react";
import clickSound from "/rock2.mp3";
import { fetchMusicians } from "../../redux/musicians";

const LandingPage = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const audio = new Audio(clickSound);

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
    audio.play();
    const serverResponse = await dispatch(thunkLogin({ email, password }));
    if (serverResponse && serverResponse.errors) {
      setErrors(serverResponse.errors);
    }
    dispatch(fetchMusicians());
  };

  const handleDemoUser = async () => {
    audio.play();
    const serverResponse = await dispatch(
      thunkLogin({ email: "demo@aa.io", password: "password" })
    );
    if (serverResponse && serverResponse.errors) {
      setErrors(serverResponse.errors);
    }

    dispatch(fetchMusicians());
  };

  const handleDemoMusician = async () => {
    audio.play();
    const serverResponse = await dispatch(
      thunkLogin({ email: "demo@musician.com", password: "password" })
    );
    if (serverResponse && serverResponse.errors) {
      setErrors(serverResponse.errors);
    }
    dispatch(fetchMusicians());
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
          <h1>Back for an Encore?</h1>
          <form onSubmit={handleSubmit}>
            <label>
              <input
                placeholder="Email"
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
          <p id="ready">Ready to Rock? Sign up as</p>
          <div id="signup">
            <Link to="/signup?type=user">User</Link>
            {" | "}
            <Link to="/signup?type=musician">Musician</Link>
          </div>
          <p>Or</p>
          <p className="demotitle">Don&apos;t want to create an account?</p>
          <button className="demobutton" onClick={handleDemoUser}>
            Login as Demo User
          </button>
          <button className="demobutton" onClick={handleDemoMusician}>
            Login as Demo Musician
          </button>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
