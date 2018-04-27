import React, { Component } from "react";
import PropTypes from "prop-types";
import CommentBox from "./presenter";

class Container extends Component {
  state = {
    comment: ""
  };
  static propTypes = {
    photoId: PropTypes.number.isRequired,
  };
  render() {
    return (
      <CommentBox
        {...this.state}
      />
    );
  }
}

export default Container;