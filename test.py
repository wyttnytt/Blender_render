from pyautocad import Autocad, aDouble

acad = Autocad(create_if_not_exists=True)


pmatrx = aDouble(10, 10, 0, 20, 10, 0, 10, 20, 0, 20, 20, 0, 10, 20, 10, 20, 20, 10, 10, 10, 10, 20, 10, 10, 10, 10, 0, 20, 10, 0)

#10, 10, 0, 10, 20, 0, 20, 20, 0, 20, 10, 0, 10, 10, 0, 10, 10, 10, 10, 20, 10, 20, 20, 10, 20, 10, 10, 10, 10, 10 
mesh1 = acad.model.Add3DMesh(5 , 2, pmatrx)