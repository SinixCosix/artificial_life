import arcade
import pymunk

from simulation.organism_builder import OrganismBuilder

from .camera import Camera
from .renderer import Renderer

class WorldView(arcade.View):
    def __init__(self):
        super().__init__()

        self.camera = Camera()
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)
        
        # move organism to somewhere else. for example World class which
        # which contains organisms, food, objects and etc...
        self.organism = OrganismBuilder.build_primitive()
        self.space.add(self.organism.body, self.organism.shape)

    def on_draw(self):
        self.clear()
        self.camera.use()

        center = arcade.XYWH(-2.5, -2.5, 5, 5)
        arcade.draw_rect_filled(center, (255, 255, 255))
        
        Renderer.render(self.organism)

    def on_update(self, delta_time):
        self.camera.on_update()

    def on_fixed_update(self, delta_time):
        self.organism.update()
        self.space.step(0.1)

    def on_key_press(self, key, modifiers):
        self.camera.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.camera.on_key_release(key, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        self.camera.on_mouse_drag(x, y, dx, dy, button, modifiers)

