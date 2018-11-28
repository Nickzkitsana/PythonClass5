from pracLibrary import line35
import math as m

line35()
x1,y1 = input('Point 1 (X,Y): ').split(' ')
x2,y2 = input('Point 2 (X,Y): ').split(' ')
x3,y3 = input('Point 3 (X,Y): ').split(' ')
line35()

point1 = int(x1),int(y1)
point2 = int(x2),int(y2)
point3 = int(x3),int(y3)

point = [point1 , point2 , point3]

areatri = point[0][1]*(point[1][1]-point[2][1])-point[1][0]*(point[0][1]-point[2][1])+point[2][0]*(point[0][1]-point[1][1])

ansarea = abs(areatri/2)
print(ansarea)
