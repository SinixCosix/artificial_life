import pymunk

from .organism import Organism
import ai


class OrganismBuilder():
    @staticmethod
    def build_from_fixture(path_to_fixture):
        pass

    @staticmethod
    def build_primitive__random():
        pass

    @staticmethod
    def build_primitive():
        body = pymunk.Body(1, 1)
        body.position = (50.0, 50.0)
        shape = pymunk.Poly(
            body,
            [(-10, -10), (5, -5), (10, 10)],
        )
        organism = Organism(
            body,
            shape,
        )

        return organism

    @staticmethod
    def build_no_ai():
        pass