import arcade

import simulation

class Renderer():
    @staticmethod
    def render(object: simulation.Organism):
        poly = [object.body.local_to_world(vertex) for vertex in object.shape.get_vertices()]
        arcade.draw_polygon_filled(poly, object.color)
        