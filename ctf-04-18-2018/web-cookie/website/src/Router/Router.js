import React, {Component} from 'react'
import {Route, Switch} from 'react-router-dom'
import Splash from '../Splash/Splash'
import Cookie from '../Cookie/Cookies'
import Patils from '../Patils/Patils'
export default class DefaultRouter extends Component {
	render(){
		return(
			<Switch>
			<Route exact path="/" component={Splash}/>
			<Route exact path="/cookies" component={Cookie}/>
			<Route exact path="/patils" component={Patils}/>
			</Switch>
		)
	}
}
