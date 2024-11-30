import random

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

from elements import *
from organism import Organism

organisms = [
    Organism(position=[random.uniform(-0.9, 0.9), random.uniform(-0.9, 0.9)])
    for _ in range(5)
]


def main():
    if not glfw.init():
        return
    window = glfw.create_window(800, 600, "Artificial Life", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    gluOrtho2D(-1, 1, -1, 1)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        for organism in organisms:
            organism.move()
            organism.draw()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
