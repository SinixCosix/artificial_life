import random

import pymunk

from ai.brain import Brain
from simulation.organism import Organism
from simulation.matter import Matter


class OrganismBuilder:
    def __init__(self):
        self.body = None
        self.shape = None
        self.speed = 20
        self.energy = 100
        self.color = (0, 255, 0) 
        self.has_ai = True  

    def set_body(self, body: pymunk.Body):
        self.body = body
        return self

    def set_shape(self, shape: list[int|float]):
        if self.body is None:
            raise ValueError("Body must be set before setting the shape")
        
        self.shape = pymunk.Poly(self.body, shape)
        return self

    def set_speed(self, speed: float):
        self.speed = speed
        return self

    def set_energy(self, energy: float):
        self.energy = energy
        return self

    def set_color(self, color: tuple):
        self.color = color
        return self

    def disable_brain(self):
        self.has_ai = False
        return self

    def build(self) -> 'Organism':
        if self.body is None or self.shape is None:
            raise ValueError("Body and Shape must be set before building Organism")
        
        organism = Organism(
            body=self.body,
            shape=self.shape,
            speed=self.speed,
            energy=self.energy,
            color=self.color,
        )
        
        if not self.has_ai:
            organism.brain = None
        
        return organism

