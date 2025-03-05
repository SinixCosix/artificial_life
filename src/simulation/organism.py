import numpy as np

from artificial_intelligence.tasks.task import RouteTask, WaypointTask
from simulation.matter import Matter


class Organism:
    def __init__(self, transform, rigidbody, speed=0.4, energy=100, color=(0, 255, 0)):
        self.energy = energy
        self.color = color
        self.matter = Matter()

        self.transform = transform
        self.rigidbody = rigidbody

        self.speed = speed
        self.velocity = np.array([0, self.speed])
        self.task = RouteTask(
            [
                (1, 1),
                (15, 11),
                (31, 18),
                (11, 16),
                (41, 43),
                (31, 12),
                (1, 1),

            ],
            self,
        )

        self.task = WaypointTask((-4, -4), self)

    def update(self):
        self.rigidbody.transform.position += self.velocity
        self.task.update()
