import React from 'react';

const ResultsChart = () => {
  return (
    <div className='results-chart'>
      <div className='results-chart-header'>
        Your song sounds like:
      </div>
      <div className='results-chart-list'>
        <table>
          <tr>
            <th>Genre</th>
            <th>Confidence</th>
          </tr>
          <tr>
            <td>Rock</td>
            <td>80%</td>
          </tr>
          <tr>
            <td>Metal</td>
            <td>14%</td>
          </tr>
          <tr>
            <td>Pop</td>
            <td>6%</td>
          </tr>
        </table>

      </div>
    </div>
  )
}

export default ResultsChart;
