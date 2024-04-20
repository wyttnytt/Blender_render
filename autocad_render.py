from pyautocad import Autocad, aDouble

acad = Autocad(create_if_not_exists=True)
cubes={}

class Cube():
    def __init__(self, size):
        global cubes
        self.width, self.height, self.depth = size
        

    def create_cube(self):
        x, y, z = self.x, self.y, self.z
        width, height, depth = self.width, self.height, self.depth
        pmatrx = aDouble(x, z, y, 
                         x+width, z, y, 
                         x, z+depth, y, 
                         x+width, z+depth, y, 
                         x, z+depth, y+height, 
                         x+width, z+depth, y+height, 
                         x, z, y+height, 
                         x+width, z, y+height, 
                         x, z, y, 
                         x+width, z, y,
                         x+width, z, y,
                         x+width, z+depth, y,
                         x+width, z, y+height,
                         x+width, z+depth, y+height,
                         x, z, y+height,
                         x, z+depth, y+height,
                         x, z, y,
                         x, z+depth, y,
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
            self.mini_cube = Cube((self.width/2, self.height, self.depth/2))
            self.mini_cube.x, self.mini_cube.y, self.mini_cube.z = self.x + self.width/4, self.y, self.z + self.depth/4
            mini_matrx=self.mini_cube.create_cube()
            mini_mesh = acad.model.Add3DMesh(5 , 2, mini_matrx)

def deploy_cube():
    global cubes
    cube = Cube((10, 10, 10))
    cube.xyz()
    cubes["cube",str(len(cubes)+1)] = cube
    matrx = cube.create_cube()

    mesh = acad.model.Add3DMesh(5 , 2, matrx)

cube=Cube((10, 10, 10))
cube.xyz()
cubes["cube",str(len(cubes)+1)] = cube
matrx = cube.create_cube()
cube.mini_cube()

mesh1 = acad.model.Add3DMesh(9 , 2, matrx)

cube2 = Cube((20, 20, 10))
cube2.xyz()
cubes["cube",str(len(cubes)+1)] = cube2
matrx2 = cube2.create_cube()
cube2.mini_cube()

mesh2 = acad.model.Add3DMesh(9 , 2, matrx2)

cube3 = Cube((10, 10, 10))
cube3.xyz()
cubes["cube",str(len(cubes)+1)] = cube3
matrx3 = cube3.create_cube()
cube3.mini_cube()

mesh3 = acad.model.Add3DMesh(9 , 2, matrx3)
