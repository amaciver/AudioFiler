export const fetchTracks = (query_string) => {
  return $.ajax({
    method: 'GET',
    url: 'https://api.spotify.com/v1/search?type=track',
    data: {query_string}
  });
};
