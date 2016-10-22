from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry


class TorusGeometry(Geometry):
    """TorusGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 17:17:08 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/TorusGeometry 
    """

    def __init__(self, radius=100, tube=40, radialSegments=8, tubularSegments=6, arc=6.283185307179586, **kwargs):
        kwargs['radius'] = radius
        kwargs['tube'] = tube
        kwargs['radialSegments'] = radialSegments
        kwargs['tubularSegments'] = tubularSegments
        kwargs['arc'] = arc
        super(Geometry, self).__init__(**kwargs)

    _view_name = Unicode('TorusGeometryView').tag(sync=True)
    _model_name = Unicode('TorusGeometryModel').tag(sync=True)

    radius = CFloat(100).tag(sync=True)
    tube = CFloat(40).tag(sync=True)
    radialSegments = CInt(8).tag(sync=True)
    tubularSegments = CInt(6).tag(sync=True)
    arc = CFloat(6.283185307179586).tag(sync=True)

