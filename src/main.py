import arcade

class Game(arcade.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

    def on_draw():
        arcade.draw_circle_filled(50, 50, 15, arcade.color.AUBURN)



def main():
    screen = arcade.get_display_size()
    width, height = screen[0] / 3, screen[1] / 2
    window = Game(width, height)

    arcade.run()

if __name__ == "__main__":
    main()
