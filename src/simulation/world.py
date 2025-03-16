import pymunk
from simulation.organism_builder import OrganismBuilder

class World:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)

        self.organisms = []
        self.objects = []

        builder = OrganismBuilder()
        organism = builder.build_static()
        self.add_organism(organism)

    def add_organism(self, organism):
        self.organisms.append(organism)
        self.space.add(organism.body, organism.shape)

    def update(self, delta_time):
        for organism in self.organisms:
            organism.update()

    def fixed_update(self, delta_time):
        self.space.step(0.1)
