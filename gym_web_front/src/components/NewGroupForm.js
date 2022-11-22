import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import {API_GROUP_URL } from ".";

class NewGroupForm extends React.Component {
  state = {
    pk: 0,
    name: "",
    time: "",
    instructor: "",
  };

  componentDidMount() {
    if (this.props.NewGroupForm) {
      const {   pk, name, members, instructor, time } = this.props.NewGroupForm;
      this.setState({ pk, name, members, instructor, time });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createNewGroupForm = e => {
    e.preventDefault();
    axios.post(API_GROUP_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editNewGroupForm = e => {
    e.preventDefault();
    axios.put(API_GROUP_URL + this.state.pk, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.NewGroupForm ? this.editNewGroupForm : this.createNewGroupForm}>
        <FormGroup>
          <Label for="name">Name:</Label>
          <Input
            type="text"
            name="name"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.name)}
          />
        </FormGroup>

        <FormGroup>
          <Label for="time">Time:</Label>
          <Input
            name="time"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.time)}
          />
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewGroupForm;