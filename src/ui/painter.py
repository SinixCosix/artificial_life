import numpy as np
import arcade


class Painter:
    def draw(self, object):
        color = tuple(int(c) for c in np.array(object.color))

        size = object.transform.scale[0]
        x = object.transform.position[0]
        y = object.transform.position[1]

        points = [
            (x - size, y - size),
            (x + size, y - size),
            (x + size, y + size),
            (x - size, y + size)
        ]

        arcade.draw_polygon_filled(points, color)
