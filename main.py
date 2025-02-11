import random

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

from simulation.organism import Organism
from ui.painter import Painter
from core.space import Space


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

    space = Space()
    gluOrtho2D(-100, 100, -100, 100)
    painter = Painter()

    organisms = []
    organism = Organism(
        position=(0.01, 0.01),
        velocity=(0.4, 0),
    )

    organisms.append(organism)
    space.add(organism)

    # organism = Organism(
    #     position=(0.2, 0.01),
    #     velocity=(-0.4, 0),
    #     color=(0, 0, 255),
    # )
    # organisms.append(organism)
    # space.add(organism)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        space.update()

        for organism in organisms:
            painter.draw(organism)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
