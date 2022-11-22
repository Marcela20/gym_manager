import React, { Component } from "react";
import { Table } from "reactstrap";
import NewGroupModal from "./NewGroupModal";

import ConfirmRemovalGroup from "./ConfirmRemovalGroup";

class GroupList extends Component {
  render() {
    const groups = this.props.groups;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Name</th>
            <th>Time</th>

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
                <td>{group.time}</td>

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