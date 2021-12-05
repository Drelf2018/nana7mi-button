const webpack = require('webpack');

module.exports = {
  publicPath: process.env.BASE_URL,
  configureWebpack: {
    plugins: [
      new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
      })
    ]
  }
}