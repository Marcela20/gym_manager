import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import {API_INSTRUCTOR_URL } from ".";

class NewInstructorForm extends React.Component {
  state = {
    pk: 0,
    name: "",
    email: "",
    second_name: "",
    phone: ""
  };

  componentDidMount() {
    if (this.props.NewInstructorForm) {
      const { pk, name, document, email, phone } = this.props.NewInstructorForm;
      this.setState({ pk, name, document, email, phone });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createNewInstructorForm = e => {
    e.preventDefault();
    axios.post(API_INSTRUCTOR_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editNewInstructorForm = e => {
    e.preventDefault();
    axios.put(API_INSTRUCTOR_URL + this.state.pk, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.NewInstructorForm ? this.editNewInstructorForm : this.createNewInstructorForm}>
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
          <Label for="second_name">Second Name:</Label>
          <Input
            type="text"
            name="second_name"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.second_name)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="email">Email:</Label>
          <Input
            type="email"
            name="email"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.email)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="phone">Phone:</Label>
          <Input
            type="text"
            name="phone"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.phone)}
          />
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewInstructorForm;