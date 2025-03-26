import arcade

import simulation


class Renderer:
    def __init__(self):
        self.sprite_list = arcade.SpriteList()
        self.sprite_map = {}

    def initialize(self, items):
        for item in items:
            sprite = self.create_sprite(item)
            self.sprite_list.append(sprite)
            self.sprite_map[item] = sprite

    def create_sprite(self, item):
        sprite = arcade.SpriteSolidColor(20, 20, item.color)
        sprite.position = item.position

        return sprite

    def update(self, items):
        for item in items:
            sprite = self.sprite_map.get(item)
            if sprite:
                sprite.position = item.position
                sprite.color = item.color

    def render(self, items):
        self.update(items)
        self.sprite_list.draw()
