import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    light_position = [1.0, 1.0, 1.0, 1.0]
    light_ambient = [0.2, 0.2, 0.2, 1.0]
    light_diffuse = [1.0, 1.0, 1.0, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    material_diffuse = [0.6, 0.6, 0.6, 1.0]
    material_specular = [1.0, 1.0, 1.0, 1.0]
    material_shininess = [50.0]

    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 10)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

    glRotatef(45, 0, 1, 0)  # Rotar la esfera

    glutSolidSphere(1.0, 20, 20)  # Dibujar la esfera

    glFlush()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(640, 480, "OpenGL Window", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    init()

    while not glfw.window_should_close(window):
        glfw.poll_events()

        display()

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == '__main__':
    glutInit()  # Inicializar GLUT
    main()
