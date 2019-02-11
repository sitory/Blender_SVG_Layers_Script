import bpy

def SelectCurves():
 Scale = (25, 25, 0)
 SelectedCurve = "Curve"
 SelectedCurveNumber = 0
 while bpy.data.objects.get(SelectedCurve) is not None:
  bpy.data.objects[SelectedCurve].scale = Scale
  bpy.data.objects[SelectedCurve].rotation_euler = (1.5708,0,0)
  bpy.data.objects[SelectedCurve].select = True
  SelectedCurveNumber = SelectedCurveNumber + 1
  SelectedCurve= "Curve." + str(SelectedCurveNumber).zfill(3)

def ImportSVG():
 Object = "Curve"
 Move = -0.001
 Layer = 0
 LayNum = 0
 while bpy.data.objects.get(Object) is not None:
  bpy.data.objects[Object].location.y = Layer
  LayNum = LayNum + 1
  Layer = Layer + Move
  Object= "Curve." + str(LayNum).zfill(3)

SelectCurves()
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
ImportSVG()
