import React, {Component} from 'react';
import {withRouter} from 'react-router-dom';
import axios from 'axios';
import {API_BASE_URL} from '../Config';
import Header from './Header';
import Editor from './Editor/Editor';

class Document extends React.Component {
  state = {
    document: null
  }

  componentWillMount() {
    var { doc_id } = this.props.match.params;
    var user = getLocal('user');

    if (Number.isInteger(Number(doc_id))) {
      // GET doc from API request
      this.getDoc(doc_id);
    } else if (doc_id == "new") {
      // Create new doc and get its ID
      var payload = {
        title: "New Document",
        user_id: user.id
      }
      this.newDoc(payload);
    }
  }

  getDoc = (id) => {
    axios.get(API_BASE_URL + "/docs/" + id)
    .then( response => {
      console.log("got doc, ", response.data)
      this.setState({document: response.data})
    })
    .catch( error => {
      console.error("Document error: ", error, error.response);
    })
  }

  newDoc = (payload) => {
    console.log("newDoc activate", payload);
    axios.post(API_BASE_URL + "/docs/new", payload)
    .then( response => {
      console.log("response is ", response)
      this.props.history.push("/docs/" + response.data.doc_id);
      this.setState({ document: response.data })
    })
    .catch( error => {
      console.error("error is", error)
    })
  }

  saveDoc = (id, payload) => {
    console.log("Saving the document...");

    axios.post(API_BASE_URL + "/docs/" + id, payload)
    .then( response => {
      console.log(response.data);
    })
    .catch( error => {
      console.error("SaveDoc error", error, error.response.data);
    })
  }

  setTitle = (title) => {
    var submit = {title: title}

    axios.post(API_BASE_URL + "/docs/" + this.state.document.doc_id + "/rename", submit)
    .then( response => {
      console.log("Changing title... ", response.data.message);
    })
    .catch( error => {
      console.error("SetTitle error", error, error.response.data);
    });

    console.log("this state", this.state);

    this.setState({
      document: {
        ...this.state.document,
        title : title
      }
    });
  }

  render() {
    var {name, type, pic} = getLocal("user");
    var {document} = this.state;
    var user = getLocal('user');

    var display = document
    ? (
      <div>
        <Editor doc={document} setTitle={this.setTitle} user={user} saveDoc={this.saveDoc} />
      </div>
    )
    : <h3>Invalid Document ID</h3>;

    return (
      <div className="document">
        <Header name={name} type={type} pic={pic} />
        { display }
      </div>
    )
  }
}

export default Document;
