import React from 'react';
import ResultsChart from './results_chart';

class Results extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    let chart;
    if (this.props.results.classification) {
      chart = <ResultsChart results={this.props.results}/>
    }
    console.log(this.props.currentTrack);
    return(
      <div className='results-wrapper'>
        <div className='results-title'>Results</div>
        <div className='results-chart-wrapper'>
          {chart}
        </div>

      </div>
    )
  }
}

export default Results;
