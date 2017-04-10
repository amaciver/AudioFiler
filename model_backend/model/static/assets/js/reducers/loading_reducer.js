import { RECEIVE_RESULTS,
    START_LOADING_RESULTS
  } from '../actions/results_actions';

const initialState = false;

export default (state = initialState, action) => {
  Object.freeze(state);
  switch(action.type){
    case RECEIVE_RESULTS:
      return initialState;
    case START_LOADING_RESULTS:
      return true;
    default:
      return state;
  }
};
