import React, { Component } from 'react';
import logo from './neil.jpeg';
import './App.css';
export default class Splash extends Component {
  render() {
    return (
      <div className="App">
          <img src={logo} className="App-logo" alt="logo" />
          <h1>Welcome to Neil&#39;s Patils</h1>
		  <h3>We have lots of Patils for sale!</h3>
		  <h4>and other random things? lmao.</h4>
		  <br />
      </div>
    );
  }
}
