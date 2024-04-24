from pyautocad import Autocad, aDouble

acad = Autocad(create_if_not_exists=True)
cubes={}

Layer1=acad.doc.Layers.Add("Layer1")
Layer1.color=5
Layer2=acad.doc.Layers.Add("Layer2")
Layer2.color=1


class Cube():
    def __init__(self, size):
        global cubes
        self.width, self.height, self.depth = size
        

    def create_cube(self):
        x, y, z = self.x, self.y, self.z
        width, height, depth = self.width, self.height, self.depth
        pmatrx = aDouble(x, y, z, 
                         x+width, y, z, 
                         x, y+depth, z, 
                         x+width, y+depth, z, 
                         x, y+depth, z+height, 
                         x+width, y+depth, z+height, 
                         x, y, z+height, 
                         x+width, y, z+height, 
                         x, y, z, 
                         x+width, y, z,
                         x+width, y, z,
                         x+width, y+depth, z,
                         x+width, y, z+height,
                         x+width, y+depth, z+height,
                         x, y, z+height,
                         x, y+depth, z+height,
                         x, y, z,
                         x, y+depth, z,
                         )
        
        
        return pmatrx

    def xyz(self):
        global cubes
        self.x, self.y, self.z = 0, 0, 0
        if len(cubes)!=0:

            for cube in cubes:
                self.x += cubes[cube].width


    def mini_cube(self):

        if len(cubes)==3:
            self.mini_cube = Cube((self.width/2, self.height+0.5, self.depth/2))
            self.mini_cube.x, self.mini_cube.y, self.mini_cube.z = self.x + self.width/4, self.y + self.depth/4, self.z 
            mini_matrx=self.mini_cube.create_cube()
            mini_mesh = acad.model.Add3DMesh(9 , 2, mini_matrx)
            mini_mesh.layer="Layer2"


cube=Cube((10, 10, 10))
cube.xyz()
cubes["cube",str(len(cubes)+1)] = cube
matrx = cube.create_cube()
cube.mini_cube()

mesh1 = acad.model.Add3DMesh(9 , 2, matrx)
mesh1.layer="Layer1"

cube2 = Cube((20, 20, 10))
cube2.xyz()
cubes["cube",str(len(cubes)+1)] = cube2
matrx2 = cube2.create_cube()
cube2.mini_cube()

mesh2 = acad.model.Add3DMesh(9 , 2, matrx2)
mesh2.layer="Layer1"

cube3 = Cube((10, 10, 10))
cube3.xyz()
cubes["cube",str(len(cubes)+1)] = cube3
matrx3 = cube3.create_cube()
cube3.mini_cube()

mesh3 = acad.model.Add3DMesh(9 , 2, matrx3)
mesh3.layer="Layer1"