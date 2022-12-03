import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";
import DropdownList from "react-widgets/DropdownList";
import axios from "axios";
import "react-widgets/styles.css";
import {API_GROUP_URL, API_INSTRUCTOR_URL } from ".";

class NewGroupForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      pk: 0,
      name: "",
      instructor: "",
      level: "",
      limit: "",
      instructors: []
    };
    this.getInstructors();
  };

  componentDidMount() {
    if (this.props.NewGroupForm) {

      const { pk, name, instructor, level, limit } = this.props.NewGroupForm;
      this.setState({ pk, name, instructor, level, limit });

    }
  }

  onChange = e => {
    if (e.target){
      this.setState({ [e.target.name]: e.target.value });
    }
    else{
      this.setState({instructor: e.pk})

    }
  };


  findNamesInstructors(data) {
    const instructors_names_array = []
    for (const [i, inst] of data.entries()) {
      instructors_names_array.push({'pk':inst.pk, 'name':`${inst.name} ${inst.second_name}`})
    }
    this.setState({instructors: instructors_names_array})
  }

  getInstructors = () => {
    axios.get(API_INSTRUCTOR_URL).then(res => this.findNamesInstructors(res.data));
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
          <Label for="instructor">Instructor:</Label>
            <DropdownList
                name="instructor"
                data={this.state.instructors}
                dataKey='pk'
                textField="name"
                onChange={this.onChange}
                value={this.defaultIfEmpty(this.state.instructor)}
                defaultValue={1}

          />
        </FormGroup>
        <FormGroup>
          <Label for="level">Level:</Label>
          <Input
            type="text"
            name="level"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.level)}

          />
        </FormGroup>
        <FormGroup>
          <Label for="limit">Limit:</Label>
          <Input
            type="text"
            name="limit"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.limit)}
          />
        </FormGroup>

        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewGroupForm;

