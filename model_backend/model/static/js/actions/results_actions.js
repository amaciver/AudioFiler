import * as APIUtil from '../util/results_api_util';

export const RECEIVE_RESULTS = "RECEIVE_RESULTS";
export const CLEAR_RESULTS = "CLEAR_RESULTS";
export const START_LOADING_RESULTS = "START_LOADING_RESULTS";


export const receiveResults = results => ({
  type: RECEIVE_RESULTS,
  results
});

export const clearResults = results => ({
  type: CLEAR_RESULTS,
  results
})

export const startLoadingResults = () => ({
	type: START_LOADING_RESULTS
});


export const fetchResults = (url_string) => dispatch => {
  dispatch(startLoadingResults());
  return (
    APIUtil.fetchResults(url_string)
    .then(results => dispatch(receiveResults(results)))
  );
}
