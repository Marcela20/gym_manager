import React, { Component } from "react";
import { Table } from "reactstrap";
import NewGroupModal from "./NewGroupModal";
import { API_INSTRUCTOR_URL } from ".";
import ConfirmRemovalGroup from "./ConfirmRemovalGroup";
import axios from "axios";

class GroupList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      instructors: {}
    };
  };
  componentDidMount() {
    this.getInstructors();
  }
  getInstructors = () => {
    const createDict = (data) => {
      const dict_with_instructors = {}
      for (const [i, inst] of data.entries()) {
        dict_with_instructors[inst.pk] = `${inst.name} ${inst.second_name}`
      }; this.setState({instructors:dict_with_instructors})
    }
    axios.get(`${API_INSTRUCTOR_URL}`).then(res => {createDict(res.data)});
  };

  render() {
    const groups = this.props.groups;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Name</th>
            <th>Instructor</th>
            <th>Level</th>
            <th>Limit</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!groups || groups.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            groups.map(group => (
              <tr key={group.pk}>
                <td>{group.name}</td>
                <td>{this.state.instructors[group.instructor]}</td>
                <td>{group.level}</td>
                <td>{group.limit}</td>

                <td align="center">
                  <NewGroupModal
                    create={false}
                    group={group}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalGroup
                    pk={group.pk}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default GroupList;