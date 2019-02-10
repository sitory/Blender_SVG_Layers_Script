import bpy

Object = "Curve"
Scale = (25, 25, 0)
Move = -0.001
Layer = 0
LayNum = 0
while bpy.data.objects.get(Object) is not None:
    #Select all Curves
    bpy.data.objects[Object].select = True
    #Scale all Curves
    bpy.data.objects[Object].scale = Scale
    #Rotation
    bpy.data.objects[Object].rotation_euler = (1.5708,0,0)
    #Set origin
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    #Move the layers
    bpy.data.objects[Object].location.y = Layer
    LayNum = LayNum + 1
    Layer = Layer + Move
    Object= "Curve." + str(LayNum).zfill(3)

    
