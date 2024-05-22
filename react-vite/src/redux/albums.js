const GET_ALBUMS_REQUEST = "albums/GET_ALBUMS_REQUEST";
const GET_ALBUMS_SUCCESS = "albums/GET_ALBUMS_SUCCESS";
const GET_ALBUMS_FAILURE = "albums/GET_ALBUMS_FAILURE";
const GET_ALL_ALBUMS = "albumsReducer/GET_ALL_ALBUMS";

const getAlbumsRequest = () => ({ type: GET_ALBUMS_REQUEST });
const getAlbumsSuccess = (albums) => ({
  type: GET_ALBUMS_SUCCESS,
  payload: albums,
});
const getAlbumsFailure = (error) => ({
  type: GET_ALBUMS_FAILURE,
  payload: error,
});

const getAlbums2 = (albums) => ({
  type: GET_ALL_ALBUMS,
  payload: albums,
});

export const getAllAlbums = () => async (dispatch) => {
  const res = await fetch("/api/albums");

  if (res.ok) {
    const final = await res.json();
    dispatch(getAlbums2(final));
  } else {
    const error = await res.json();
    return error;
  }
};

export const getAlbums = () => async (dispatch) => {
  dispatch(getAlbumsRequest());
  try {
    const response = await fetch(`/api/albums/`, {
      credentials: "include",
    });
    if (!response.ok) {
      throw new Error("Failed to fetch albums");
    }
    const data = await response.json();
    dispatch(getAlbumsSuccess(data.albums));
  } catch (error) {
    dispatch(getAlbumsFailure(error.message));
  }
};

const initialState = {
  loading: false,
  error: null,
  albums: [],
};

const albumsReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_ALL_ALBUMS: {
      return { ...state, ...action.payload };
    }
    case GET_ALBUMS_REQUEST:
      return {
        ...state,
        loading: true,
        error: null,
      };
    case GET_ALBUMS_SUCCESS:
      return {
        ...state,
        loading: false,
        albums: action.payload,
      };
    case GET_ALBUMS_FAILURE:
      return {
        ...state,
        loading: false,
        error: action.payload,
      };
    default:
      return state;
  }
};

export default albumsReducer;
