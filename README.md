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

## Technologies & Technical Challenges
  ###### Backend: Python/Django
  ###### Frontend: JavaScript

#### Composing a dataset
  + ##### Accessing song data
   - 'Million Song Dataset' has produced a publicly available dataset from Last.fm, which contains songs and genre tags. We may be able to extract the meta-data we need for building out a list of training songs directly from this dataset.
   - Regardless, we can use the Last.fm API to determine 20-30 top tags that we feel adequately covers a wide range of genres. We will use SQL queries on the MSD, or API calls by tag-name to Last.fm to get a robust list of tracks with which to train our model

  + ##### Feature Extraction
   - Using this list of song titles and tags, we will stream 30-second clips of songs from the Spotify API into our Feature Extraction module
   - Our Feature Extraction module will implement the PyAudioAnalysis Library to extract a variety of features of the audio into a multi dimensional vector which will constitute an entry into our training dataset, along with the corresponding genre tag

#### Constructing the neural network
  + ##### Building the network
    - Powerful tools are available for the construction of neural networks, including the Tensorflow library, as well as several detailed tutorials for building and training a neural network
    - We intend to build a 3- to 4-layer neural network with an input dimensionality equal to the number of audio features we extract, and an output dimensionality equal to the number of genres we select as possibilities
  + ##### Determining the fitness function
    - We intend to use the softmax linear regression optimizer to judge the fitness of outcomes
  + ##### Training and validating the model
    - Once the network is constructed and dataset established, it is somewhat trivial to train the model
    - Validation will be done with a subset of our dataset, and by subjective judgement

#### Frontend Interface
  + ##### Searching and Streaming
    - We will implement Spotify Search to allow users to select a song to evaluate
    - We will stream a 30-second clip from spotify into our model
    - The outcome will be sent back to the frontend for user evaluation

  #### Bonus Features
    * Visualizations showing the training process
    * Visualizations of the audio feature extraction
    * User evaluations are incorporated into the dataset and used to improve the model


## Project Flowchart

![project-diagram](./images/project-diagram.png)


## Group Members & Work Breakdown
