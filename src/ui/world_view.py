import arcade
import pymunk

from core.organism_builder import OrganismBuilder
from simulation.world import World
from .camera import Camera
from .renderer import Renderer

class WorldView(arcade.View):
    def __init__(self):
        super().__init__()

        self.camera = Camera()
        self.world = World()

    def on_draw(self):
        self.clear()
        self.camera.use()

        center = arcade.XYWH(-2.5, -2.5, 5, 5)
        arcade.draw_rect_filled(center, (255, 255, 255))

        Renderer.render(self.world.organisms)
        Renderer.render(self.world.objects)

    def on_update(self, delta_time):
        self.camera.update()
        self.world.update(delta_time)

    def on_fixed_update(self, delta_time):
        self.world.fixed_update(delta_time)

    def on_key_press(self, key, modifiers):
        self.camera.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.camera.on_key_release(key, modifiers)

    def on_mouse_drag(self, *args):
        self.camera.on_mouse_drag(*args)

