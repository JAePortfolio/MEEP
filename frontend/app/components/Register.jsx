import axios from 'axios';
import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import { API_BASE_URL } from '../Config';

class Register extends React.Component {
  state = { "message" : null,
            register : false,
            redirect : false}

  handleSubmit = (e) => {
    // Prevents default behavior of refreshing the page
    e.preventDefault();

    // Data passed to the server.
    let submitData = {
      username: e.target[0].value,
      password: e.target[1].value,
    }

    axios.post(API_BASE_URL + '/register', submitData)
    .then(response => {
      saveLocal("user", response.data);

      // Redirect to "/"
      this.props.history.push('/');
    })
    .catch(error => {
      // handle error
      console.error("register error", error);
      this.setState(error.response.data);
    });
  }

  setRedirect = () => {
    this.setState({
      redirect: true
    })
  }
  renderRedirect = () => {
    if (this.state.redirect) {
      return <Redirect to='/' />
    }
  }

  render() {
    console.log(this.props);

    return (
      <div>
        <div className="header" style={{display: "inline-block", marginRight: "40px"}}>
          {this.renderRedirect()}
          <img src="/images/logo.png" onClick={this.setRedirect}/>
        </div>
        <div>
          <h2>Regististration for New Users</h2>
          <hr />
          <div>
            {this.state.message}
          </div>
          <form onSubmit={ this.handleSubmit }>
            <label htmlFor="username">Username</label><br />
            <input type="text" name="username" /><br />

            <label htmlFor="password">Pass</label><br />
            <input type="password" name="password" /><br />

            <button type="submit">Submit</button>
          </form>
        </div>
      </div>
    )
  }
}

export default Register;
