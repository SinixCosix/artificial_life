import arcade
import numpy as np

from core import Rigidbody, Space, Transform
from simulation import Organism
from ui import Painter


class MainWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Artificial Life", fullscreen=False)
        arcade.set_background_color(arcade.color.BLACK)

        self.space = Space()
        self.painter = Painter()
        transform = Transform(position=np.array([0, 0]))
        rigidbody = Rigidbody(transform=transform)
        organism = Organism(transform, rigidbody)
        self.space.add(organism)

    def on_draw(self):
        self.clear()

        for organism in self.space.objects:
            self.painter.draw(organism)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.close()

    def on_update(self, delta_time):
        self.space.update()

