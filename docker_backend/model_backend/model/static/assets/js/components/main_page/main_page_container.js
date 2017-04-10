import React from 'react';
import { connect } from 'react-redux';
import MainPage from './main_page';

const mapStateToProps = (state) => ({
  loading: state.loading
});

const mapDispatchToProps = dispatch => ({

});

export default connect(mapStateToProps, mapDispatchToProps)(MainPage);
