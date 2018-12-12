import React, { Component } from 'react';
import { BrowserRouter, Route } from 'react-router-dom';

import Landing from './components/Landing';
import Register from './components/Register';
import OUapply from './components/OUapply';
import DocumentDirectory from './components/DocumentDirectory';
import Document from './components/Document';
import UserDirectory from './components/UserDirectory';
import Taboos from './components/Taboos';
import SearchUser from './components/SearchUser';
import SearchDocument from './components/SearchDocument';
import Notifications from './components/Notifications/Notifications';
import Users from './components/Users';

class App extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <div className="meep-app container">
          <Route exact path="/" component={Landing} />                 {/* Home page*/}
          <Route path="/register" component={Register} />              {/* Allow new users to register guest accounts */}
          <Route path="/apply" component={OUapply} />                  {/* Allow guest users to apply to be an ordinary user */}
          <Route exact path="/docs" component={DocumentDirectory} />   {/* Return directory of all public documents */}
          <Route path="/docs/:doc_id" component={Document} onChange={() => console.log('Entered /')} />            {/* Display the editor for a given document */}
          <Route path="/users" component={UserDirectory} />            {/* Return directory of all public users */}
          <Route path="/user/:u_id" component={Users} />  {/* Display the profile for a given user */}
          <Route path="/taboos" component={Taboos} />       {/* Display the taboo list + suggestion form */}
          <Route path="/searchUser" component={SearchUser} />       {/* Allow users to Search users, documents */}
          <Route path="/searchDocument" component={SearchDocument} />       {/* Allow users to Search users, documents */}
          <Route path="/notifs" component={Notifications} />
        </div>
      </BrowserRouter>
    )
  }
}

export default App;
