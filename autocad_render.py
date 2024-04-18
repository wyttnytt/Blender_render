from pyautocad import Autocad, APoint, aDouble

acad = Autocad(create_if_not_exists=True)
cubes={}

class Cube():

    def __init__(self, width, height) :
        self.width = width
        self.height = height
        self.vertices = 4
    

    def calculate_distance(self):
        global cubes
        x, y = 0.0, 0.0
        if len(cubes)!=0:
            for cube in cubes:
                width = cubes[cube].width
                x = x+width
                y = y
        self.tlxy = (x, y)

    def calculate_exy(self):
        exy=[]
        for vertice in range(0, self.vertices*2):                                             
            if vertice==0:
                x=self.tlxy[0]
                y=self.tlxy[1]
                z=0
            elif vertice==1:
                x=self.tlxy[0]
                y=self.tlxy[1]+self.height
                z=0
            elif vertice==2:
                x=self.tlxy[0]+self.width
                y=self.tlxy[1]+self.height
                z=0
            elif vertice==3:
                x=self.tlxy[0]+self.width
                y=self.tlxy[1]
                z=0
            
            self.crd = [x, y, z]
    
            exy.extend(self.crd)
        fp = [self.tlxy[0], self.tlxy[1], 0]
        exy.extend(fp)

        return exy
    
    def texy(self, exy):
        texy=tuple(exy)
        return texy
    
def add_cube(width:float, height:float):
    global cubes
    cube=Cube(width, height)
    cube.calculate_distance()
    exy=cube.calculate_exy()
    texy=cube.texy(exy)
    polygon = aDouble(texy)
    polygond = acad.model.AddPolyline(polygon)
    cubes["cube_"+str(len(cubes)+1)]=cube


polygon_1 = add_cube(12.5, 12.5)

polygon_2 = add_cube(12.5, 12.5)

polygon_3 = add_cube(12.5, 12.5)
