import bpy
import math
Move = -0.001
Scale = 20
Angle = 90

def SelectCurves():
 SelectedCurve = "Curve"
 SelectedCurveNumber = 0
 while bpy.data.objects.get(SelectedCurve) is not None:
  bpy.data.objects[SelectedCurve].rotation_euler = (math.radians(Angle),0,0)
  bpy.data.objects[SelectedCurve].select = True
  SelectedCurveNumber = SelectedCurveNumber + 1
  SelectedCurve= "Curve." + str(SelectedCurveNumber).zfill(3)

def ImportSVG():
 Object = "Curve"
 Layer = 0
 LayNum = 0
 while bpy.data.objects.get(Object) is not None:
  bpy.data.objects[Object].location.y = Layer
  LayNum = LayNum + 1
  Layer = Layer + Move
  Object= "Curve." + str(LayNum).zfill(3)

bpy.ops.object.select_all(action='DESELECT')
SelectCurves()
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
ImportSVG()
bpy.ops.transform.resize(value=(Scale, 1, Scale))
#Cursor to center
bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
# Use Shift + S - > Selection to Cursor (Offset) to move your model to center
# Use S -> Shift+Y to resize your model
