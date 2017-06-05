import * as APIUtil from '../util/tracks_api_util';

export const RECEIVE_TRACKS = "RECEIVE_TRACKS";
export const RECEIVE_TRACK = "RECEIVE_TRACK";
export const CLEAR_TRACKS = "CLEAR_TRACKS";
export const CLEAR_TRACK = "CLEAR_TRACK";
// export const START_LOADING_TRACK = "START_LOADING_TRACK";
// export const START_LOADING_TRACKS = "START_LOADING_TRACKS";


export const receiveTracks = tracks => ({
  type: RECEIVE_TRACKS,
  tracks
});

export const receiveTrack = track => ({
  type: RECEIVE_TRACK,
  track
});

export const clearTracks = tracks => ({
  type: CLEAR_TRACKS,
  tracks
});

export const clearTrack = track => ({
  type: CLEAR_TRACK,
  track
});



export const fetchTracks = (query_string, token) => dispatch => {
  // dispatch(startLoadingTracks());
  console.log(token);
  return (
    APIUtil.fetchTracks(query_string, token)
    .then(tracks => dispatch(receiveTracks(tracks)))
  );
}

// export const fetchTrack = id => dispatch => {
//   // dispatch(startLoadingTrack());
//   return (
//     APIUtil.fetchTrack(id)
//       .then(track => dispatch(receiveTrack(track)))
//   );
// }
