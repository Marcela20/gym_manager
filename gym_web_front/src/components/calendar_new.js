import React from 'react';
import { Container } from "reactstrap";
import Scheduler, { Resource} from 'devextreme-react/scheduler';

import {API_CALENDAR, API_NEW_CALENDAR, API_GROUP_URL} from ".";
import notify from 'devextreme/ui/notify';
import 'whatwg-fetch';
import CustomStore from 'devextreme/data/custom_store';
import axios from "axios";
const url_get =API_NEW_CALENDAR;
const url_post =API_CALENDAR;

function handleErrors(response) {
  if (!response.ok) {
      throw Error(response.statusText);
  }
  return response;
}
const DataSource = new CustomStore({
  key: 'AttributeId',
   load: () => {
      return fetch(url_get)
          .then(handleErrors)
          .then(response => response.json())
  },
  insert: (values) => {
    return fetch(url_post, {
        method: 'POST',
        body: JSON.stringify(values),
        headers:{
            'Content-Type': 'application/json'
        }
    })
    .then(handleErrors)
    .catch(() => { throw 'Network error' });
},
remove: (key) => {
  return fetch(`${url_post}${encodeURIComponent(key)}`, {
      method: 'DELETE'
  })
  .then(handleErrors)
  .catch(() => { throw 'Network error' });
},
update: (key, values) => {
  return fetch(`${url_post}${encodeURIComponent(key)}`, {
      method: 'PUT',
      body: JSON.stringify(values),
      headers:{
          'Content-Type': 'application/json'
      }
  })
  .then(handleErrors)
  .catch(() => { throw 'Network error' });
}
});
const views = ['day', 'workWeek', 'week', 'month', 'timelineDay'];

class Calendar extends React.Component {

  constructor(props) {

    super(props);
    this.state = {
      allowAdding: true,
      allowDeleting: true,
      allowResizing: true,
      allowDragging: false,
      allowUpdating: true,
      groups: [],

    };
    this.showAddedToast = this.showAddedToast.bind(this);
    this.showUpdatedToast = this.showUpdatedToast.bind(this);
    this.showDeletedToast = this.showDeletedToast.bind(this);

  }

  componentDidMount() {
    this.getGroups();
  }

  getGroups = () => {

    const createavailableOptions = (data) => {
        const groups_array = [];
          for (const [i, inst] of data.entries()) {
            groups_array.push({'id':inst.pk, 'text':`${inst.instructor} ${inst.name}`})
          };
          this.setState({groups:groups_array})
    };
    axios.get(API_GROUP_URL).then(res => {createavailableOptions(res.data) });}

  render() {
    return (

      <Container>
        <Scheduler
          dataSource={DataSource}
          views={views}
          defaultCurrentView="week"
          startDayHour={9}
          endDayHour={19}
          height={600}
          onAppointmentAdded={this.showAddedToast}
          onAppointmentUpdated={this.showUpdatedToast}
          onAppointmentDeleted={this.showDeletedToast}
          >
          <Resource
          dataSource={this.state.groups}
          label="Group"
          allowMultiple={false}
          fieldExpr="group"
          />

        </Scheduler>
      </Container>
    );
  }


  showToast(event, value, type) {
    notify(`${event} "${value}" task`, type, 800);
  }

  showAddedToast(e) {
    this.showToast('Added', e.appointmentData.text, 'success');
  }

  showUpdatedToast(e) {
    this.showToast('Updated', e.appointmentData.text, 'info');

  }

  showDeletedToast(e) {
    this.showToast('Deleted', e.appointmentData.text, 'warning');

  }
}

export default Calendar;
