import random

import glfw
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

from elements import *
from object import Object
from organism import Organism
from ui.painter import Painter

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
                    objects.remove(obj)


def handle_organism_interactions(organisms):
    for i in range(len(organisms)):
        for j in range(i + 1, len(organisms)):
            organisms[i].repel(organisms[j])


def main():
    if not glfw.init():
        return
    window = glfw.create_window(800, 600, "Artificial Life", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    gluOrtho2D(-1, 1, -1, 1)
    painter = Painter()

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        handle_organism_interactions(organisms)

        for organism in organisms:
            organism.update()
            painter.draw(organism)

        for obj in objects:
            painter.draw(obj)

        check_collisions(organisms, objects)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
