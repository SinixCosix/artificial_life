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
        self.with_brain = True  

    def set_body(self, body: pymunk.Body):
        self.body = body
        return self

    def set_shape(self, shape: list[int|float]):
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
        self.with_brain = False
        return self

    def build(self) -> 'Organism':
        if self.body is None or self.shape is None:
            raise ValueError("Body and Shape must be set before building Organism")
        
        organism = Organism(
            body=self.body,
            shape=self.shape,
            speed=self.speed,
            energy=self.energy,
            color=self.color
        )
        
        if not self.with_brain:
            organism.brain = None
        
        return organism

    def build_random(self) -> 'Organism':
        body = pymunk.Body(1, random.uniform(50, 500))
        body.position = (random.uniform(0, 800), random.uniform(0, 600))
        shape = pymunk.Poly.create_box(body, (random.uniform(10, 30), random.uniform(10, 30)))
        shape.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
        
        return (self.set_body(body)
                   .set_shape(shape)
                   .set_speed(random.uniform(10, 50))
                   .set_energy(random.uniform(50, 150))
                   .build())

    def build_static(self) -> 'Organism':
        body = pymunk.Body(1, 1)
        body.position = (100, 100)
        return (
            self.set_body(body)
                .set_shape([(-4, -4), (0, 4), (4, -4)])
                .set_speed(30)
                .set_color((255, 255, 0))
                .build()
        )
