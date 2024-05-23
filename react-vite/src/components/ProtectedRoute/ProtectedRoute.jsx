import { Navigate } from "react-router-dom";
import { useSelector } from "react-redux";

const ProtectedRoute = ({ children }) => {
  const sessionUser = useSelector((state) => state.session.user);
  return sessionUser ? children : <Navigate to="/landing" />;
};

export default ProtectedRoute;
