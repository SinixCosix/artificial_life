import numpy as np


class Transform:
    left = np.array((-1, 0), dtype=float)
    right = np.array((-1, 0), dtype=float)
    up = np.array((-1, 0), dtype=float)
    down = np.array((-1, 0), dtype=float)

    def __init__(self, position=(0, 0), rotation=0, scale=(1, 1)):
        self.position = np.array(position, dtype=float)
        self.rotation = rotation
        self.scale = np.array(scale, dtype=float)

    def translate(self, x, y):
        self.position += np.array([x, y])

    def rotate(self, angle):
        self.rotation += angle

    def set_scale(self, x, y):
        self.scale = np.array([x, y])
