import React, { Component } from 'react';
import patils from './patil.jpg'

function convertStrings(string){
	var sum = 0
	for(var i = 0; i < string.length; ++i){
		sum += string.charCodeAt(i);
	}
	return sum
}

export default class Patils extends Component {
	constructor(props){
		super(props)
		this.state = {
			value: '',
			gottem: false
		}
		this.handleChange = this.handleChange.bind(this)
		this.handleSubmit = this.handleSubmit.bind(this)
	}
	handleChange(event){
		this.setState({value: event.target.value.toLowerCase()})
	}
	handleSubmit(event){
		event.preventDefault()
		console.log(convertStrings(this.state.value))
		if(convertStrings(this.state.value) === 8000){
			this.setState({gottem: true})
		}
	}
  render() {
	  let found = null
	  if(this.state.gottem){
		  found = <center><h1>utflag&#123;blockchain_is_bae&#125;</h1></center>
	  }
	  else{
		  found = <center>
		  <form onSubmit={this.handleSubmit}>
			  <label>
				Code:
				<input type="text" value={this.state.value} onChange={this.handleChange} />
			  </label>
			  <br />
			  <br />
			  <input type="submit" value="Submit" />
			</form>
			</center>
	  }
    return (
      <div className="App">
	  	  <img src= {patils}/>
          <h1>Welcome to the PREMIER Patil Delivery Service (PPDS)</h1>
		  <h3>We are pleased to announce our new blockchain based Patil Delivery Service at BlockDev Conference 2018</h3>
		  <h4>Please enter your promo code here:</h4>
		  {found}
		  <h4>We tried to give a bunch of codes to Praetorian, since they seemed to be interested in investing in our venture, but Neil gave our codes to Facebook, because he wanted to go to Menlo Park, since Austin was too boring for him, even though what they offered was exactly what we wanted</h4>
      </div>
    );
  }
}
