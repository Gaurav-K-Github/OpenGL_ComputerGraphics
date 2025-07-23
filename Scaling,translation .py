from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# House coordinates (simple triangle + square)
house = [
    [100, 300],  # bottom-left
    [200, 300],  # bottom-right
    [200, 200],  # top-right
    [100, 200],  # top-left
    [150, 150]   # top of the roof
]

# Copy house for transformations
house_scaled_translated = []
house_scaled_about_point = []

# Function to draw house
def draw_house(points):
    glBegin(GL_LINE_LOOP)
    for i in range(4):
        glVertex2f(points[i][0], points[i][1])
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(points[3][0], points[3][1])  # top-left
    glVertex2f(points[4][0], points[4][1])  # top (roof)

    glVertex2f(points[2][0], points[2][1])  # top-right
    glVertex2f(points[4][0], points[4][1])  # top (roof)
    glEnd()

# Scaling about origin and translation
def scale_and_translate(points, sx, sy, tx, ty):
    result = []
    for x, y in points:
        x_new = x * sx + tx
        y_new = y * sy + ty
        result.append([x_new, y_new])
    return result

# Scaling about an arbitrary point
def scale_about_point(points, sx, sy, refx, refy):
    result = []
    for x, y in points:
        x_new = refx + (x - refx) * sx
        y_new = refy + (y - refy) * sy
        result.append([x_new, y_new])
    return result

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw original house in white
    glColor3f(1, 1, 1)
    draw_house(house)

    # Draw scaled and translated house in red
    glColor3f(1, 0, 0)
    draw_house(house_scaled_translated)

    # Draw scaled about point house in green
    glColor3f(0, 1, 0)
    draw_house(house_scaled_about_point)

    glFlush()

def main():
    global house_scaled_translated, house_scaled_about_point

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"House Scaling and Translation")
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(0, 600, 600, 0)  # (left, right, bottom, top)

    # Precompute the transformations
    house_scaled_translated = scale_and_translate(house, 1.5, 1.5, 100, -50)
    house_scaled_about_point = scale_about_point(house, 1.5, 1.5, 150, 300)

    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
