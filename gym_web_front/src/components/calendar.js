// import * as React from 'react';
// import Paper from '@mui/material/Paper';
// import { ViewState, EditingState } from '@devexpress/dx-react-scheduler';
// import {
//   Scheduler,
//   DayView,
//   WeekView,
//   Appointments,
//   DateNavigator,
//   Toolbar,
//   ViewSwitcher,
//   MonthView,
//   AppointmentTooltip,
//   EditRecurrenceMenu,
//   AppointmentForm
// } from '@devexpress/dx-react-scheduler-material-ui';
// import { API_FORM_DAYS, API_GROUP_URL, API_CALENDAR } from ".";

// import axios from "axios";
// import {useState, useEffect} from 'react';
// // import { appointments } from './demo-data/month-appointments';


// const Select = (props) => {
//   // eslint-disable-next-line react/destructuring-assignment
//   return <AppointmentForm.Select {...props} />;
// };

// function getGroups() {
//   const [AvailableGroups, setAvailableGroups] = useState([]);
//   const createavailableOptions = (data) => {
//     const groups_array = []

//     for (const [i, inst] of data.entries()) {
//       groups_array.push({'id':inst.pk, 'text':`${inst.instructor} ${inst.name}`})
//     };
//     setAvailableGroups(groups_array);
//   }
//   useEffect(() => {
//     const expensesListResp = async () => {
//       await axios.get(API_GROUP_URL)
//       .then(
//         response => {setAvailableGroups(response.data); createavailableOptions(response.data);})

//     }
//     expensesListResp();

//   }, []);

//   return AvailableGroups
// }

// const BasicLayout = ({ onFieldChange, appointmentData, ...restProps }) => {
//   const onCustomFieldChange = (nextValue) => {
//     onFieldChange({ group: nextValue });
//   };

//   return (
//     <AppointmentForm.BasicLayout
//       appointmentData={appointmentData}
//       onFieldChange={onFieldChange}
//       {...restProps}
//     >
//       <AppointmentForm.Label
//         text="Group"
//         type="title"
//       />
//       <AppointmentForm.Select
//         value={appointmentData.group}
//         availableOptions={getGroups()}
//         onValueChange={onCustomFieldChange}
//       />
//     </AppointmentForm.BasicLayout>
//   );
// };


//   export default class Calendar extends React.PureComponent {

//     constructor(props) {
//       super(props);
//       this.state = {
//         data: [],
//         addedAppointment: {},
//         appointmentChanges: {},
//         editingAppointment: undefined,
//       };

//       this.commitChanges = this.commitChanges.bind(this);
//       this.changeAddedAppointment = this.changeAddedAppointment.bind(this);
//       this.changeAppointmentChanges = this.changeAppointmentChanges.bind(this);
//       this.changeEditingAppointment = this.changeEditingAppointment.bind(this);


//     }
//     changeAddedAppointment(addedAppointment) {
//       this.setState({ addedAppointment });
//     }

//     changeAppointmentChanges(appointmentChanges) {
//       this.setState({ appointmentChanges });
//     }

//     changeEditingAppointment(editingAppointment) {
//       this.setState({ editingAppointment });
//     }


//     componentDidMount() {
//       this.getDates();

//     }
//     getDates = () => {
//       axios.get(API_CALENDAR).then(res => this.setState({ data: res.data }));
//     };



//     commitChanges({ added, changed, deleted }) {

//         this.setState((state) => {
//         let { data } = state;
//         if (added) {

//           const response = async () => {await axios.post(API_CALENDAR, this.state.addedAppointment)}
//           const startingAddedId = data.length > 0 ? data[data.length - 1].id + 1 : 0;
//           data = [...data, { id: startingAddedId, ...added }];
//           response()
//         }
//         if (changed) {
//           var changed_appointment = this.state.editingAppointment
//           var to_db = this.state.appointmentChanges
//           const accumulative = {
//             ...changed_appointment,
//             ...to_db
//           }

//           data = data.map(appointment => (
//             changed[appointment.id] ? { ...appointment, ...changed[appointment.id] } : appointment));
//         }

//         if (deleted !== undefined) {
//           data = data.filter(appointment => appointment.id !== deleted);
//         }

//         return { data };
//       })
//     }

//   render() {
//     const {
//       addedAppointment, appointmentChanges, editingAppointment
//     } = this.state;
//     return (
//       <Paper>
//         <Scheduler
//           data={this.state.data}
//           height={660}
//         >
//           <ViewState
//             defaultCurrentViewName="Week"
//           />

//           <DayView
//             startDayHour={6}
//             endDayHour={22}
//           />
//           <EditingState
//             onCommitChanges={this.commitChanges}
//             addedAppointment={addedAppointment}
//             onAddedAppointmentChange={this.changeAddedAppointment}
//             appointmentChanges={appointmentChanges}
//             onAppointmentChangesChange={this.changeAppointmentChanges}
//             editingAppointment={editingAppointment}
//             onEditingAppointmentChange={this.changeEditingAppointment}
//           />
//           <WeekView
//             startDayHour={6}
//             endDayHour={22}
//           />
//           <MonthView
//           />
//           <Appointments />
//           <EditRecurrenceMenu />
//           <AppointmentTooltip
//             showCloseButton
//             showOpenButton
//           />
//           <AppointmentForm
//               basicLayoutComponent={BasicLayout}
//               SelectComponent={Select}
//           />
//           <Toolbar />
//           <DateNavigator />
//           <ViewSwitcher />
//           <EditRecurrenceMenu />

//         </Scheduler>
//       </Paper>
//     );
//   }
// }
