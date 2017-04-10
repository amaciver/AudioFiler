import React from 'react';

const Row = ({genre, confidence}) => (
  <tr>
    <td>{genre}</td>
    <td>{confidence*100}%</td>
  </tr>
);

export default Row;
