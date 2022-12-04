import React, { Component } from 'react';

import {
  Col,
  Row,
  Container
} from 'reactstrap';
import GetRestObject from './ConnectServerGet';
import "../index.css";
import XTable from "./TableComponent/Table";



class CsvDataReader extends Component {
    constructor(props) {
      super(props);

      this.state = {
          csvDataObject:[]
      };
    }

    HelloGetRequestedDetails = () => {
      GetRestObject.GetRestRequest(`http://127.0.0.1:8000/api/calendar/?group=2`, getResultObj => {
          this.setState({
            csvDataObject:getResultObj
          })
      });
    }

    renderColumnNames = (colmunList) => {
        return(

            colmunList.map( (item, index) => {
                return(
                    <span key={index} className="mr-1 text-default">{index+1}: {item}</span>
                )
            })
        )
    }

    renderCsvDataResults = () => {
        if (this.state.csvDataObject.length > 0 ){
            var apiData = this.state.csvDataObject;

            apiData = apiData[0];

                return(
                    <div className="App">
                    <Container className="themed-container" >
                      <div>
                        <XTable columns={apiData.columns} loading={false} data={apiData.rowData} />
                      </div>
                    </Container>
                  </div>
                )
            }
         }

    componentDidMount(){
      this.HelloGetRequestedDetails();

    }

    loading = () => <div className="animated fadeIn pt-1 text-center">Loading...</div>

    render() {
      return (
        <div className="animated fadeIn">
        <Container className="themed-container" >
            <Row>
            <Col md={12}>
              <hr/>
              {this.renderCsvDataResults()}
            </Col>

            </Row>
          </Container>
        </div>
    );
  }
}

export default CsvDataReader;

