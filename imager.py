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

    square_size = min(600 // cols, 600 // rows)

    x_offset = (600 - square_size * cols) / 2
    y_offset = (600 - square_size * rows) / 2

    def render():
        glClear(GL_COLOR_BUFFER_BIT)

        for i in range(rows):
            for j in range(cols):
                glColor3f(*random_color())

                glBegin(GL_QUADS)
                glVertex2f(j * square_size + x_offset, i * square_size + y_offset)
                glVertex2f((j + 1) * square_size + x_offset, i * square_size + y_offset)
                glVertex2f((j + 1) * square_size + x_offset, (i + 1) * square_size + y_offset)
                glVertex2f(j * square_size + x_offset, (i + 1) * square_size + y_offset)
                glEnd()

        glutSwapBuffers()

    glutDisplayFunc(render)

    glutMainLoop()