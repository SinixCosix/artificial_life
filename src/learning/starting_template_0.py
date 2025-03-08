import arcade

class Game(arcade.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

        self.ball_x = 50
        self.ball_y = 50


    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.AUBURN)

    def on_update(self, delta_time):
        self.ball_x += 1
        self.ball_y += 1



def main():
    screen = arcade.get_display_size()
    width, height = screen[0] / 3, screen[1] / 2
    window = Game(width, height)

    arcade.run()

if __name__ == "__main__":
    main()
