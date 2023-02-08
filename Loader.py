import struct

class Load:
    def __init__(self) -> None:
        self.vertices = []
        self.triangles = 0
        self.points = []
        self.count = 0

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
        fp = open(filename, 'r')
        self.normal = []
        for line in fp.readlines():
            words = line.split()
            if len(words) > 0:
                
                if words[0] == 'facet':
                    #name = words[1]
                    self.normal.append(eval(words[2]))
                    self.normal.append(eval(words[3]))
                    self.normal.append(eval(words[4]))

                if words[0] == 'vertex':
                    #final list of vertices
                    self.vertices.append(eval(words[1]))
                    self.vertices.append(eval(words[2]))
                    self.vertices.append(eval(words[3]))
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(1.00000000000000)
                    self.vertices.append(self.normal[0])
                    self.vertices.append(self.normal[1])
                    self.vertices.append(self.normal[2])
                    

                if words[0] == 'endloop':
                    #for OpenGL to create the triangle, we get the index of the vertex in the list vertices
                    #self.triangle.append((self.vertices.index(self.points[0]), self.vertices.index(self.points[1]), self.vertices.index(self.points[2]))) 
                    #self.triangle.append((len(self.vertices)-3, len(self.vertices)-2, len(self.vertices)-1)) 
                    self.normal = []
                    
                    
    def loadBinaryStl(self, filename):
        fp = open(filename, 'rb')
        header = fp.read(80)


        self.vertices = []
        self.triangles = 0
        self.normal = []
        


        l = struct.unpack('i',fp.read(4))[0]
        self.triangles = l


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


                self.count += 1
                fp.read(2)

                if len(p)==0:
                    break
            except EOFError: #when file is finished
                break
        fp.close()
    
    def returnCount(self):
        return self.count
    def returnTriangles(self):
        return self.triangles
