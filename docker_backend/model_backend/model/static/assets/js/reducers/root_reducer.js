import { combineReducers } from 'redux';

import LoadingReducer from './loading_reducer';
import TracksReducer from './tracks_reducer';
import TrackReducer from './track_reducer';
import ResultsReducer from './results_reducer';

const rootReducer = combineReducers({
  loading: LoadingReducer,
  tracks: TracksReducer,
  currentTrack: TrackReducer,
  results: ResultsReducer
});

export default rootReducer;
