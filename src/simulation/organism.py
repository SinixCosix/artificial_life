import numpy as np

from ai.tasks import RouteTask
from simulation.matter import Matter


class Organism:
    def __init__(self, body, shape, speed=20, energy=100, color=(0, 255, 0)):
        self.energy = energy
        self.color = color
        self.matter = Matter()

        self.body = body
        self.shape = shape

        self.speed = speed
        self.task = None
        # TODO: self.brain = Brain # task manager


    def update(self):
        self.task.do()
