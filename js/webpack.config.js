var loaders = [
    { test: /\.json$/, loader: "json-loader" },
    { test: /\.css$/, loader: 'style-loader!css-loader' }
];

var buildExtension = require('@jupyterlab/extension-builder/lib/builder').buildExtension;

buildExtension({
    name: 'jupyter-threejs',
    entry: './src/labplugin',
    outputDir: '../pythreejs/staticlab',
    useDefaultLoaders: false,
    config: {
        module: {
            loaders: loaders
        }
    }
});

module.exports = [
    {
        // Notebook extension
        entry: './src/extension.js',
        output: {
            filename: 'extension.js',
            path: '../pythreejs/static',
            libraryTarget: 'amd'
        },
        resolve: {
            extensions: [ "", ".autogen.js", ".js" ]
        },
    },
    {
        // jupyter-threejs bundle for the notebook
        entry: './src/index.js',
        output: {
            filename: 'index.js',
            path: '../pythreejs/static',
            libraryTarget: 'amd'
        },
        devtool: 'source-map',
        module: {
            loaders: loaders
        },
        externals: ['jupyter-js-widgets'],
        resolve: {
            extensions: [ "", ".autogen.js", ".js" ]
        },

    },
    {
        // embeddable jupyter-threejs bundle
        entry: './src/index.js',
        output: {
            filename: 'index.js',
            path: './dist/',
            libraryTarget: 'amd'
        },
        devtool: 'source-map',
        module: {
            loaders: loaders
        },
        externals: ['jupyter-js-widgets'],
        resolve: {
            extensions: [ "", ".autogen.js", ".js" ]
        },

    },
    {
        // embeddable jupyter-threejs bundle
        entry: './src/index.js',
        output: {
            filename: 'index.standalone.js',
            path: './dist/',
        },
        devtool: 'source-map',
        module: {
            loaders: loaders
        },
        resolve: {
            extensions: [ "", ".autogen.js", ".js" ]
        },

    }

];
