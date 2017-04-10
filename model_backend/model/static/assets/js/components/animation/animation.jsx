import React from 'react';

class Animation extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      visible: false,
      fading: false
    };
    this.switchVisible = this.switchVisible.bind(this);
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.loading === true) {
      console.log('loading');
      this.switchVisible();
    } else if (nextProps.loading === false && this.state.visible === true) {
      console.log('done loading');
      this.switchVisible();
    }
  }

  fadein () {

  }

  fadeout() {

  }

  switchVisible() {
    if (this.state.visible === false) {
      this.setState({visible: true, fading: false}, )
    } else {
      this.setState({fading: true}, () => {
        setTimeout(() => {
          this.setState({visible: false});
          this.setState({fading: false});
        }, 3000)
      })
    }
  }

  render() {

    let fadeClass = ""
    if (this.state.visible === false) {
      fadeClass = 'animation-wrapper hidden';
    }
    if (this.state.visible === true) {
      fadeClass = 'animation-wrapper';
    }
    if (this.state.fading === true) {
      fadeClass = 'animation-wrapper fade-out';
    }
    return(
      <div>

        <div className={fadeClass}>
          <div className='animation-title'>Working...</div>
          <div className='brain-wrapper'>
            <div id='circuit-brain'></div>
          </div>
        </div>
      </div>
    )
  }
}

export default Animation;

// <button onClick={this.switchVisible}>switch</button>
// <div className='brain-wrapper'>
//   <img className='brain' src='http://res.cloudinary.com/couchsmurfing/image/upload/v1491690862/brain-gear_yx26tx.png' />
// </div>

// <div id='loading-brain'></div>
