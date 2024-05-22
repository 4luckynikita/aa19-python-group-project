export const GET_REVIEW_REQUEST = "reviews/GET_REVIEW_REQUEST";
export const GET_REVIEW_SUCCESS = "reviews/GET_REVIEW_SUCCESS";
export const GET_REVIEW_FAILURE = "reviews/GET_REVIEW_FAILURE";

export const UPDATE_REVIEW_REQUEST = "reviews/UPDATE_REVIEW_REQUEST";
export const UPDATE_REVIEW_SUCCESS = "reviews/UPDATE_REVIEW_SUCCESS";
export const UPDATE_REVIEW_FAILURE = "reviews/UPDATE_REVIEW_FAILURE";

export const DELETE_REVIEW_REQUEST = "reviews/DELETE_REVIEW_REQUEST";
export const DELETE_REVIEW_SUCCESS = "reviews/DELETE_REVIEW_SUCCESS";
export const DELETE_REVIEW_FAILURE = "reviews/DELETE_REVIEW_FAILURE";

const getReviewRequest = () => ({ type: GET_REVIEW_REQUEST });
const getReviewSuccess = (review) => ({
  type: GET_REVIEW_SUCCESS,
  payload: review,
});
const getReviewFailure = (error) => ({
  type: GET_REVIEW_FAILURE,
  payload: error,
});

const updateReviewRequest = () => ({ type: UPDATE_REVIEW_REQUEST });
const updateReviewSuccess = (review) => ({
  type: UPDATE_REVIEW_SUCCESS,
  payload: review,
});
const updateReviewFailure = (error) => ({
  type: UPDATE_REVIEW_FAILURE,
  payload: error,
});

const deleteReviewRequest = () => ({ type: DELETE_REVIEW_REQUEST });
const deleteReviewSuccess = (reviewId) => ({
  type: DELETE_REVIEW_SUCCESS,
  payload: reviewId,
});
const deleteReviewFailure = (error) => ({
  type: DELETE_REVIEW_FAILURE,
  payload: error,
});

export const getReview = (reviewId) => async (dispatch) => {
  dispatch(getReviewRequest());
  try {
    const response = await fetch(`/api/reviews/${reviewId}`, {
      credentials: "include",
    });
    if (!response.ok) {
      throw new Error("Failed to fetch review");
    }
    const data = await response.json();
    dispatch(getReviewSuccess(data));
  } catch (error) {
    dispatch(getReviewFailure(error.message));
  }
};

export const updateReview = (reviewId, review) => async (dispatch) => {
  dispatch(updateReviewRequest());
  try {
    const response = await fetch(`/api/reviews/${reviewId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify(review),
    });
    if (!response.ok) {
      throw new Error("Failed to update review");
    }
    const data = await response.json();
    dispatch(updateReviewSuccess(data));
    return data;
  } catch (error) {
    dispatch(updateReviewFailure(error.message));
  }
};

export const deleteReview = (reviewId) => async (dispatch) => {
  dispatch(deleteReviewRequest());
  try {
    const response = await fetch(`/api/reviews/${reviewId}`, {
      method: "DELETE",
      credentials: "include",
    });
    if (!response.ok) {
      throw new Error("Failed to delete review");
    }
    dispatch(deleteReviewSuccess(reviewId));
  } catch (error) {
    dispatch(deleteReviewFailure(error.message));
  }
};

const initialState = {
  loading: false,
  error: null,
  reviews: {},
};

const reviewsReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_REVIEW_REQUEST:
    case UPDATE_REVIEW_REQUEST:
    case DELETE_REVIEW_REQUEST:
      return {
        ...state,
        loading: true,
        error: null,
      };
    case GET_REVIEW_SUCCESS:
    case UPDATE_REVIEW_SUCCESS: {
      return {
        ...state,
        loading: false,
        reviews: {
          ...state.reviews,
          [action.payload.id]: action.payload,
        },
      };
    }
    case DELETE_REVIEW_SUCCESS: {
      // eslint-disable-next-line no-unused-vars
      const { [action.payload]: _, ...remainingReviews } = state.reviews;
      return {
        ...state,
        loading: false,
        reviews: remainingReviews,
      };
    }
    case GET_REVIEW_FAILURE:
    case UPDATE_REVIEW_FAILURE:
    case DELETE_REVIEW_FAILURE:
      return {
        ...state,
        loading: false,
        error: action.payload,
      };
    default:
      return state;
  }
};

export default reviewsReducer;
