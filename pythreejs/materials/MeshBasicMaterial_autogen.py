from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .Material_autogen import Material

from ..textures.Texture_autogen import Texture

class MeshBasicMaterial(Material):
    """MeshBasicMaterial
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 17:17:07 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Materials/MeshBasicMaterial 
    """

    _view_name = Unicode('MeshBasicMaterialView').tag(sync=True)
    _model_name = Unicode('MeshBasicMaterialModel').tag(sync=True)

    color = Unicode("#ffffff").tag(sync=True)
    map = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    aoMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    aoMapIntensity = CFloat(1).tag(sync=True)
    specularMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    alphaMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    envMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    combine = Enum(Operations, "MultiplyOperation").tag(sync=True)
    reflectivity = CFloat(1).tag(sync=True)
    refractionRatio = CFloat(0.98).tag(sync=True)
    fog = Bool(True).tag(sync=True)
    shading = Enum(Shading, "SmoothShading").tag(sync=True)
    wireframe = Bool(False).tag(sync=True)
    wireframeLinewidth = CFloat(1).tag(sync=True)
    wireframeLinecap = Unicode("round").tag(sync=True)
    wireframeLinejoin = Unicode("round").tag(sync=True)
    vertexColors = Enum(Colors, "NoColors").tag(sync=True)
    skinning = Bool(False).tag(sync=True)
    morphTargets = Bool(False).tag(sync=True)

