import struct
import os

from OpenGL.GL import *
from OpenGL.GLU import *

class createPoint:
    def __init__(self, p, c=(0,1,0)): #p being the point and c being the colour
        self.point_size = 0.5
        self.colour = c
        
        self.x = p[0]
        self.y = p[1]
        self.z = p[2]

    def glvertex(self):
        glVertex3f(self.x, self.y, self.z)

class createTriangle:
    points = None
    normal = None
    
    def __init__(self, p1, p2, p3, n = None):
        #3 points of the triangle
        self.points = createPoint(p1), createPoint(p2), createPoint(p3)

        #triangles normal
        self.normal = createPoint(self.calculateNormal(self.points[0], self.points[1], self.points[2]))

    #calculate vector / edge
    def calculateVector(self, p1, p2):
        return -p1.x+p2.x, -p1.y+p2.y, -p1.z+p2.z

    def calculateNormal(self, p1, p2, p3):
        a = self.calculateVector(p3, p2)
        b = self.calculateVector(p3, p1)

        #calculating the cross product returns a vector that is perpendicular
    def crossProduct(self, p1, p2):
        return (p1[1]*p2[2]-p2[1]*p1[2]) , (p1[2]*p2[0])-(p2[2]*p1[0]) , (p1[0]*p2[1])-(p2[0]*p1[1])

class loader:
    model = []

    #return the faces of the triangles
    def getTriangles(self):
        if self.model:
            for face in self.model:
                yield face

    def loadStl(self, filename):
        #determine if the file is binary or ascii
        fp = open(filename, 'rb')
        h = fp.read(80)
        type = h[0:5]
        fp.close()

        if type == 'solid':
            print("reading text file, " + str(filename))
            self.loadTextStl(filename)
        else:
            print("reading binary stl file, " + str(filename))
            self.loadBinaryStl(filename)
        
        #read text stl and match keywords to grab the points to build the model
    def loadTextStl(self, filename):
        fp = open(filename, 'r')

        for line in fp.readlines():
            words = line.split()
            if len(words) > 0:
                if words[0] == 'solid':
                    self.name = words[1]

                if words[0] == 'facet':
                    center=[0.0, 0.0,0.0]
                    triangle=[]
                    normal = (eval(words[2]), eval(words[3]), eval(words[4]))

                if words[0] == 'vertex':
                    triangle.append(eval(words[1]), eval(words[2]), eval(words[3]))

                if words[0] == 'endloop':
                #make sure we got the corrent number of values before storing
                    if len(triangle) == 3:
                        self.model.append(createTriangle(triangle[0], triangle[1], triangle[2], normal))
        fp.close()
    def loadBinaryStl(self, filename):
        fp = open(filename, 'rb')
        h = fp.read(80)

        l = struct.unpack('I', fp.read(4))[0]
        count = 0
        while True:
            try:
                p = fp.read(12)
                if len(p) == 12:
                    n=struct.unpack('f',p[0:4])[0],struct.unpack('f',p[4:8])[0],struct.unpack('f',p[8:12])[0]
                  
                p=fp.read(12)
                if len(p) == 12:
                    p1=struct.unpack('f',p[0:4])[0],struct.unpack('f',p[4:8])[0],struct.unpack('f',p[8:12])[0]

                p=fp.read(12)
                if len(p) == 12:
                    p2=struct.unpack('f',p[0:4])[0],struct.unpack('f',p[4:8])[0],struct.unpack('f',p[8:12])[0]

                p=fp.read(12)
                if len(p) == 12:
                    p3=struct.unpack('f',p[0:4])[0],struct.unpack('f',p[4:8])[0],struct.unpack('f',p[8:12])[0]

                newTri = (n, p1, p2, p3,)

                if len(newTri) == 4:
                    tri = createTriangle(p1, p2, p3, n)
                    self.model.append(tri)
                count += 1
                
                fp.read(2)
                if len(p) == 0:
                    break
            except EOFError:
                break
        fp.close()

class drawScene:
    def __init__(self,style = 1):
        self.model1 = loader()
        self.model1.loadStl(os.path.abspath('') + '/binary.stl')
        self.initShading()
    
def main():
    model1 = loader()
    model1.loadStl(os.path.abspath("C:/Users/aidan/Downloads") + '/Cube.stl')
main()




