import { createBrowserRouter } from "react-router-dom";
import LoginFormPage from "../components/LoginFormPage";
import SignupFormPage from "../components/SignupFormPage";
import Layout from "./Layout";
import UserProfilePage from "../components/UserProfilePage";
import EditUserForm from "../components/EditUserForm";
import EditReviewForm from "../components/EditReviewForm";
import HomePage from "../components/HomePage/HomePage";
import MusicianProfilePage from "../components/MusicianProfilePage/MusicianProfilePage";
import LandingPage from "../components/LandingPage";
import ProtectedRoute from "../components/ProtectedRoute/ProtectedRoute";

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/landing",
        element: <LandingPage />,
      },
      {
        path: "/",
        element: (
          <ProtectedRoute>
            <HomePage />
          </ProtectedRoute>
        ),
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
        element: (
          <ProtectedRoute>
            <UserProfilePage />
          </ProtectedRoute>
        ),
      },
      {
        path: "users/:id/edit",
        element: (
          <ProtectedRoute>
            <EditUserForm />
          </ProtectedRoute>
        ),
      },
      {
        path: "reviews/:reviewId/edit",
        element: (
          <ProtectedRoute>
            <EditReviewForm />
          </ProtectedRoute>
        ),
      },
      {
        path: "musicians/:id",
        element: (
          <ProtectedRoute>
            <MusicianProfilePage />
          </ProtectedRoute>
        ),
      },
    ],
  },
]);
