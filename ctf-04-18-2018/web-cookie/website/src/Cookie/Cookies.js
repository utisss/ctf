import { withCookies, Cookies } from 'react-cookie';
import React, { Component } from 'react';
import { instanceOf } from 'prop-types';
import neil from './neil.jpeg';
import cookie from './cookie.jpeg'


class Cookie extends Component{
	static propTypes = {
	    cookies: instanceOf(Cookies).isRequired
	  };
	constructor(props){
		super(props)
		this.state = {
			value: '',
			phase1: false,
			phase2: false,
			value2: '',
			counter: 0
		}
		this.handleChange = this.handleChange.bind(this)
		this.handlePassChange = this.handlePassChange.bind(this)
		this.handleSubmit = this.handleSubmit.bind(this)
	}
	handlePassChange(event){
		this.setState({value2:event.target.values})
	}

	handleChange(event){
		this.setState({value: event.target.value});
	}
	handleSubmit(event){
		const {cookies} = this.props
		if (cookies.get('logged_in') === 'true'){
			this.setState({phase1: true})
			if(cookies.get('name') === undefined){
				cookies.set('name', "Neil Patil")
			}
			window.location.reload()
		}
		else{
			this.setState({counter: this.state.counter + 1})
			alert("Invalid Login.")
		}
	}
	componentDidMount(){
		const {cookies} = this.props
		if(cookies.get('logged_in') === undefined){
			cookies.set('logged_in',false)
		}
		else if (cookies.get('logged_in') === 'true'){
			this.setState({phase1: true})
			if(cookies.get('name') === undefined){
				cookies.set('name', "Neil Patil")
			}
		}
	}
	componentWillMount(){
		const {cookies} = this.props
		if(cookies.get('logged_in') === undefined){
			cookies.set('logged_in',false)
		}
		else if (cookies.get('logged_in') === 'true'){
			this.setState({phase1: true})
			if(cookies.get('name') === undefined){
				cookies.set('name', "Neil Patil")
			}
		}
	}
	render(){
		const {cookies} = this.props;
		let result = null
		let tip = null

		if (!this.state.phase1){
			result = <center>
			<h3>Login to buy cookies</h3>
			<h5>Check da Cookiez on dis website</h5>
			<form onSubmit={this.handleSubmit}>
		        <label>
		          Username:
		          <input type="text" value={this.state.value} onChange={this.handleChange} />
		        </label>
				<br />
				<label>
		          Password:
		          <input type="password" value={this.state.value2} onChange={this.handlePassChange} />
		        </label>
				<br />
		        <input type="submit" value="Submit" />
		      </form>
			  </center>
		}
		else if(this.state.phase1 && cookies.get('name') != "Neil Patil"){
			result = <div><center><h1>utflag&#123;buy_more_cookiez&#125;</h1></center><br /><center><img src ={cookie} /></center></div>
		}
		else{
			result = <center><h1>You are logged in as Neil Patil. Neil, you can&#39;t buy your own cookies dadgummit!</h1></center>
		}
		if(this.state.counter === 5){
			tip = <center><h3>Maybe you should see how the website checks if you&#39;re logged in?</h3></center>
		}
		else if(this.state.counter === 10){
			tip = <center><h3>There&#39;s a hint in the source html file</h3></center>
		}

		return(
			<div>
			<center><img src ={neil} /></center><br />
			{result}
			{tip}
			</div>
		)
	}
}
export default withCookies(Cookie)
