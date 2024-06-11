import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate, useLocation } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import "./SignUpForm.css";

function SignupFormPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const location = useLocation();
  const sessionUser = useSelector((state) => state.session.user);

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [isMusician, setIsMusician] = useState(false);
  const [name, setName] = useState("");
  const [genre, setGenre] = useState("");
  const [description, setDescription] = useState("");
  const [imageUrl, setImageUrl] = useState("");
  const [errors, setErrors] = useState({});

  useEffect(() => {
    const params = new URLSearchParams(location.search);
    const type = params.get("type");
    setIsMusician(type === "musician");
  }, [location.search]);

  if (sessionUser) return <Navigate to="/" replace={true} />;

  const validateEmail = (email) => {
    const regex = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    return regex.test(email);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const newErrors = {};
    if (!validateEmail(email)) {
      newErrors.email = "Invalid email format.";
    }
    if (password.length < 8) {
      newErrors.password = "Password must be at least 8 characters.";
    }
    if (password !== confirmPassword) {
      newErrors.confirmPassword =
        "Confirm Password field must be the same as the Password field.";
    }
    if (username && (username.length < 3 || username.length > 25)) {
      newErrors.username = "Username must be between 3 and 25 characters.";
    }
    if (description.length < 10 || description.length > 1000) {
      newErrors.description =
        "Description must be between 10 and 1000 characters.";
    }
    if (Object.keys(newErrors).length > 0) {
      return setErrors(newErrors);
    }

    const userData = {
      email,
      password,
      is_musician: isMusician,
      description,
      image_url: imageUrl,
    };

    if (isMusician) {
      userData.name = name;
      userData.genre = genre;
    } else {
      userData.username = username;
      userData.first_name = firstName;
      userData.last_name = lastName;
    }

    //console.log("USER INPUT ---------", userData);

    const serverResponse = await dispatch(thunkSignup(userData));

    //console.log("RESPONSE --------", serverResponse);

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      navigate("/");
    }
  };

  return (
    <div className="sign-up-container">
      <h1>Create Your Account</h1>
      {errors.server && <p>{errors.server}</p>}
      <form onSubmit={handleSubmit} className="sign-up-form">
        <label className="sign-up-split">
          <p>Email</p>
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            placeholder="Email"
          />
        </label>
        {errors.email && <p>{errors.email}</p>}

        {isMusician ? (
          <>
            <label className="sign-up-split">
              <p>Musician/Band Name</p>
              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
                placeholder="Musician/Band Name"
              />
            </label>
            {errors.name && <p>{errors.name}</p>}
            <label className="sign-up-split">
              <p>Genre</p>
              <input
                type="text"
                value={genre}
                onChange={(e) => setGenre(e.target.value)}
                required
                placeholder="Genre"
              />
            </label>
          </>
        ) : (
          <>
            <label className="sign-up-split">
              <p>Username</p>
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
                placeholder="Username"
              />
            </label>
            {errors.username && <p>{errors.username}</p>}
            <label className="sign-up-split">
              <p>First Name</p>
              <input
                type="text"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                required
                placeholder="First Name"
              />
            </label>
            <label className="sign-up-split">
              <p>Last Name</p>
              <input
                type="text"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                required
                placeholder="Last Name"
              />
            </label>
          </>
        )}

        <label className="sign-up-split">
          <p>Password</p>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            placeholder="Password"
          />
        </label>
        {errors.password && <p>{errors.password}</p>}
        <label className="sign-up-split">
          <p>Confirm Password</p>
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
            placeholder="Confirm Password"
          />
        </label>
        {errors.confirmPassword && <p>{errors.confirmPassword}</p>}

        <label className="sign-up-split">
          <p>Description</p>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
            placeholder="Description"
          />
        </label>
        {errors.description && <p>{errors.description}</p>}
        <label className="sign-up-split">
          <p>Image URL</p>
          <input
            type="text"
            value={imageUrl}
            onChange={(e) => setImageUrl(e.target.value)}
            required
            placeholder="Image URL"
          />
        </label>
        {errors.imageUrl && <p>{errors.imageUrl}</p>}

        <div className="sign-up-button-container">
          <button type="submit" className="sign-up-submit-button">
            Sign Up
          </button>
          <button
            type="button"
            className="sign-up-cancel-button"
            onClick={() => navigate(`/landing`)}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
}

export default SignupFormPage;
