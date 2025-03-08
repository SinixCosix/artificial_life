import arcade

from ui import MainWindow

def main():
    screen = arcade.get_display_size()
    width, height = screen[0] / 3, screen[1] / 2
    arcade.open_window(width, height)
    arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

    arcade.start_render()
    arcade.draw_lrbt_rectangle_filled(0, width, 0, height / 3, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_polygon_filled((
        (40, 40),
        (45, 60),
        (35, 89),
        (40, 55),
    ), arcade.csscolor.SIENNA)
    arcade.draw_line(100, 150, 200, 150, arcade.color.YELLOW, 3)
    arcade.finish_render()

    arcade.run()

if __name__ == "__main__":
    main()
