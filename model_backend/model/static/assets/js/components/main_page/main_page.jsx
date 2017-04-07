import React from 'react';
import Header from './header';
import GraphicsContainer from '../graphics/graphics_container';
import SearchContainer from '../search/search_container';
import Animation from '../animation/animation';
import ResultsContainer from '../results/results';
import About from '../about/about';

class MainPage extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return(
      <div>
        <h1>
          Main Page, Jerk.
        </h1>
        <Header />
        <GraphicsContainer />
        <SearchContainer />
        <Animation />
        <ResultsContainer />
        <About />
      </div>
    )
  }
}

export default MainPage;
