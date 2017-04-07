import React from 'react';

const Header = () => {
  return(
    <div className='header-wrapper'>
      <div className='header'>
        <div className='header-title'>
          AudioFiler
          <div className='links-wrapper'>
            <div className='links'>
              <a href="https://github.com/amaciver/AudioFiler">
                <img className="link-img" src="http://res.cloudinary.com/couchsmurfing/image/upload/v1491592922/github-logo_dutwf3.png" alt="github"/>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Header;
