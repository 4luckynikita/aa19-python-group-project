import { createBrowserRouter } from "react-router-dom";
import LoginFormPage from "../components/LoginFormPage";
import SignupFormPage from "../components/SignupFormPage";
import Layout from "./Layout";
import UserProfilePage from "../components/UserProfilePage";
import EditUserForm from "../components/EditUserForm";
import EditReviewForm from "../components/EditReviewForm";

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <h1>Welcome!</h1>,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "users/:id",
        element: <UserProfilePage />,
      },
      {
        path: "users/:id/edit",
        element: <EditUserForm />,
      },
      {
        path: "reviews/:reviewId/edit",
        element: <EditReviewForm />,
      },
    ],
  },
]);
