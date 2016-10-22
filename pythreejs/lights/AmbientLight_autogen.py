from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .Light_autogen import Light


class AmbientLight(Light):
    """AmbientLight
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 17:17:07 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Lights/AmbientLight 
    """

    def __init__(self, color="#ffffff", intensity=1, **kwargs):
        kwargs['color'] = color
        kwargs['intensity'] = intensity
        super(Light, self).__init__(**kwargs)

    _view_name = Unicode('AmbientLightView').tag(sync=True)
    _model_name = Unicode('AmbientLightModel').tag(sync=True)


