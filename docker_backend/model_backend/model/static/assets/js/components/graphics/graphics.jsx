import React from 'react';

class Graphics extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return(
      <div className='graphics-wrapper'>
        <div className='subtitle-wrapper'>
          <div className='subtitle-content'>
            Machine Learning Song Classifier
          </div>

        </div>
        <div className='graphics-background'>
          <img className='background-graphic' src='http://res.cloudinary.com/couchsmurfing/image/upload/v1491594643/neural-background_nx9aup.jpg'/>
        </div>
      </div>
    )
  }
}

export default Graphics;
