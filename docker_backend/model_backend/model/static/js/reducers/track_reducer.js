import { RECEIVE_TRACK, CLEAR_TRACK } from '../actions/tracks_actions';
import merge from 'lodash/merge';

const TrackReducer = (state = {}, action) => {
  Object.freeze(state)
  let newState = merge({}, state);

  switch(action.type) {
    case RECEIVE_TRACK:
      return action.track;
    case CLEAR_TRACK:
      return action.track;
    default:
      return state;
  }
};

export default TrackReducer;
