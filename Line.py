import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_line():
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)  
    glVertex2f(-0.5, 0.0)  
    glVertex2f(0.5, 0.0)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluOrtho2D(-1, 1, -1, 1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
        
        glClear(GL_COLOR_BUFFER_BIT)  
        draw_line()  
        pygame.display.flip()  
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
