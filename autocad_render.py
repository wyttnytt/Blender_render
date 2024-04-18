from pyautocad import Autocad, APoint, aDouble

acad = Autocad(create_if_not_exists=True)

class Cube():
    def __init__(self, width, height) :
        self.width = width
        self.height = height
        self.vertices = 4
    
    def calculate_xy(self, xy):
        lxy = (map(float, xy.split(", ")))
        tlxy = tuple(lxy)
        return tlxy
    
    def calculate_exy(self, tlxy):
        exy=[]
        for vertice in range(0, self.vertices*2):                                             
            if vertice==0:
                x=tlxy[0]
                y=tlxy[1]
                z=0
            elif vertice==1:
                x=tlxy[0]
                y=tlxy[1]+self.height
                z=0
            elif vertice==2:
                x=tlxy[0]+self.width
                y=tlxy[1]+self.height
                z=0
            elif vertice==3:
                x=tlxy[0]+self.width
                y=tlxy[1]
                z=0
            
            self.crd = [x, y, z]
    
            exy.extend(self.crd)
        fp = [tlxy[0], tlxy[1], 0]
        exy.extend(fp)
        print(exy)
        return exy
    
    def texy(self, exy):
        texy=tuple(exy)
        return texy
    


cube=Cube(12.5, 12.5)
tlxy=cube.calculate_xy("0, 0")
exy=cube.calculate_exy(tlxy)
texy=cube.texy(exy)

polygon = aDouble(texy)
polygond = acad.model.AddPolyline(polygon)