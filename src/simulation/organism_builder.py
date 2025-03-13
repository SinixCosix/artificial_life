from .organism import Organism
import core
import ai
import pymunk


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

        organism.task = ai.RouteTask(
            organism,
            [
                (100, 50),
                (115, 411),
                (341, 118),
                (111, 156),
                (410, 403),
                (131, 212),
                (100, 50),
            ]
        )

        return organism

    @staticmethod
    def build_no_ai():
        pass