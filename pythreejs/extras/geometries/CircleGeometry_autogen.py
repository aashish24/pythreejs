from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry


class CircleGeometry(Geometry):
    """CircleGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 17:17:08 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/CircleGeometry 
    """

    def __init__(self, radius=50, segments=8, thetaStart=0, thetaLength=6.283185307179586, **kwargs):
        kwargs['radius'] = radius
        kwargs['segments'] = segments
        kwargs['thetaStart'] = thetaStart
        kwargs['thetaLength'] = thetaLength
        super(Geometry, self).__init__(**kwargs)

    _view_name = Unicode('CircleGeometryView').tag(sync=True)
    _model_name = Unicode('CircleGeometryModel').tag(sync=True)

    radius = CFloat(50).tag(sync=True)
    segments = CInt(8).tag(sync=True)
    thetaStart = CFloat(0).tag(sync=True)
    thetaLength = CFloat(6.283185307179586).tag(sync=True)

