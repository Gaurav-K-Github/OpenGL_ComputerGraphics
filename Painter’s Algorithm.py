from OpenGL.GL import *       
from OpenGL.GLUT import *     
from OpenGL.GLU import *      
import sys
import math

width, height = 500, 500

translate_x, translate_y = 0.5, 0.3  
rotate_angle = 45                   
scale_x, scale_y = 1.5, 0.5         

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)      
    glColor3f(0.0, 0.0, 0.0)             
    glMatrixMode(GL_PROJECTION)         
    glLoadIdentity()                    
    gluOrtho2D(-1.0, 2.0, -1.0, 2.0)     

def draw_triangle():
    glBegin(GL_TRIANGLES)               
    glVertex2f(0.0, 0.0)                
    glVertex2f(0.0, 1.0)                
    glVertex2f(1.0, 0.0)                
    glEnd()                             

def display():
    glClear(GL_COLOR_BUFFER_BIT)        

    glColor3f(0.0, 0.0, 1.0)            
    draw_triangle()

    glPushMatrix()                      
    glTranslatef(translate_x, translate_y, 0.0)  
    glRotatef(rotate_angle, 0.0, 0.0, 1.0)       
    glScalef(scale_x, scale_y, 1.0)             
    glColor3f(1.0, 0.0, 0.0)            
    draw_triangle()
    glPopMatrix()                       

    glFlush()                           

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"2D Triangle Transformation")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
