import React from 'react';
import Autosuggest from 'react-autosuggest';
import { hashHistory } from 'react-router';

// TODO: implement isMobile on suggestions list kaimellea/isMobile

// When suggestion is clicked, Autosuggest needs to populate the input element
// based on the clicked suggestion. Teach Autosuggest how to calculate the
// input value for every given suggestion.
const getSuggestionValue = suggestion => suggestion.track;

// const getSuggestionId = suggestion => suggestion.id;

const renderSuggestion = suggestion => (
  <div className='search-list-item'>
    {suggestion.track}
    {suggestion.artist}

  </div>
);


class Search extends React.Component {
  constructor(props) {
    super(props);
    // console.log(props.cities);
    this.state = {
      value: '',
      suggestions: []
    };
    this.onChange = this.onChange.bind(this);
    this.onSuggestionsFetchRequested = this.onSuggestionsFetchRequested.bind(this);
    this.onSuggestionsClearRequested = this.onSuggestionsClearRequested.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentWillMount() {
    // if (!this.props.cities.length > 0) {
    //   this.props.fetchCities();
    // }
  }

  componentWillReceiveProps(nextProps) {
    // if (this.props.cities.length !== nextProps.cities.length) {
    //   this.setState({suggestions: nextProps.cities})
    // }
  }

  onChange(event, { newValue }){
    this.props.fetchTracks(newValue).then( () => {
      this.setState({
        value: newValue,
        suggestions: this.props.tracks
      })
    })
  }

  handleSubmit(){
    // const match = (this.props.cities.filter(city =>
    //   city.name.toLowerCase() === this.state.value.toLowerCase()));
    //
    // if (match.length === 1) {
    //   const id = match[0].id;
    //   hashHistory.push(`/cities/${id}`);
    // }
  }

  // Autosuggest will call this function every time you need to update suggestions.
  // You already implemented this logic above, so just use it.
  onSuggestionsFetchRequested({ value }) {
    this.setState({
      suggestions: this._getSuggestions(value)
    });
  }

  // Autosuggest will call this function every time you need to clear suggestions.
  onSuggestionsClearRequested() {
    this.setState({
      suggestions: []
    });
  }

  _getSuggestions(value) {
    const inputValue = value.trim().toLowerCase();
    const inputLength = inputValue.length;
    return this.state.suggestions;
    // return inputLength === 0 ? [] : this.props.tracks.filter(city =>
    //   city.name.toLowerCase().slice(0, inputLength) === inputValue
    // );
  };


  render(){
    const { value, suggestions } = this.state;

    // Autosuggest will pass through all these props to the input element.
    const inputProps = {
      placeholder: "Enter a track name",
      value,
      onChange: this.onChange
    };

    const renderInputComponent = inputProps => (
      <div >
        <input className='search-field' {...inputProps} />
        <div></div>
      </div>
    );

    return(
      <div className='search-wrapper'>
        <div className='search-title'>Search</div>

        <form className='search-form' onSubmit={this.handleSubmit}>
          <div className='search-oval'>
            <Autosuggest

              suggestions={suggestions}
              onSuggestionsFetchRequested={this.onSuggestionsFetchRequested}
              onSuggestionsClearRequested={this.onSuggestionsClearRequested}
              getSuggestionValue={getSuggestionValue}
              renderSuggestion={renderSuggestion}
              highlightFirstSuggestion={true}
              alwaysRenderSuggestions={false}
              focusInputOnSuggestionClick={false}
              inputProps={inputProps}
              renderInputComponent={renderInputComponent}
            />
            <button
              className="search-submit"
              title="Search"
              type='submit'>

              <i className="fa fa-search fa-2x" aria-hidden="true"></i>
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default Search;
