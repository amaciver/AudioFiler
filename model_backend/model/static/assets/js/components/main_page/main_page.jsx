import React from 'react';
import Header from './header';
import GraphicsContainer from '../graphics/graphics_container';
import SearchContainer from '../search/search_container';
import Animation from '../animation/animation';
import ResultsContainer from '../results/results_container';
import About from '../about/about';
import Modal from 'react-modal';
// import Howler from './player';

const aboutStyles = {
  content : {
    top                   : '50%',
    left                  : '50%',
    right                 : 'auto',
    bottom                : 'auto',
    marginRight           : '-50%',
    transform             : 'translate(-50%, -50%)'
  }
};

class MainPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {modalIsOpen: false};
    this.openModal = this.openModal.bind(this);
    this.closeModal = this.closeModal.bind(this);
  }

  componentWillMount() {
    Modal.setAppElement('body');
  }

  openModal() {
    this.setState({modalIsOpen: true});
  }

  closeModal() {
    this.setState({modalIsOpen: false})
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
              <Animation loading={this.props.loading}/>
            </div>
            <div className='col-1-3 right-pane'>
              <ResultsContainer />
            </div>
          </div>
        </div>

        <div className='footer-wrapper'>
          <div onClick={this.openModal} className='bottom-tab'>
            <h2>About</h2>
          </div>
        </div>
        <Modal
              isOpen={this.state.modalIsOpen}
              onRequestClose={this.closeModal}
              contentLabel='About Modal'
              style={aboutStyles}
              >
              <About closeModal={this.closeModal} />

            </Modal>
      </div>
    )
  }
}

export default MainPage;
