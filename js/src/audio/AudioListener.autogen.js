//
// This file auto-generated with generate-wrappers.js
// Date: Fri Oct 21 2016 17:17:07 GMT-0700 (PDT)
//

var _ = require('underscore');
var widgets = require('jupyter-js-widgets');

var ThreeModel = require('../_base/Three').ThreeModel;
var ThreeView = require('../_base/Three').ThreeView;


var AudioListenerModel = ThreeModel.extend({

    defaults: _.extend({}, ThreeModel.prototype.defaults, {

        _view_name: 'AudioListenerView',
        _model_name: 'AudioListenerModel',


    }),

    constructThreeObject: function() {

        return new THREE.AudioListener();

    },

    createPropertiesArrays: function() {

        ThreeModel.prototype.createPropertiesArrays.call(this);
        


    },

});

var AudioListenerView = ThreeView.extend({});

module.exports = {
    AudioListenerView: AudioListenerView,
    AudioListenerModel: AudioListenerModel,
};
