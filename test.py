from pyautocad import Autocad, APoint


acad = Autocad(create_if_not_exists=True)
# Box: (Origin/Center, Length, Width, Height)
box = acad.model.AddBox(APoint(0, 0, 0), 1000, 1200, 750)

# Cone: (Center, Base radius, Height)
cone = acad.model.AddCone(APoint(2000, 0, 0), 750, 800)

# Cylinder: (Center, Radius, Height)
cyl =  acad.model.AddCylinder(APoint(3200, 0, 0), 350, 1250)

# Elliptical Cone: (Center, MajorRadius, MinorRadius, Height)
econe =  acad.model.AddEllipticalCone(APoint(4000, 500 , 0), 450, 225, 1275.62)

# EllipticalCylinder: (Center, MajorRadius, MinorRadius, Height)
ecyl =  acad.model.AddEllipticalCylinder(APoint(1500, 2000 , 0), 750, 400, 950)

# Sphere: (Center, Radius)
sph = acad.model.AddSphere(APoint(2500, 3500, 0), 250)

# Torus: (Center, TorusRadius, TubeRadius)
tor = acad.model.AddTorus(APoint(1000, 4000, 0), 500, 100)

# Wedge: (Center, Length, Width, Height)
wed = acad.model.AddWedge(APoint(2000, 5000, 0), 1000, 1200, 750)  