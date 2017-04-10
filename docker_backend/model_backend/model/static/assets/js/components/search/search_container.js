import React from 'react';
import { connect } from 'react-redux';
import Search from './search';
import { fetchTracks, receiveTrack } from '../../actions/tracks_actions';
import { fetchResults } from '../../actions/results_actions';

const mapStateToProps = (state) => {
  let tracks = [];
  if (state.tracks.tracks) {
    tracks = Object.keys(state.tracks.tracks.items).map( (key) => {
      return (
        {
          track: state.tracks.tracks.items[key].name,
          artist: state.tracks.tracks.items[key].artists[0].name,
          url: state.tracks.tracks.items[key].preview_url
        }
      )
    });
  }
  // console.log(tracks);
  return ({
    tracks: tracks
  });
}

const mapDispatchToProps = dispatch => ({
  fetchTracks: (query_string) => dispatch(fetchTracks(query_string)),
  fetchResults: (url_string) => dispatch(fetchResults(url_string)),
  receiveTrack: (track) => dispatch(receiveTrack(track))
});

export default connect(mapStateToProps, mapDispatchToProps)(Search);
