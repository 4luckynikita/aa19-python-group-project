const GET_MUSICIANS = "musicians/getMusicians";
const GET_MUSICIAN = "musician/getMusician";

const getMusicians = (musicians) => ({
  type: GET_MUSICIANS,
  payload: musicians,
});
const getMusician = (musician) => ({
  type: GET_MUSICIAN,
  payload: musician,
});

export const fetchMusicians = () => async (dispatch) => {
  const response = await fetch("/api/users/musicians");
  if (response.ok) {
    const data = await response.json();
    dispatch(getMusicians(data.users));
  }
};
export const fetchCurrentMusician = (id) => async (dispatch) => {
  const response = await fetch(`/api/users/${id}`);
  if (response.ok) {
    const musician = await response.json();
    dispatch(getMusician(musician));
  }
};

const initialState = { musician: null };
function musicianReducer(state = initialState, action) {
  switch (action.type) {
    case GET_MUSICIANS:
      return { ...state, musicians: action.payload };
    case GET_MUSICIAN:
      return { ...state, musician: action.payload };
    default:
      return state;
  }
}

export default musicianReducer;
