import React, {Component} from 'react'
import DefaultRouter from './Router/Router'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import Navigation from './Navbar/Navbar'
/* eslint-enable no-unused-vars */

export default class App extends Component {
  render () {
    return (
      <MuiThemeProvider>
        <div>
        <Navigation />
          <DefaultRouter />
        </div>
      </MuiThemeProvider>
    )
  }
}
