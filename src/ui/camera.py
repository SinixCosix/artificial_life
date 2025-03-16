import arcade
import numpy as np


class Camera(arcade.Camera2D):
    def __init__(self):
        super().__init__()

        self.speed = 3
        self.velocity = [0, 0]

    def update(self):
        x = self.position[0] + self.velocity[0]
        y = self.position[1] + self.velocity[1]
        self.position = (x, y)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.velocity[1] = self.speed
        elif key == arcade.key.S:
            self.velocity[1] = -self.speed
        elif key == arcade.key.A:
            self.velocity[0] = -self.speed
        elif key == arcade.key.D:
            self.velocity[0] = self.speed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.velocity[1] = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.velocity[0] = 0

    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT or button == arcade.MOUSE_BUTTON_MIDDLE:
            x = self.position[0] - dx
            y = self.position[1] - dy
            self.position = (x, y)