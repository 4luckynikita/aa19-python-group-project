const GET_ALBUMS_REQUEST = "albums/GET_ALBUMS_REQUEST";
const GET_ALBUMS_SUCCESS = "albums/GET_ALBUMS_SUCCESS";
const GET_ALBUMS_FAILURE = "albums/GET_ALBUMS_FAILURE";
const GET_ALL_ALBUMS = "albumsReducer/GET_ALL_ALBUMS";
const GET_ALBUMS = "album/getAlbums";
const CREATE_ALBUM = "album/newAlbum";
const GET_CURRENT_ALBUM = "album/current";

const getCurrentAlbum = (album) => ({
  type: GET_CURRENT_ALBUM,
  payload: album,
});

const createAlbum = (album) => ({
  type: CREATE_ALBUM,
  payload: album,
});

export const createAnAlbum = (formData) => async (dispatch) => {
  // //console.log(JSON.stringify(formData))
  const response = await fetch(`/api/albums/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formData),
  });
  if (response.ok) {
    const data = getAllAlbums();
    const newAlbum = await response.json();
    dispatch(getAlbums2(data));
    dispatch(createAlbum(newAlbum));
    return newAlbum;
  } else if (response.status < 500) {
    const errorMessages = await response.json();
    return errorMessages;
  } else {
    return { server: "Something went wrong. Please try again" };
  }
};

export const CreateSong = (formData, id) => async (dispatch) => {
  // //console.log(JSON.stringify(formData))
  const response = await fetch(`/api/songs/albums/${id}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formData),
  });
  if (response.ok) {
    const data = getAllAlbums();
    const newAlbum = await response.json();
    dispatch(getAlbums2(data));
    return newAlbum;
  } else if (response.status < 500) {
    const errorMessages = await response.json();
    return errorMessages;
  } else {
    return { server: "Something went wrong. Please try again" };
  }
};

export const deleteAlbum = (id) => async () => {
  const res = await fetch(`/api/albums/${id}`, {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
  });
  const deleted = await res.json();
  return deleted;
};

export const editAlbum = (id, formData) => async () => {
  try {
    const response = await fetch(`/api/albums/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });
    if (!response.ok) {
      throw new Error("Failed to update album");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    return error.message;
  }
};

export const deleteSong = (id) => async () => {
  const res = await fetch(`/api/songs/${id}`, {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
  });
  const deleted = await res.json();
  // dispatch(fetchCurrentMusician(userId));
  return deleted;
};

export const musicianAlbumsReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_ALBUMS:
      return { ...state, albums: action.payload };
    case CREATE_ALBUM:
      return { newAlbum: action.payload };
    case GET_CURRENT_ALBUM:
      return { ...state, currentAlbum: action.payload };
    default:
      return state;
  }
};

const getAlbumsRequest = () => ({ type: GET_ALBUMS_REQUEST });
const getAlbumsSuccess = (albums) => ({
  type: GET_ALBUMS_SUCCESS,
  payload: albums,
});
const getAlbumsFailure = (error) => ({
  type: GET_ALBUMS_FAILURE,
  payload: error,
});

const getAlbums3 = (albums) => ({
  type: GET_ALBUMS,
  payload: albums,
});

const getAlbums2 = (albums) => ({
  type: GET_ALL_ALBUMS,
  payload: albums,
});

export const fetchAlbums = (id) => async (dispatch) => {
  const response = await fetch(`/api/albums/musicians/${id}`);
  if (response.ok) {
    const albums = await response.json();
    dispatch(getAlbums3(albums));
    return albums;
  }
};

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

export const fetchCurrentAlbum = (albumId) => async (dispatch) => {
  //console.log("bbbbbbhiiiiiiiiiii");
  const res = await fetch(`/api/albums/${albumId}`);
  if (res.ok) {
    //console.log("hiiiiiiiiiii");
    const current = await res.json();
    dispatch(getCurrentAlbum(current));
  }
};

const initialState = {
  loading: false,
  error: null,
  albums: [],
  newAlbum: [],
  currentAlbum: [],
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
    case GET_ALBUMS:
      return { ...state, albums: action.payload };
    default:
      return state;
  }
};

export default albumsReducer;
