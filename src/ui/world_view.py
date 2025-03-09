import arcade

from .camera import Camera

class WorldView(arcade.View):
    def __init__(self):
        super().__init__()

        self.camera = Camera()

    def on_draw(self):
        self.clear()

        a = arcade.XYWH(0, 0, 40, 50)
        arcade.draw_rect_filled(a, (133, 154, 55))
        self.camera.use()

    def on_update(self, delta_time):
        self.camera.on_update()
        

    def on_key_press(self, key, modifiers):
        self.camera.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.camera.on_key_release(key, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        self.camera.on_mouse_drag(x, y, dx, dy, button, modifiers)

