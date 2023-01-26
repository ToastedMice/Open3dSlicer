import struct
import numpy

class Load:
    def __init__(self) -> None:
        self.vertices = []
        self.triangle = []
        self.points = []

    def load(self, filename):
        #file = open(filename,'rb')
        #data = file.read(80) #80 bytes is enough to determin if the file is binary
        #type = data[0:5]
        #file.close()
        Ascii = True
        fp = open(filename, 'r')
        try:
            line = fp.readline()
            words = line.split()

        except:
            self.loadBinaryStl(filename)
            Ascii = False
        if(Ascii == True):
            self.loadTextStl(filename)
        

        #if len(words) > 0:
        #    if words[0] == 'solid':
        #        self.loadTextStl(filename)
        #        print("ASCII")
        #    else:
        #        self.loadBinaryStl(filename)
        #        print("Binary")


    def loadTextStl(self, filename):
        print("ASCII")
        fp = open(filename, 'r')
        normal = []
        for line in fp.readlines():
            words = line.split()
            if len(words) > 0:
                
                if words[0] == 'solid':
                    name = words[1]

                #if words[0] == 'facet':
                #    center=[0.0, 0.0,0.0]
                #    self.points = []
                #    normal.append(eval(words[2]))
                #    normal.append(eval(words[3]))
                #    normal.append(eval(words[4]))

                if words[0] == 'vertex':
                    #final list of vertices
                    self.vertices.append(eval(words[1]))
                    self.vertices.append(eval(words[2]))
                    self.vertices.append(eval(words[3]))
                    self.vertices.append(0.00000000000000)
                    self.vertices.append(0.00000000000000)
                    self.vertices.append(1.00000000000000)
                    

                if words[0] == 'endloop':
                    #for OpenGL to create the triangle, we get the index of the vertex in the list vertices
                    #self.triangle.append((self.vertices.index(self.points[0]), self.vertices.index(self.points[1]), self.vertices.index(self.points[2]))) 
                    #self.triangle.append((len(self.vertices)-3, len(self.vertices)-2, len(self.vertices)-1)) 
                    normal = []
                    
                    
    def loadBinaryStl(self, filename):
        fp = open(filename, 'rb')
        header = fp.read(80)


        self.vertices = []
        self.triangle = []
        self.points = []
        self.normal = []


        l = struct.unpack('i',fp.read(4))[0]

        count=0

        while True:
            try:
                self.normal = []
                p = fp.read(12)
                if len(p) == 12:
                    normal = []
                    self.normal.append(struct.unpack('f',p[0:4])[0])
                    self.normal.append(struct.unpack('f',p[4:8])[0])
                    self.normal.append(struct.unpack('f',p[8:12])[0])
                  
                p=fp.read(12)
                if len(p)==12:
                    self.vertices.append(struct.unpack('f',p[0:4])[0])
                    self.vertices.append(struct.unpack('f',p[8:12])[0])
                    self.vertices.append(struct.unpack('f',p[4:8])[0])
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(self.normal[0])
                    self.vertices.append(self.normal[1])
                    self.vertices.append(self.normal[2])
                    

                p=fp.read(12)
                if len(p)==12:
                    self.vertices.append(struct.unpack('f',p[0:4])[0])
                    self.vertices.append(struct.unpack('f',p[8:12])[0])
                    self.vertices.append(struct.unpack('f',p[4:8])[0])
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(self.normal[0])
                    self.vertices.append(self.normal[1])
                    self.vertices.append(self.normal[2])

                p=fp.read(12)
                if len(p)==12:
                    self.vertices.append(struct.unpack('f',p[0:4])[0])
                    self.vertices.append(struct.unpack('f',p[8:12])[0])
                    self.vertices.append(struct.unpack('f',p[4:8])[0])
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(self.normal[0])
                    self.vertices.append(self.normal[1])
                    self.vertices.append(self.normal[2])
                    
                #if len(tri) == 17:

                self.triangle.append((len(self.vertices)-3, len(self.vertices)-2, len(self.vertices)-1))

                count+=1
                fp.read(2)

                if len(p)==0:
                    break
            except EOFError: #when file is finished
                break
        fp.close()
