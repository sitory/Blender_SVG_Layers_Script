import bpy

def SelectCurves():
 SelectedCurve = "Curve"
 SelectedCurveNumber = 0
 while bpy.data.objects.get(SelectedCurve) is not None:
  bpy.data.objects[SelectedCurve].select = True
  SelectedCurveNumber = SelectedCurveNumber + 1
  SelectedCurve= "Curve." + str(SelectedCurveNumber).zfill(3)

def ImportSVG():
 Object = "Curve"
 Move = -0.001
 Layer = 0
 LayNum = 0
 Scale = (25, 25, 0)
 while bpy.data.objects.get(Object) is not None:
  #Rotation
  bpy.data.objects[Object].rotation_euler = (1.5708,0,0)
  #Scale
  bpy.data.objects[Object].scale = Scale
  bpy.data.objects[Object].location.y = Layer
  LayNum = LayNum + 1
  Layer = Layer + Move
  Object= "Curve." + str(LayNum).zfill(3)

SelectCurves()
ImportSVG()
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
