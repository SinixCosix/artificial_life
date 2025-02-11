import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

from core import Rigidbody, Space, Transform
from simulation import Organism
from ui import Painter


def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Artificial Life", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    space = Space()
    gluOrtho2D(-100, 100, -100, 100)
    painter = Painter()

    transform = Transform(position=[0, 0])
    rigidbody = Rigidbody(transform=transform)
    organism = Organism(transform, rigidbody)

    space.add(organism)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        space.update()

        for organism in space.objects:
            painter.draw(organism)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
