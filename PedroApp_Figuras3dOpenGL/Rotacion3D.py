import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Variables globales
rotacion = 0.0


def main():
    # Inicializar GLFW
    if not glfw.init():
        return

    # Configurar ventana y contexto OpenGL
    window = glfw.create_window(640, 480, "OpenGL Window", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # Registrar funciones de retrollamada
    glfw.set_key_callback(window, key_callback)

    # Configurar proyección y modelo de vista
    reshape(window, 640, 480)

    # Ciclo principal
    while not glfw.window_should_close(window):
        # Borrar el búfer de color
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Dibujar
        display()

        # Intercambiar los buffers de frente y atrás
        glfw.swap_buffers(window)

        # Escuchar eventos y actualizar el estado
        glfw.poll_events()

    # Terminar GLFW
    glfw.terminate()


def key_callback(window, key, scancode, action, mods):
    global rotacion

    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)
    elif key == glfw.KEY_R and action == glfw.PRESS:
        rotacion += 5.0


def display():
    global rotacion

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    gluLookAt(2.0, 2.0, 6.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glRotatef(rotacion, 0.0, 1.0, 0.0)

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(0.0, 0.0, -1.0)
    glEnd()

    # ...
    # Aquí puedes agregar más dibujos y configuraciones OpenGL
    # ...

    glFlush()


def reshape(window, width, height):
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, width / height, 0.1, 10.0)


if __name__ == '__main__':
    main()
