//
// This file auto-generated with generate-wrappers.js
// Date: Fri Oct 21 2016 17:17:07 GMT-0700 (PDT)
//

var _ = require('underscore');
var widgets = require('jupyter-js-widgets');

var ThreeModel = require('../_base/Three').ThreeModel;
var ThreeView = require('../_base/Three').ThreeView;


var AnimationMixerModel = ThreeModel.extend({

    defaults: _.extend({}, ThreeModel.prototype.defaults, {

        _view_name: 'AnimationMixerView',
        _model_name: 'AnimationMixerModel',


    }),

    constructThreeObject: function() {

        return new THREE.AnimationMixer();

    },

    createPropertiesArrays: function() {

        ThreeModel.prototype.createPropertiesArrays.call(this);
        


    },

});

var AnimationMixerView = ThreeView.extend({});

module.exports = {
    AnimationMixerView: AnimationMixerView,
    AnimationMixerModel: AnimationMixerModel,
};
