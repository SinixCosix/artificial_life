import numpy as np
import pymunk

from .task import Task


class WaypointTask(Task):
    def __init__(self, waypoint, organism):
        self.waypoint = pymunk.Vec2d(*waypoint)
        self.threshold = 1.1
        self.organism = organism

    def do(self):
        distance = self.waypoint - self.organism.body.position
        distance_x = abs(distance.x)
        distance_y = abs(distance.y)

        if distance_x < self.threshold and distance_y < self.threshold:
            self.organism.body.velocity = pymunk.Vec2d(0, 0)
            return True

        direction = np.sign([distance.x, distance.y])
        norm_dir = pymunk.Vec2d(
            direction[0] if direction[0] != 0 else 0,
            direction[1] if direction[1] != 0 else 0
        )
        self.organism.body.velocity = norm_dir * self.organism.speed
        return False
