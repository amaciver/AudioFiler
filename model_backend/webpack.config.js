var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: './model/static/assets/js/index',

  output: {
    path: path.resolve('./model/static/assets/bundles/'),
    filename: 'bundle.js'
  },
  plugins: [
    new BundleTracker({ filename: './webpack-stats.json'}),
  ],
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['react', 'es2015']
        }
      }
    ]
  },
  devtool: 'source-maps',
  resolve: {
    extensions: ['*', '.js', '.jsx']
  }
};
