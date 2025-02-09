import random

import glfw
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
import pymunk

from elements import *
from object import Object
from organism import Organism
from ui.painter import Painter


def create_random_organisms():
    return [
        Organism(position=[random.uniform(-0.9, 0.9), random.uniform(-0.9, 0.9)])
        for _ in range(5)
    ]


objects = [
    # Object(ELEMENTS["C"], [random.uniform(-0.9, 0.9), random.uniform(-0.9, 0.9)], amount=random.randint(5, 15))
    # for _ in range(20)
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
    painter = Painter()

    space = pymunk.Space()
    space.gravity = (0, 0)

    static_lines = [
        pymunk.Segment(space.static_body, (-1, -1), (1, -1), 0.0),
        pymunk.Segment(space.static_body, (1, -1), (1, 1), 0.0),
        pymunk.Segment(space.static_body, (1, 1), (-1, 1), 0.0),
        pymunk.Segment(space.static_body, (-1, 1), (-1, -1), 0.0),
    ]

    for line in static_lines:
        line.elasticity = 1.0
        space.add(line)

    organisms = []
    organism = Organism(
        position=(0.01, 0.01),
        velocity=(0.4, 0),
    )

    organisms.append(organism)
    space.add(organism.body, organism.shape)

    organism = Organism(
        position=(0.2, 0.01),
        velocity=(-0.4, 0),
        color=(0, 0, 255),
    )
    organisms.append(organism)
    space.add(organism.body, organism.shape)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        dt = 1 / 30.0
        space.step(dt)

        for organism in organisms:
            painter.draw(organism)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
