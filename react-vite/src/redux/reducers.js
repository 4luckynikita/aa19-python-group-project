import { combineReducers } from "redux";
import sessionReducer from "./session";
import usersReducer from "./users";
import albumsReducer from "./albums";
import musicianReducer from "./musicians";

const rootReducer = combineReducers({
  session: sessionReducer,
  users: usersReducer,
  albums: albumsReducer,
  musician: musicianReducer,
});

export default rootReducer;
