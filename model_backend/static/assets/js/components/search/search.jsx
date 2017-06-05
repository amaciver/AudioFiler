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
    {suggestion.track} by {suggestion.artist}

  </div>
);


class Search extends React.Component {
  constructor(props) {
    super(props);
    // console.log(props.cities);
    this.state = {
      value: '',
      suggestions: [],
      url: '',
      track: null
    };
    this.onChange = this.onChange.bind(this);
    this.onSuggestionsFetchRequested = this.onSuggestionsFetchRequested.bind(this);
    this.onSuggestionsClearRequested = this.onSuggestionsClearRequested.bind(this);
    this.onSuggestionSelected = this.onSuggestionSelected.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentWillMount() {
    this.props.fetchToken().then( () => console.log(this.props.token))
  }

  componentWillReceiveProps(nextProps) {
  }

  onChange(event, { newValue, method }) {
    switch (method) {
      case 'type':
        this.setState({value: newValue}, () => {
          this.props.fetchTracks(newValue).then( () => {
            this.setState({
              suggestions: this.props.tracks
            })
          })
        })
      default:
        this.setState({
          value: newValue
        })
    }
  }

  handleSubmit(e){
    e.preventDefault();
    // console.log(this.state.url);
    this.props.receiveTrack(this.state.track);
    this.props.clearResults({});
    // console.log(this.props.tracks);
    this.props.fetchResults(this.state.url);
  }

  onSuggestionsFetchRequested({ value }) {
    this.setState({
      suggestions: this._getSuggestions(value)
    });
  }

  onSuggestionsClearRequested() {
    this.props.clearResults({});
    this.setState({
      suggestions: []
    });
  }

  onSuggestionSelected(e, { suggestion, method }) {
    // console.log(suggestion);
    this.setState({url: suggestion.url, track: suggestion})
  }

  _getSuggestions(value) {
    const inputValue = value.trim().toLowerCase();
    const inputLength = inputValue.length;
    return this.state.suggestions;
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
        <div>Hello</div>
        <div className='search-title'>Search</div>

        <form className='search-form' onSubmit={this.handleSubmit}>
          <div className='search-oval'>
            <Autosuggest

              suggestions={suggestions}
              onSuggestionsFetchRequested={this.onSuggestionsFetchRequested}
              onSuggestionsClearRequested={this.onSuggestionsClearRequested}
              onSuggestionSelected={this.onSuggestionSelected}
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
