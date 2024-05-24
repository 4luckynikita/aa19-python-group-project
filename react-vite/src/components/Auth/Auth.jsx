import { useEffect } from "react";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";

const Auth = ({ children }) => {
  const navigate = useNavigate();
  const sessionUser = useSelector((state) => state.session.user);

  useEffect(() => {
    if (sessionUser) {
      if (sessionUser.is_musician) {
        navigate(`/musicians/${sessionUser.id}`);
      } else {
        navigate("/");
      }
    }
  }, [sessionUser, navigate]);

  return children;
};

export default Auth;
