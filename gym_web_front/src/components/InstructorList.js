import React, { Component } from "react";
import { Table } from "reactstrap";
import NewInstructorModal from "./NewInstructorModal";

import ConfirmRemovalInstructor from "./ConfirmRemovalInstructor";

class InstructorList extends Component {
  render() {
    const instructors = this.props.instructors;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Second name</th>
            <th>Phone</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!instructors || instructors.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            instructors.map(instructor => (
              <tr key={instructor.pk}>
                <td>{instructor.name}</td>
                <td>{instructor.email}</td>
                <td>{instructor.second_name}</td>
                <td>{instructor.phone}</td>
                <td align="center">
                  <NewInstructorModal
                    create={false}
                    instructor={instructor}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalInstructor
                    pk={instructor.pk}
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

export default InstructorList;