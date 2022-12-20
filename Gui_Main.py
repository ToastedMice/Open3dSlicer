import pygame
from pygame.locals import *

import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *

import Loader

import subprocess

import ctypes

buildSizeX = 200
buildSizeY = 200

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)
surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
)
colours = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)
mesh = Loader.Load()
#mesh.load("C:/Users/aidan/Downloads/Cube.stl")
mesh.load("C:/Users/aidan/Downloads/CubeTextAsci.stl")
vertices = mesh.vertices
surfaces = mesh.triangle
print(vertices)

def Cube():
    glBegin(GL_TRIANGLES)
    for surface in surfaces:
        x = 0

        for vertex in surface:
            x += 1
            glColor3fv(colours[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    #glBegin(GL_LINES)
    #for edge in edges:
    #    for vertex in edge:
    #        glVertex3fv(vertices[vertex])
    #glEnd()

def createBuffer(vertices):
    bufferdata = (ctypes.c_float*len(vertices))(*vertices) # float buffer
    buffersize = len(vertices)*4                           # buffer size in bytes 

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, buffersize, bufferdata, GL_STATIC_DRAW) 
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    return vbo

def drawBuffer(vbo, noOfVertices):
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, None)

    glDrawArrays(GL_POINTS, 0, noOfVertices)

    glDisableClientState(GL_VERTEX_ARRAY)
    glBindBuffer(GL_ARRAY_BUFFER, 0)



def main():
    pygame.init()
    display = (1400, 1300)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)

    gluPerspective(90, float((display[0]/display[1])), 0.1, 1000.0)
    

    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    glTranslatef(0, 10, -70)

    glRotatef(90, 10, 0, 0)

    bufferObj = createBuffer(vertices)
    numberOfPoints  = len(vertices) // 3
    
    mousePosition = pygame.mouse.get_rel()
    lastPressed = False

    while True:
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #Cube()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, 0.5, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -0.5, 0)
        if pygame.mouse.get_pressed() == (1, 0, 0):
            mousePosition = pygame.mouse.get_rel()
            print(mousePosition)
            glRotatef(mousePosition[0]/3, 0, 0, 1)
            glRotatef(mousePosition[1]/3, 1, 0, 0)

        else:
            mousePosition = pygame.mouse.get_rel()

        drawBuffer(bufferObj, numberOfPoints)

        pygame.display.flip()
        #pygame.time.wait(1)


main()