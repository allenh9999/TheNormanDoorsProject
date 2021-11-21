const path = require('path');
const webpack = require('webpack');




const HtmlWebpackPlugin = require('html-webpack-plugin')




/*
 * We've enabled HtmlWebpackPlugin for you! This generates a html
 * page for you when you compile webpack, which will make you start
 * developing and prototyping faster.
 *
 * https://github.com/jantimon/html-webpack-plugin
 *
 */

const WorkboxWebpackPlugin = require('workbox-webpack-plugin');

const { VueLoaderPlugin } = require('vue-loader')


module.exports = {
  mode: 'development',
  entry: './NormanDoors/js/main.js',

  plugins: [
   new webpack.ProgressPlugin(), 
   new HtmlWebpackPlugin({
            template: 'index.html'
          }), new WorkboxWebpackPlugin.GenerateSW({
          swDest: 'sw.js',
          clientsClaim: true,
          skipWaiting: false,
        }), 
   new VueLoaderPlugin(),
   new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery"
   })
  ],

  module: {
    rules: [
    {
       test: /\.css$/,
       use: [
         'vue-style-loader',
         'css-loader'
       ]
    },
    {
       test: /\.vue$/,
       loader: 'vue-loader'
    },
    {
       test: /\.js$/,
       loader: 'babel-loader'
    }
    ]
  },

  devServer: {
    open: true,
    host: 'localhost'
  },
  
  resolve: {
    extensions: ['.js', '.jsx', '.vue'],
    alias: { vue: 'vue/dist/vue.js' },
  },
  
  output: {
    path: path.join(__dirname, '/NormanDoors/static/js/'),
    filename: 'bundle.js',
  },
}