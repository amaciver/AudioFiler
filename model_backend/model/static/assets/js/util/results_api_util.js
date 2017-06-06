export const fetchResults = (url_string) => {
  // console.log(url_string);
  return $.ajax({
    method: 'GET',
    url: `/main/api/${url_string}`
  });
};
