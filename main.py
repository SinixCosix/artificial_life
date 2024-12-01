import random

import glfw
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

from elements import *
from object import Object
from organism import Organism

organisms = [
    Organism(position=[random.uniform(-0.9, 0.9), random.uniform(-0.9, 0.9)])
    for _ in range(5)
]

objects = [
    Object(ELEMENTS["C"], [random.uniform(-0.9, 0.9), random.uniform(-0.9, 0.9)], amount=random.randint(5, 15))
    for _ in range(20)
]


def check_collisions(organisms, objects):
    for organism in organisms:
        for obj in objects:
            distance = np.linalg.norm(organism.position - obj.position)
            if distance < 0.1:
                organism.absorb_matter(obj)
                if obj.amount <= 0:
                    objects.remove(obj)  # Удаление объекта, если его материя исчерпана


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

        for obj in objects:
            obj.draw()

        check_collisions(organisms, objects)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
