import React from 'react';

class Graphics extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return(
      <div className='graphics-wrapper'>
        <div className='graphics-background'>
          <img className='background-graphic' src='http://res.cloudinary.com/couchsmurfing/image/upload/v1491594643/neural-background_nx9aup.jpg'/>
        </div>
        <h2>Graphics</h2>
      </div>
    )
  }
}

export default Graphics;
