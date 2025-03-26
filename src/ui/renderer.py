import arcade

import simulation


class Renderer:
    def __init__(self):
        self.shape_list = arcade.shape_list.ShapeElementList()

    def initialize(self, items):
        for item in items:
            vertices = item.shape.get_vertices()
            shape = [item.local_to_world(vertex) for vertex in vertices]
            shape = arcade.shape_list.create_polygon(shape, item.color)
            self.shape_list.append(shape)

    def render(self, items):
        self.shape_list.clear()
        self.initialize(items)
        self.shape_list.draw()
