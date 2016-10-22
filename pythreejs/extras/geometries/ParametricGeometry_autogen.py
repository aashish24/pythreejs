from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry


class ParametricGeometry(Geometry):
    """ParametricGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 17:17:08 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/ParametricGeometry 
    """

    def __init__(self, func, slices=3, stacks=3, **kwargs):
        kwargs['func'] = func
        kwargs['slices'] = slices
        kwargs['stacks'] = stacks
        super(Geometry, self).__init__(**kwargs)

    _view_name = Unicode('ParametricGeometryView').tag(sync=True)
    _model_name = Unicode('ParametricGeometryModel').tag(sync=True)

    func = Unicode('function (u,v) { return THREE.Vector3(); }').tag(sync=True)
    slices = CInt(3).tag(sync=True)
    stacks = CInt(3).tag(sync=True)

