from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

win_width, win_height = 500, 500
polygon_points = [(100, 150), (200, 250), (300, 200), (250, 100), (150, 100)]
fill_color = [0.0, 1.0, 0.0]

edges = []

class EdgeBucket:
    def __init__(self, y_max, x, inverse_slope):
        self.y_max = y_max
        self.x = x
        self.inverse_slope = inverse_slope

def draw_polygon():
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for x, y in polygon_points:
        glVertex2f(x, y)
    glEnd()

def scan_fill():
    global edges
    edges = [[] for _ in range(win_height)]

    n = len(polygon_points)
    for i in range(n):
        x1, y1 = polygon_points[i]
        x2, y2 = polygon_points[(i + 1) % n]

        if y1 == y2:
            continue

        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        inverse_slope = (x2 - x1) / (y2 - y1)
        edges[int(y1)].append(EdgeBucket(int(y2), x1, inverse_slope))

    aet = []

    for y in range(win_height):
        aet += edges[y]
        aet = [edge for edge in aet if edge.y_max > y]
        aet.sort(key=lambda e: e.x)

        i = 0
        while i < len(aet) - 1:
            x_start = int(aet[i].x)
            x_end = int(aet[i + 1].x)
            glColor3f(*fill_color)
            glBegin(GL_LINES)
            glVertex2i(x_start, y)
            glVertex2i(x_end, y)
            glEnd()
            i += 2

        for edge in aet:
            edge.x += edge.inverse_slope

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_polygon()
    scan_fill()
    glFlush()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, win_width, 0, win_height)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(win_width, win_height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Concave Polygon - Scan Fill")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
