export const fetchToken = () => {
  return $.ajax({
    method: 'GET',
    url: `/main/token`
  });
};
