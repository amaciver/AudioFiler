import React from 'react';
import ReactHowler from 'react-howler';

class Howler extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      mute: false
    }
    this.handleMute = this.handleMute.bind(this);
    // console.log(this.props.url);
  }

  handleMute() {
    this.setState({
      mute: !this.state.mute
    })
  }

  render() {
    let icon
    console.log(this.props.url);
    if (this.state.mute === true) {
      icon = <i className="fa fa-volume-off" onClick={this.handleMute} aria-hidden="true"></i>
    } else {
      icon = <i className="fa fa-volume-up" onClick={this.handleMute} aria-hidden="true"></i>
    }
    return (
      <div>
      </div>
    )
  }

}

export default Howler;

// {icon}
// <ReactHowler
//   src={'https://s3-us-west-1.amazonaws.com/listentothis-pro/tracks/mp3_files/000/000/004/original/Jeopardy+Theme.mp3'}
//   playing={true}
//   preload={true}
//   mute={this.state.mute}
//   volume={1.0}
//   />
