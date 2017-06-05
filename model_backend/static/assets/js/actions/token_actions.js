import * as APIUtil from '../util/token_api_util';

export const RECEIVE_TOKEN = "RECEIVE_TOKEN";


export const receiveToken = token => ({
  type: RECEIVE_TOKEN,
  token
});


export const fetchToken = () => dispatch => {
  return (
    APIUtil.fetchToken()
    .then(token => dispatch(receiveToken(token)))
  );
}
