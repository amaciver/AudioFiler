import { RECEIVE_TOKEN } from '../actions/token_actions';
import merge from 'lodash/merge';

const TokenReducer = (state = {}, action) => {
  Object.freeze(state)
  let newState = merge({}, state);

  switch(action.type) {
    case RECEIVE_TOKEN:
      return action.token;
    default:
      return state;
  }
};

export default TokenReducer;
