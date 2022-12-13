import React, { Component, useState, useEffect } from 'react';
import { useTable } from 'react-table'
import useFetchData from './use-fetch-data.js'

function Table() {
    const {
        raw_data,
        loading,
    } = useFetchData();
    
    const [data, setData] = useState([]);
    const [columns, setColumns] = useState([]);
    

    useEffect(() => {
        if (raw_data) {
            
            setData(raw_data[0].rowData)
            setColumns(raw_data[0].columns)
        }
      }, [loading]);

   const {

     getTableProps,

     getTableBodyProps,

     headerGroups,

     rows,

     prepareRow,

   } = useTable({ columns, data })

   return (

     <table {...getTableProps()} style={{ border: 'solid 1px blue' }}>

       <thead>

         {headerGroups.map(headerGroup => (

           <tr {...headerGroup.getHeaderGroupProps()}>

             {headerGroup.headers.map(column => (
                 

                 <th
                     className={column.render('subgroup')}

                 {...column.getHeaderProps()}

                 style={{

                   borderBottom: 'solid 3px red',

                   background: 'aliceblue',

                   color: 'black',

                   fontWeight: 'bold',

                 }}

               >

                 {column.render('Header')}

               </th>

             ))}

           </tr>

         ))}

       </thead>

       <tbody {...getTableBodyProps()}>

         {rows.map(row => {

           prepareRow(row)

           return (

             <tr {...row.getRowProps()}>

                   {row.cells.map(cell => {

                 return (

                   <td

                     {...cell.getCellProps()}

                     style={{

                       padding: '10px',

                       border: 'solid 1px gray',

                       background: 'papayawhip',

                     }}

                   >

                     {cell.render('Cell')}

                   </td>

                 )

               })}

             </tr>

           )

         })}

       </tbody>

     </table>

   )

 }
 export default Table;
