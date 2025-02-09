import random

import numpy as np
from OpenGL.GL import *
from matter import Matter
import pymunk


class Organism:
    def __init__(self, position, velocity=(-0.01, 0.01), energy=100, color=(0, 255, 0)):
        self.energy = energy
        self.matter = Matter()
        self.color = color
        self.size = 0.02

        mass = 1.0
        moment = pymunk.moment_for_circle(mass, 0, self.size)
        self.body = pymunk.Body(mass, moment)
        self.body.position = position
        self.body.velocity = velocity

        self.shape = pymunk.Circle(self.body, self.size)
        self.shape.elasticity = 1.0  # коэффициент упругости для отражения
        self.shape.friction = 0.5

    def absorb_matter(self, obj):
        amount_to_absorb = min(1, obj.amount)
        self.matter.add_element(obj.element, amount_to_absorb)
        obj.amount -= amount_to_absorb

        # Направление от объекта к организму
        direction = self.position - obj.position
        if np.linalg.norm(direction) != 0:
            direction /= np.linalg.norm(direction)  # Нормализация направления
