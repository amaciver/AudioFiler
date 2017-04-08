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
      <div className='main-wrapper'>

        <Header />
        <GraphicsContainer />
        <div className='ux-wrapper'>

          <div className='instructions-wrapper'>
            <div className='instructions-content'>
              Select a song and our trained model
              will analyze it and tell you the genre it appears to be.
            </div>
          </div>

          <div className='ux-content'>
            <div className='col-1-3 left-pane'>
              <SearchContainer />
            </div>
            <div className='col-1-3 middle-pane'>
              <Animation />
            </div>
            <div className='col-1-3 right-pane'>
              <ResultsContainer />
            </div>
          </div>
        </div>

        <div className='footer-wrapper'>
          <div className='bottom-tab'>
            <About />
          </div>
        </div>
      </div>
    )
  }
}

export default MainPage;
