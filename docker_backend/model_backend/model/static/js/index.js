import React from 'react';
import ReactDOM from 'react-dom';

import configureStore from './store/store';
import Root from './components/root.jsx'



import * as TracksActions from './actions/tracks_actions';
import * as ResultsActions from './actions/results_actions';


document.addEventListener('DOMContentLoaded', () => {
  
  let store = configureStore();

  const root = document.getElementById('root');

  window.store = store;

  window.fetchTracks = TracksActions.fetchTracks;
  window.receiveTracks = TracksActions.receiveTracks;
  window.receiveTrack = TracksActions.receiveTrack;
  window.clearTracks = TracksActions.clearTracks;
  window.clearTrack = TracksActions.clearTrack;

  window.fetchResults = ResultsActions.fetchResults;
  window.receiveResults = ResultsActions.receiveResults;
  window.clearResults = ResultsActions.clearResults;
  window.startLoadingResults = ResultsActions.startLoadingResults;




  ReactDOM.render(<Root store={store} />, root);
});
