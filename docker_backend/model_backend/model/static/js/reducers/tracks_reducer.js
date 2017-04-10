import { RECEIVE_TRACKS, CLEAR_TRACKS } from '../actions/tracks_actions';
import merge from 'lodash/merge';

const TracksReducer = (state = {}, action) => {
  Object.freeze(state)
  let newState = merge({}, state);

  switch(action.type) {
    case RECEIVE_TRACKS:
      return action.tracks;
    case CLEAR_TRACKS:
      return action.tracks;
    default:
      return state;
  }
};

export default TracksReducer;
