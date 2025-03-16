import arcade
import numpy as np


class Camera(arcade.Camera2D):
    def __init__(self):
        super().__init__()

        self.speed = 3
        self.velocity = [0, 0]
        
        self.zoom = 1.0
        self.min_zoom = 0.1    
        self.max_zoom = 5.0   
        self.zoom_speed = 0.1 

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
        elif key == arcade.key.EQUAL or key == arcade.key.PLUS:
            self.zoom_in()
        elif key == arcade.key.MINUS:
            self.zoom_out()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.velocity[1] = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.velocity[0] = 0

    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT or button == arcade.MOUSE_BUTTON_MIDDLE:
            x = self.position[0] - dx / self.zoom 
            y = self.position[1] - dy / self.zoom
            self.position = (x, y)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        mouse_world_x = self.position[0] + (x - self.viewport_width / 2) / self.zoom
        mouse_world_y = self.position[1] + (y - self.viewport_height / 2) / self.zoom

        if scroll_y > 0:
            self.zoom_in()
        elif scroll_y < 0:
            self.zoom_out()

        new_x = mouse_world_x - (x - self.viewport_width / 2) / self.zoom
        new_y = mouse_world_y - (y - self.viewport_height / 2) / self.zoom
        self.position = (new_x, new_y)

    def zoom_in(self):
        new_zoom = min(self.zoom + self.zoom_speed, self.max_zoom)
        self.zoom = new_zoom

    def zoom_out(self):
        new_zoom = max(self.zoom - self.zoom_speed, self.min_zoom)
        self.zoom = new_zoom
        