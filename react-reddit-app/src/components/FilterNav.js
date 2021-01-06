import React from 'react'

const Checkbox = props => (
    <input type="checkbox" {...props} />
  )

class FilterNav extends React.Component {
state = { checked: false }
handleCheckboxChange = event =>
    this.setState({ checked: event.target.checked })
render() {
    return (
    <div>
        <label>
        <Checkbox
            checked={this.state.checked}
            onChange={this.handleCheckboxChange}
        />
        <span>Weight Loss</span>

        </label>
        <label>
        <Checkbox
            checked={this.state.checked}
            onChange={this.handleCheckboxChange}
        />
        <span>Weight Gains</span>
        </label>
    </div>    
    ) 
}
}

export default FilterNav;