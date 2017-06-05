import 'jquery'

export const fetchTracks = (query_string, token) => {
  // console.log(token);
  return $.ajax({
    method: 'GET',
    url: `https://api.spotify.com/v1/search?q=track:${query_string}&type=track&limit=5`,
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
};
