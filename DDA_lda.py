from OpenGL.GL import *
from OpenGL.GLUT import *

x1, y1 = 50, 100
x2, y2 = -50, 300

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    glBegin(GL_POINTS)
    for _ in range(int(steps)):
        glVertex2f(x / 400, y / 400) 
        x += x_inc
        y += y_inc
    glEnd()

    glFlush()

glutInit()
glutInitWindowSize(400, 400)
glutCreateWindow(b"DDA Line Drawing")
glutDisplayFunc(display)
glutMainLoop()
