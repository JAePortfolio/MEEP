import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import { API_BASE_URL } from '../Config';

class DocumentDirectory extends React.Component {
  state = {
    docs: null
  }

  componentDidMount() {
    axios.get(API_BASE_URL + "/docs").then(response => {
      console.log(response);
      this.setState({docs: response.data});
    })
  }

  render() {
    var { docs } = this.state;
    var items = docs ? docs.map(doc => {
      return (
        <li key={doc.doc_id}>
          <Link to={"/docs/" + doc.doc_id }>
            <b>{doc.title}</b><br />
          </Link>
          <em>{doc.owner}</em>
        </li>
      );
    })
    : "No documents found";

    return (
      <div>
        <h1>Doc Directory</h1>
        <ul>
        { items }
        </ul>
      </div>
    )
  }
}

export default DocumentDirectory;
