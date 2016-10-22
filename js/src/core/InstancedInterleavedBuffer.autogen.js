//
// This file auto-generated with generate-wrappers.js
// Date: Fri Oct 21 2016 17:17:07 GMT-0700 (PDT)
//

var _ = require('underscore');
var widgets = require('jupyter-js-widgets');

var ThreeModel = require('../_base/Three').ThreeModel;
var ThreeView = require('../_base/Three').ThreeView;


var InstancedInterleavedBufferModel = ThreeModel.extend({

    defaults: _.extend({}, ThreeModel.prototype.defaults, {

        _view_name: 'InstancedInterleavedBufferView',
        _model_name: 'InstancedInterleavedBufferModel',


    }),

    constructThreeObject: function() {

        return new THREE.InstancedInterleavedBuffer();

    },

    createPropertiesArrays: function() {

        ThreeModel.prototype.createPropertiesArrays.call(this);
        


    },

});

var InstancedInterleavedBufferView = ThreeView.extend({});

module.exports = {
    InstancedInterleavedBufferView: InstancedInterleavedBufferView,
    InstancedInterleavedBufferModel: InstancedInterleavedBufferModel,
};
