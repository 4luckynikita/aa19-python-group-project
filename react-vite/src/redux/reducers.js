import { combineReducers } from 'redux';
import sessionReducer from './session';
import usersReducer from './users';

const rootReducer = combineReducers({
  session: sessionReducer,
  users: usersReducer,
});

export default rootReducer;
