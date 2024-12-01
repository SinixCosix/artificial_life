import random

import numpy as np
from OpenGL.GL import *
from matter import Matter


class Organism:
    def __init__(self, position, velocity=None, energy=100):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity if velocity else [random.uniform(-0.01, 0.01) for _ in range(2)], dtype=float)
        self.energy = energy
        self.matter = Matter()  # Материя внутри организма
        self.color = (0, 255, 0)  # Зеленый цвет для визуализации организмов

    def move(self):
        self.position += self.velocity

        # Отражение от границ мира
        if self.position[0] >= 1 or self.position[0] <= -1:
            self.velocity[0] = -self.velocity[0]
            self.position[0] = np.clip(self.position[0], -1, 1)

        if self.position[1] >= 1 or self.position[1] <= -1:
            self.velocity[1] = -self.velocity[1]
            self.position[1] = np.clip(self.position[1], -1, 1)

    def absorb_matter(self, obj):
        amount_to_absorb = min(1, obj.amount)
        self.matter.add_element(obj.element, amount_to_absorb)
        obj.amount -= amount_to_absorb
        print(f"Организм поглотил {amount_to_absorb} единиц {obj.element.symbol}. Остаток в объекте: {obj.amount}")

    def draw(self):
        glColor3f(*np.array(self.color) / 255.0)
        glBegin(GL_QUADS)
        size = 0.05
        glVertex2f(self.position[0] - size, self.position[1] - size)
        glVertex2f(self.position[0] + size, self.position[1] - size)
        glVertex2f(self.position[0] + size, self.position[1] + size)
        glVertex2f(self.position[0] - size, self.position[1] + size)
        glEnd()
