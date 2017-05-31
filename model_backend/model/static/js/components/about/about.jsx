import React from 'react';

const About = () => {
  return(
    <h2>You select a song, AudioFiler sends off a request to Spotify
        to grab a 30 second preview of the song you chose. The song is then
        sent to our backend and analyzed to produce a 70 dimensional vector
        with all sorts of data on the song, ranging from spectral analysis
        to bpm to intensity. Our backend then runs that vector through 20
        separately trained Random Forest models, and each one votes on which genre it thinks
        that your song is. Once that's finished, the top results are returned to
        you, sorted by which genres received the most votes.</h2>
    );
};

export default About;
