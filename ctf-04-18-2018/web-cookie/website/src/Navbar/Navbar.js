/* eslint-disable no-unused-vars */
import React, {Component} from 'react'
import {Navbar, Nav, NavItem, Button, FormGroup, FormControl} from 'react-bootstrap'
import {LinkContainer} from 'react-router-bootstrap'
import {Link} from 'react-router-dom'
/* eslint-enable no-unused-vars */
import header from '../Splash/neil.jpeg'


export default class Navigation extends Component {
  render () {
    return (
		<Navbar inverse collapseOnSelect>
	  <Navbar.Header>
	    <Navbar.Brand>
	      <a href="/">Neil&#39;s Patils</a>
	    </Navbar.Brand>
	    <Navbar.Toggle />
	  </Navbar.Header>
	  <Navbar.Collapse>
	    <Nav>
	      <NavItem eventKey={1} href="/cookies">
	        Cookies!
	      </NavItem>
	      <NavItem eventKey={2} href="/patils">
	        Patils
	      </NavItem>
	    </Nav>
	  </Navbar.Collapse>
	</Navbar>
	);
  }
}
