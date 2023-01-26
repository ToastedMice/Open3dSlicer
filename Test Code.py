import pygame
from OpenGL.GL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.arrays import vbo
import ctypes
import glm
import Loader

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)

clock = pygame.time.Clock()

vertex_shader_source = """
#version 330
uniform mat4 projection;
uniform mat4 view;
uniform mat4 model;
in vec3 position;
in vec4 color;
in vec3 normal;

out vec3 v_normal;
out vec4 v_color;
void main() {
    gl_Position = projection * view * model * vec4(position, 1.0);
    v_color = color;
    v_normal = normal;
}
"""

fragment_shader_source = """
#version 330
out vec4 frag_color;
in vec4 v_color;

in vec3 v_normal;
void main() {
    vec4 normalizedv_normal = normalize(vec4(v_normal, 0.0));
    vec4 light_direction = normalize(vec4(1.0,1.0,1.0,0.0));
    float diffuse = dot(normalizedv_normal,light_direction);
    frag_color = v_color * diffuse;
}
"""

# Compile the shaders
vertex_shader = glCreateShader(GL_VERTEX_SHADER)
glShaderSource(vertex_shader, vertex_shader_source) # passing the source code as string
glCompileShader(vertex_shader)


fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
glShaderSource(fragment_shader, fragment_shader_source)
glCompileShader(fragment_shader)

# Create the program
shader_program = glCreateProgram()
glAttachShader(shader_program, vertex_shader)
glAttachShader(shader_program, fragment_shader)
glLinkProgram(shader_program)

mesh = Loader.Load()
mesh.load("C:/Users/aidan_i6wswtz/Downloads/Ascii.stl")

triangle_vertices = mesh.vertices
triangle_vertices = (ctypes.c_float * len(triangle_vertices))(*triangle_vertices)

vbo = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, ctypes.sizeof(triangle_vertices), triangle_vertices, GL_STATIC_DRAW)
#glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
#gluPerspective(90, float((800/600)), 0.1, 1000.0)

glEnable(GL_DEPTH_TEST)
glShadeModel(GL_FLAT)

# Create the projection matrix
projection = glm.perspective(glm.radians(45.0), 800/600, 0.1, 100.0)

# Create the view matrix
view = glm.lookAt(glm.vec3(3, 3, 3), glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))

# Create the model matrix
model = glm.mat4(1.0)
model = glm.translate(model, glm.vec3(0.0, 0.0, 0.0))
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)
    glClearColor(0.1, 0.2, 0.2, 1)

    # Use the program
    glUseProgram(shader_program)

    # Bind the vertex buffer object
    glBindBuffer(GL_ARRAY_BUFFER, vbo)

    # Enable the vertex attribute
    position = glGetAttribLocation(shader_program, "position")
    glEnableVertexAttribArray(position)
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE,  10 * ctypes.sizeof(ctypes.c_float), None)

    color = glGetAttribLocation(shader_program, "color")
    glEnableVertexAttribArray(color)
    glVertexAttribPointer(color, 4, GL_FLOAT, GL_FALSE, 10 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(3 * ctypes.sizeof(ctypes.c_float)))

    normal = glGetAttribLocation(shader_program, "normal")
    glEnableVertexAttribArray(normal)
    glVertexAttribPointer(normal, 3, GL_FLOAT, GL_TRUE, 10 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(7 * ctypes.sizeof(ctypes.c_float)))

    projection_loc = glGetUniformLocation(shader_program, "projection")
    glUniformMatrix4fv(projection_loc, 1, GL_FALSE, glm.value_ptr(projection))

    view_loc = glGetUniformLocation(shader_program, "view")
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, glm.value_ptr(view))

    model_loc = glGetUniformLocation(shader_program, "model")
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, glm.value_ptr(model))

    # Draw the triangle
    model = glm.rotate(model, glm.radians(2.0), glm.vec3(1, 1, 0))

    glDrawArrays(GL_TRIANGLES, 0, int(len(triangle_vertices) / 10)) # 7 components per attrribute tuple)
    
    # Disable the vertex attribute
    glDisableVertexAttribArray(position)
    glDisableVertexAttribArray(color)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    
    

    # Swap the buffers
    pygame.display.flip()
    clock.tick(60)