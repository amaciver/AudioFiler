import React from 'react';
import { Provider } from 'react-redux';
import { Router, Route, IndexRoute, hashHistory } from 'react-router';
import App from './app';
import MainPageContainer from './main_page/main_page_container.js'

const Root = ({ store }) => {

  return (
    <Provider store={ store }>
      <App />
    </Provider>
  );
}

export default Root;



// <Provider store={ store }>
//   <Router history={ hashHistory }>
//     <Route path="/" component={ App }>
//       <IndexRoute component={MainPageContainer} />
//     </Route>
//   </Router>
// </Provider>
