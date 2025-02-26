from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

def setup():
    return True

def image(data):
    rows = len(data)
    cols = len(data[0])

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"STM Image")
    glOrtho(0, 600, 0, 600, -1, 1)

    def random_color():
        return random.random(), random.random(), random.random()

    square_size = 600 // max(cols, rows)

    def render():
        glClear(GL_COLOR_BUFFER_BIT)

        for i in range(rows):
            for j in range(cols):
                glColor3f(*random_color())

                glBegin(GL_QUADS)
                glVertex2f(j * square_size, i * square_size)
                glVertex2f((j + 1) * square_size, i * square_size)
                glVertex2f((j + 1) * square_size, (i + 1) * square_size)
                glVertex2f(j * square_size, (i + 1) * square_size)
                glEnd()

        glutSwapBuffers()

    glutDisplayFunc(render)

    glutMainLoop()