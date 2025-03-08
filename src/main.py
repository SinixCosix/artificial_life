import arcade

from ui import MainWindow

def main():
    screen = arcade.get_display_size()
    width, height = screen[0] / 3, screen[1] / 2

    window = MainWindow(width, height)
    arcade.run()


if __name__ == "__main__":
    main()
