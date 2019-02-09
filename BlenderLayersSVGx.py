import bpy
Object = "Curve"
Move = 0.001
Layer = 0
def MoveIt():
    if bpy.data.objects.get(Object) is not None:
        bpy.data.objects[Object].location.z += Layer
MoveIt()

Layer = Layer + Move
Object= "Curve.001"
MoveIt()

Layer = Layer + Move
Object= "Curve.002"
MoveIt()
