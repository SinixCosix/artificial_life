import arcade

import ui


class MainWindow(arcade.Window):
    def __init__(self):
        screen = arcade.get_display_size()
        width, height = int(screen[0] / 3), (screen[1] / 2)
        super().__init__(width, height, "Artificial Life", fullscreen=False,)
        arcade.set_background_color(arcade.color.BLACK)

        world_view = ui.WorldView()
        self.show_view(world_view)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.close()
