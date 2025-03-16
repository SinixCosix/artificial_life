from simulation.matter import Matter
from ai.brain import Brain

class Organism:
    def __init__(self, body, shape, speed=20, energy=100, color=(0, 255, 0)):
        self.energy = energy
        self.color = color
        self.matter = Matter()

        self.brain = Brain(self)
        self.body = body
        self.shape = shape

        self.speed = speed


    def update(self):
        if (self.brain):
            self.brain.update()
