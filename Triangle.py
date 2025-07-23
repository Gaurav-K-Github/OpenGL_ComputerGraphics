from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 500

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    gluOrtho2D(-width // 2, width // 2, -height // 2, height // 2)  # Centered coordinate system

def draw_line():
    glColor3f(1.0, 1.0, 1.0)  # White color
    glBegin(GL_LINES)
    glVertex2f(0, -100)  # Starting point
    glVertex2f(0, 100)    # Ending point
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_line()
    glFlush()

# GLUT setup
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutCreateWindow(b"Simple Line")
init()
glutDisplayFunc(display)
glutMainLoop()
