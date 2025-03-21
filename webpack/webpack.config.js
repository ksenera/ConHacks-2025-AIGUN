const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');
module.exports = {
   mode: "development",
   devtool: "inline-source-map",
   entry: {
      background: path.resolve(__dirname, "..", "src", "background.ts"),
      contentScript: path.resolve(__dirname, "..", "src", "contentScript.ts" )
   },
   output: {
      path: path.join(__dirname, "../dist"),
      filename: "[name].js",
   },
   resolve: {
      extensions: [".ts", ".js"],
   },
   module: {
      rules: [
         {
            test: /\.tsx?$/,
            loader: "ts-loader",
            exclude: /node_modules/,
         },
      ],
   },
   plugins: [
      new CopyPlugin({
         patterns: [{from: 'public/manifest.json', to: path.resolve(__dirname, 'dist')}]
      }),
   ],
};