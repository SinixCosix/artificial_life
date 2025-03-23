import pymunk

from core.organism_factory import OrganismFactory

class World:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)

        self.organisms = []
        self.objects = []

        organism = OrganismFactory.create_basic()
        self.add_organism(organism)

    def add_organism(self, organism):
        self.organisms.append(organism)
        self.space.add(organism, organism.shape)

    def update(self, delta_time):
        for organism in self.organisms:
            organism.update()

    def fixed_update(self, delta_time):
        self.space.step(0.1)
