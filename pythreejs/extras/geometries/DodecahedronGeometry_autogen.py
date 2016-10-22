from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry


class DodecahedronGeometry(Geometry):
    """DodecahedronGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 17:17:08 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/DodecahedronGeometry 
    """

    def __init__(self, radius=1, detail=0, **kwargs):
        kwargs['radius'] = radius
        kwargs['detail'] = detail
        super(Geometry, self).__init__(**kwargs)

    _view_name = Unicode('DodecahedronGeometryView').tag(sync=True)
    _model_name = Unicode('DodecahedronGeometryModel').tag(sync=True)

    radius = CFloat(1).tag(sync=True)
    detail = CInt(0).tag(sync=True)

