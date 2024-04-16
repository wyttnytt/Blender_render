import bpy


objects={}
meshes=[]
cubes=[]

def draw():
    for i in objects:
        view_layer.active_layer_collection.collection.objects.link(objects[i])

class cube():
    
    def __init__(self, width, height, depth):
        global cubes
        
        self.width = width
        self.height = height
        self.depth = depth
        

    def vertices_calculations(self, width, height, depth): #xyz
        x,y,z=(0,0,0)
        if len(cubes)!=0:
            for cube in cubes:
                x=x+cube.width
                y=y+cube.height
                z=z+cube.depth
            

        vertices=[(x, 0, 0), (x+width, 0, 0), (x+width, height, 0), (x+0, height, 0), (x+0, 0, depth), (x+width, 0, depth), (x+width, height, depth), (x+0, height, depth)]
        return vertices

    def edges_calculations(self):
        edges= [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)] 
        return edges

    def faces_calculations(self):
        faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]
        return faces
    
    def create_object(self):
        global objects
        object=bpy.data.objects.new("object_"+str(len(objects)+1), self.mesh)
        objects["object_"+str(len(objects)+1)]=object

def deploy_cube(object):
    global cubes

    object.vertices=object.vertices_calculations(object.width, object.height, object.depth)
    object.edges=object.edges_calculations()
    object.faces=object.faces_calculations()

    object.mesh = bpy.data.meshes.new("mesh_"+str(len(meshes)+1))
    object.mesh.from_pydata(object.vertices, object.edges, object.faces)
    object.mesh.update()

    object.create_object()

    cubes.append(object)

#xyz
try:
    cube_1 = cube(30, 10, 10)
    deploy_cube(cube_1)
    cube_2 = cube(20, 10, 50)
    deploy_cube(cube_2)
    cube_3 = cube(40, 10, 30)
    deploy_cube(cube_3)
    view_layer = bpy.context.view_layer

    draw()
except: 
    print("something went wrong")