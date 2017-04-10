import React from 'react';

const Row = ({genre, confidence='10%'}) => (
  <tr>
    <td>{genre}</td>
    <td>{confidence}</td>
  </tr>
);

export default Row;
