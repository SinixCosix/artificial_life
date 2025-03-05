import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

from core import Rigidbody, Space, Transform
from simulation import Organism
from ui import Painter


def main():
    if not glfw.init():
        return

    monitor = glfw.get_primary_monitor()
    mode = glfw.get_video_mode(monitor)
    width, height = mode.size.width, mode.size.height

    window = glfw.create_window(width, height, "Artificial Life", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.set_window_pos(window, 0, 0)
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
