from OpenGL.GL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.arrays import vbo
import ctypes

class Shader:
    def __init__(self, vertexPath, fragmentPath) -> None:
        fragmentPath = open(fragmentPath, 'r')
        vertexPath = open(vertexPath, 'r')

        vertex_shader_source = vertexPath.read()
        fragment_shader_source = vertexPath.read()

        fragmentPath.close()
        vertexPath.close()


        vertex_shader = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vertex_shader, vertex_shader_source) # passing the source code as string
        glCompileShader(vertex_shader)
        


        fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fragment_shader, fragment_shader_source)
        glCompileShader(fragment_shader)

        # Create the program
        self.ID = glCreateProgram()
        glAttachShader(self.ID, vertex_shader)
        glAttachShader(self.ID, fragment_shader)
        glLinkProgram(self.ID)

        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)
    
    def use(self):
        glUseProgram(self.ID)
    

shader = Shader("shaders/vertexShader.vs", "shaders/fragmentShader.fs")