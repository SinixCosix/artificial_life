import random

import numpy as np
from OpenGL.GL import *
from matter import Matter


class Object:
    def __init__(self, element, position, amount=10):
        self.element = element
        self.position = np.array(position, dtype=float)  # Позиция объекта
        self.amount = amount
        self.color = element.color

    def draw(self):
        glColor3f(*np.array(self.color) / 255.0)
        glBegin(GL_QUADS)
        size = 0.04 * (self.amount / 10)  # Масштабируем размер по количеству вещества
        glVertex2f(self.position[0] - size, self.position[1] - size)
        glVertex2f(self.position[0] + size, self.position[1] - size)
        glVertex2f(self.position[0] + size, self.position[1] + size)
        glVertex2f(self.position[0] - size, self.position[1] + size)
        glEnd()
