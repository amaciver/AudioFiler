import React from 'react';
import ResultsChart from './results_chart';

class Results extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return(
      <div className='results-wrapper'>
        <div className='results-title'>Results</div>
        <div className='results-chart-wrapper'>
          <ResultsChart />
        </div>

      </div>
    )
  }
}

export default Results;
