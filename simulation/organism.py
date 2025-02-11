import numpy as np
from simulation.matter import Matter


class Organism:
    def __init__(self, transform, rigidbody, energy=100, color=(0, 255, 0)):
        self.energy = energy
        self.color = color
        self.matter = Matter()

        self.transform = transform
        self.rigidbody = rigidbody

        self.velocity = np.array([0, 0.1])

    def update(self):
        self.rigidbody.transform.position += self.velocity
