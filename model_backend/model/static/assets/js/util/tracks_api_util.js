import 'jquery'

export const fetchTracks = (query_string) => {

  return $.ajax({
    method: 'GET',
    url: `https://api.spotify.com/v1/search?q=track:${query_string}&type=track`
  });
};
