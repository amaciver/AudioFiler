import { RECEIVE_RESULTS, CLEAR_RESULTS } from '../actions/results_actions';
import merge from 'lodash/merge';

const ResultsReducer = (state = {}, action) => {
  Object.freeze(state)
  let newState = merge({}, state);

  switch(action.type) {
    case RECEIVE_RESULTS:
      return action.results;
    case CLEAR_RESULTS:
      return action.track;
    default:
      return state;
  }
};

export default ResultsReducer;
