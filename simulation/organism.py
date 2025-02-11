import numpy as np
from simulation.matter import Matter


class Organism:
    def __init__(self, position, velocity=(-0.01, 0.01), energy=100, color=(0, 255, 0)):
        self.energy = energy
        self.matter = Matter()
        self.color = color
        self.size = 3

        self.position = np.array(position, dtype='float')
        self.velocity = np.array(velocity, dtype='float')

    def update(self):
        self.position += self.velocity
