import React, { Component } from 'react';

class EditorTitle extends React.Component {
  state = {
    editingTitle: false
  }

  changeTitle = (e) => {
    e.preventDefault();
    console.log("changing title...", e.target[0].value);
    this.props.setTitle(e.target[0].value);
    this.setState({ editingTitle : false });
  }

  clickTitle = (e) => {
    this.setState({editingTitle: true });
  }

  render() {
    var title = this.props.title;

    let outputTitle = this.state.editingTitle
    ?
    (
      <form onSubmit={this.changeTitle}>
        <input id="title-rename" type="text" name="title" defaultValue={title} />
      </form>
    )
    :
    (
      <h1 onClick={ this.clickTitle }>{ title }</h1>
    )

    if (this.state.editingTitle) {
      window.document.getElementById("title-rename").focus();
    };

    return (
      <div>{outputTitle}</div>
    )
  }
}

export default EditorTitle;
