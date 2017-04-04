# AudioFiler

### AudioFiler is a project aiming to implement machine learning to classify songs into genres

## Background and Overview

Classifying songs into genres is a now classic problem in contemporary computer science and media studies. We intend to approach it by extracting features from a large set of audio files in order to train a neural network to classify songs into genres.

This problem decomposes into several areas of activity:
  * Composing a training dataset
  * Constructing a neural network and building the learning model
  * Implementing a frontend interface with which users can test the result of our work

## Functionality & MVP

   - [ ] We will be able to build a training dataset of songs, each entry consisting of a multi-dimensional audio feature vector and audio tag.
   - [ ] We will build a neural network that is trained on the above dataset
   - [ ] We will have a frontend interface that allows users to search for a song and test our model by streaming that song into it and seeing the output.

#### Bonus Features
   - [ ] Visualizations showing the training process
   - [ ] Visualizations of the audio feature extraction
   - [ ] User evaluations are incorporated into the dataset and used to improve the model
   - [ ] Suggest similar tracks
   - [ ] Modify model to produce untrained clusters

## Technologies & Technical Challenges
  ##### Backend: Python/Django
  ##### Frontend: React/JavaScript

#### Composing a dataset
  + ##### Accessing song data
    + 'Million Song Dataset' has produced a publicly available dataset from Last.fm, which contains songs and genre tags. We may be able to extract the meta-data we need for building out a list of training songs directly from this dataset
    + Regardless, we can use the Last.fm API to determine 20-30 top tags that we feel adequately covers a wide range of genres. We will use SQL queries on the MSD, or API calls by tag-name to Last.fm to get a robust list of tracks with which to train our model

  + ##### Feature Extraction
    + Using this list of song titles and tags, we will stream 30-second clips of songs from the Spotify API into our Feature Extraction module
    + Our Feature Extraction module will implement the pyAudioAnalysis Library to extract a variety of features of the audio into a multi dimensional vector which, along with the corresponding genre tag, will constitute an entry into our training dataset

#### Constructing the neural network
  + ##### Building the network
    - Powerful tools are available for the construction of neural networks, including the Tensorflow library, as well as several detailed tutorials for building and training a neural network
    - We intend to build a 3- to 4-layer neural network with an input dimensionality equal to the number of audio features we extract, and an output dimensionality equal to the number of genres we select as possibilities
  + ##### Determining the fitness function
    - We intend to use the softmax linear regression optimizer to judge the fitness of outcomes
  + ##### Training and validating the model
    - Once the network is constructed and dataset established, it is somewhat trivial to train the model
    - Validation will be done with a subset of our dataset, and by subjective judgement

#### UX
  + ##### Frontend Interface
    - We will implement calls to Spotify search to populate an autosuggest field to allow users to select a song to evaluate
    - We will send the songId to the backend and then receive genre results for user evaluation
    - There will be some sort of animation or information pop-up to occupy the user while waiting for results.

  + #### Backend
    + Our backend will be a standard Django build that will be able to receive urls from the frontend when the user selects a song
    + The backend will make a request for the 30-preview of the song from Spotify and load it into a buffer
    + The audio features will be extracted from the buffer, and a test object created and fed into the NN
    + The results of the NN will be sent back to the frontend

## Project Flowchart

![build-phase](./images/build-phase.png)

![ux-phase](./images/ux-phase.png)


## Group Members & Work Breakdown

**Andrew MacIver**,
**Alec Johnson**,
**Adom Hartell**,

### Day 1
  - decide tags
  - SQL queries/ python exclusion script that filters out songs with conflicting tags **ALEC**
  - a properly populated entry into database **ADOM**
    * take some audio
    * convert and analyze with full suite of features
    * parse and join back with tag
  - complete MNIST tutorial **ANDREW**

### Day 2
  - scripting the population process (one at a time) **ADOM**
    - get song name and tag from MSD (D1)
    - make API call to Spotify with song name (D1) **ALEC**
    - buffer object written **ANDREW**
    - receive audio into buffer and output files (D1)
    - convert and analyze with full suite of features **ADOM**
    - parse and join back with tag
    - enter into master database
  - How the NN needs to be different for our implementation **GROUP/ANDREW**
  - Verify schedule and touch base, assess MVPs **decide Day 3/4 roles**
  - Django setup **ADOM**

### Day 3

 - automating dataset population to n-songs  **TBD**
 - first opportunity to train it/hopefully give it a song **TBD**
 - Django to receive a call, make a call, buffer the object **TBD**


### Day 4
  - Frontend index file with webpack, ajax calls in JS, some buttons **TBD**
  - Django need to correctly take in and return result **TBD**
  - Get heroku set up **TBD**

### Day 5
  - messing with the model or exploring the model
  - Frontend probabilities display component
  - Frontend spotify search
    + search requests
    + autosuggest population
    + send id to backend
    + backend request stream
    + backend runs feature Extraction
    + backend runs NN
    + return result to front end
  - Frontend 'working' animation/when they're waiting

### Day 6
 - About the project copy
 - improve UX
