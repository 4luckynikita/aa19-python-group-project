import { combineReducers } from "redux";
import sessionReducer from "./session";
import usersReducer from "./users";
import albumsReducer from "./albums";

const rootReducer = combineReducers({
  session: sessionReducer,
  users: usersReducer,
  albums: albumsReducer,
});

export default rootReducer;
