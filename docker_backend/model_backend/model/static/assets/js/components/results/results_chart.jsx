import React from 'react';
import Row from './row';


class ResultsChart extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    let entries = [];
    let results = this.props.results.classification;
    if (results) {
      entries = Object.keys(results).map( (key) => {
        return (
          <Row key={key} genre={results[key][0]} confidence={results[key][1]} />
        );
      });
    }

    let track = this.props.currentTrack;

    return (
      <div className='results-chart'>
        <div className='results-chart-header'>
          {track.track} by {track.artist} sounds like:
        </div>
        <div className='results-chart-list'>
          <table>
            <tbody>
              <tr>
                <th>Genre</th>
                <th>Confidence</th>
              </tr>
              {entries}
            </tbody>
          </table>

        </div>
      </div>
    )
  }
}

export default ResultsChart;
