export const fetchResults = (url_string) => {
  return $.ajax({
    method: 'GET',
    url: '',
    data: {url_string}
  });
};
