import pymunk

from core.organism_builder import OrganismBuilder


class OrganismFactory:
    @staticmethod
    def create_predator():
        pass

    @staticmethod
    def create_prey():
        pass

    @staticmethod
    def create_random():
        pass

    @staticmethod
    def create_basic():
        builder = OrganismBuilder()
        
        body = pymunk.Body(1, 1)
        body.position = (100, 100)

        return (
            builder.set_body(body)
                .set_shape([(-4, -4), (0, 4), (4, -4)])
                .set_speed(30)
                .set_color((255, 255, 0))
                .build()
        )

    @staticmethod
    def create_from_json(file_path):
        pass
