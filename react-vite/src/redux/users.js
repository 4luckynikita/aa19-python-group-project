// Action Types
const GET_USER_REQUEST = 'users/GET_USER_REQUEST';
const GET_USER_SUCCESS = 'users/GET_USER_SUCCESS';
const GET_USER_FAILURE = 'users/GET_USER_FAILURE';

const UPDATE_USER_REQUEST = 'users/UPDATE_USER_REQUEST';
const UPDATE_USER_SUCCESS = 'users/UPDATE_USER_SUCCESS';
const UPDATE_USER_FAILURE = 'users/UPDATE_USER_FAILURE';


const getUserRequest = () => ({ type: GET_USER_REQUEST });
const getUserSuccess = (user) => ({ type: GET_USER_SUCCESS, payload: user });
const getUserFailure = (error) => ({ type: GET_USER_FAILURE, payload: error });

const updateUserRequest = () => ({ type: UPDATE_USER_REQUEST });
const updateUserSuccess = (user) => ({ type: UPDATE_USER_SUCCESS, payload: user });
const updateUserFailure = (error) => ({ type: UPDATE_USER_FAILURE, payload: error });


export const getUser = (id) => async (dispatch) => {
  dispatch(getUserRequest());
  try {
    const response = await fetch(`/api/users/${id}`, {
      credentials: 'include',
    });
    if (!response.ok) {
      throw new Error('Failed to fetch user');
    }
    const data = await response.json();
    dispatch(getUserSuccess(data));
  } catch (error) {
    dispatch(getUserFailure(error.message));
  }
};

export const updateUser = (id, user) => async (dispatch) => {
  dispatch(updateUserRequest());
  try {
    const response = await fetch(`/api/users/update/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      credentials: 'include',
      body: JSON.stringify(user),
    });
    if (!response.ok) {
      throw new Error('Failed to update user');
    }
    const data = await response.json();
    dispatch(updateUserSuccess(data));
  } catch (error) {
    dispatch(updateUserFailure(error.message));
  }
};


const initialState = {
  loading: false,
  error: null,
  users: {},
};


const usersReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_USER_REQUEST:
    case UPDATE_USER_REQUEST:
      return {
        ...state,
        loading: true,
        error: null,
      };
    case GET_USER_SUCCESS:
    case UPDATE_USER_SUCCESS:
      return {
        ...state,
        loading: false,
        users: {
          ...state.users,
          [action.payload.id]: action.payload,
        },
      };
    case GET_USER_FAILURE:
    case UPDATE_USER_FAILURE:
      return {
        ...state,
        loading: false,
        error: action.payload,
      };
    default:
      return state;
  }
};

export default usersReducer;
