import random

import numpy as np
from OpenGL.GL import *
from matter import Matter


class Organism:
    def __init__(self, position, velocity=(-0.01, 0.01), energy=100, color=(0, 255, 0)):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.energy = energy
        self.matter = Matter()
        self.color = color
        self.size = 0.02

    def update(self):
        self.adjust_velocity_based_on_mass()
        self.move()

    def adjust_velocity_based_on_mass(self):
        pass

    def move(self):
        self.position += self.velocity

        # Отражение от границ мира
        if self.position[0] >= 1 or self.position[0] <= -1:
            self.velocity[0] = -self.velocity[0]
            self.position[0] = np.clip(self.position[0], -1, 1)

        if self.position[1] >= 1 or self.position[1] <= -1:
            self.velocity[1] = -self.velocity[1]
            self.position[1] = np.clip(self.position[1], -1, 1)

    def absorb_matter(self, obj):
        amount_to_absorb = min(1, obj.amount)
        self.matter.add_element(obj.element, amount_to_absorb)
        obj.amount -= amount_to_absorb

        # Направление от объекта к организму
        direction = self.position - obj.position
        if np.linalg.norm(direction) != 0:
            direction /= np.linalg.norm(direction)  # Нормализация направления

        # Отталкивание от объекта: меняем только направление, оставляя скорость постоянной
        self.velocity = -direction * np.linalg.norm(self.velocity)  # Противоположное направление

    def repel(self, other):
        """
        Обработка столкновения с другим организмом.
        Если организмы пересекаются (накладываются), то корректируем их положение
        и скорость так, чтобы они оттолкнулись друг от друга.
        """
        diff = self.position - other.position
        distance = np.linalg.norm(diff)
        min_distance = self.size + other.size  # минимальное допустимое расстояние между центрами

        if distance < min_distance:
            # Если центры совпадают, зададим случайное направление, чтобы избежать деления на 0
            if distance == 0:
                diff = np.random.rand(2) - 0.5
                distance = np.linalg.norm(diff)
            norm_diff = diff / distance
            # Определяем величину перекрытия
            overlap = min_distance - distance

            # Корректируем позиции: отодвигаем каждый организм на половину перекрытия
            self.position += norm_diff * (overlap / 2)
            other.position -= norm_diff * (overlap / 2)

            # Корректируем скорости для имитации упругого столкновения.
            # Коэффициент можно настроить (например, 0.01 или другой подходящий коэффициент).
            repulsion_strength = 0.01
            self.velocity += norm_diff * repulsion_strength
            other.velocity -= norm_diff * repulsion_strength