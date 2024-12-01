import random

import numpy as np
from OpenGL.GL import *
from matter import Matter


class Organism:
    def __init__(self, position, velocity=None, energy=100):
        if velocity is None:
            velocity = [-0.01, 0.01]

        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.energy = energy
        self.matter = Matter()
        self.color = (0, 255, 0)

    def update(self):
        self.adjust_velocity_based_on_mass()
        self.move()

    def adjust_velocity_based_on_mass(self):
        pass

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

        # Направление от объекта к организму
        direction = self.position - obj.position
        if np.linalg.norm(direction) != 0:
            direction /= np.linalg.norm(direction)  # Нормализация направления

        # Отталкивание от объекта: меняем только направление, оставляя скорость постоянной
        self.velocity = -direction * np.linalg.norm(self.velocity)  # Противоположное направление

    def draw(self):
        glColor3f(*np.array(self.color) / 255.0)
        glBegin(GL_QUADS)
        size = 0.05
        glVertex2f(self.position[0] - size, self.position[1] - size)
        glVertex2f(self.position[0] + size, self.position[1] - size)
        glVertex2f(self.position[0] + size, self.position[1] + size)
        glVertex2f(self.position[0] - size, self.position[1] + size)
        glEnd()

    def repel(self, other, min_distance=0.1):
        distance = np.linalg.norm(self.position - other.position)
        if distance < min_distance:
            direction = self.position - other.position
            if np.linalg.norm(direction) == 0:
                direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)])
            direction = direction / np.linalg.norm(direction)

            random_offset = np.array([random.uniform(-0.01, 0.01), random.uniform(-0.01, 0.01)])

            self.velocity += direction * 0.01 + random_offset
            other.velocity -= direction * 0.01 + random_offset
