import numpy as np


class Rigidbody:
    def __init__(self, transform, mass=1.0):
        self.transform = transform
        self.velocity = np.array([0, 0], dtype=float)
        self.mass = mass
        self.forces = np.array([0, 0], dtype=float)

    def apply_force(self, force):
        self.forces += np.array(force, dtype=float)

    def update(self, dt=1.0):
        acceleration = self.forces / self.mass
        self.velocity += acceleration * dt
        self.transform.position += self.velocity * dt
        self.forces = np.array([0, 0], dtype=float)
