import React from 'react';
import { connect } from 'react-redux';
import Results from './results';

const mapStateToProps = (state) => {
  return ({
    results: state.results
  });
}

const mapDispatchToProps = dispatch => ({

});

export default connect(mapStateToProps, mapDispatchToProps)(Results);
