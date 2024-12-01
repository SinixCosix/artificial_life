import numpy as np


class Object:
    def __init__(self, element, position, amount=10):
        self.element = element
        self.position = np.array(position, dtype=float)  # Позиция объекта
        self.amount = amount
        self.color = element.color
        self.size = 0.05
