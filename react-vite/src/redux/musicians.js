const GET_MUSICIAN = "musician/getMusician";

const getMusician = (musician) => ({
  type: GET_MUSICIAN,
  payload: musician,
});

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
    case GET_MUSICIAN:
      return { ...state, musician: action.payload };
    default:
      return state;
  }
}

export default musicianReducer;
