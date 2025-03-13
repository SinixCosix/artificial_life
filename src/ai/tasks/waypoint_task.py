import numpy as np
import pymunk

from .task import Task


class WaypointTask(Task):
    def __init__(self, waypoint, organism):
        self.waypoint = pymunk.Vec2d(*waypoint)
        self.threshold = 1.01
        self.organism = organism

    def do(self):
        position = self.organism.body.position
        distance = position - self.waypoint
        distance_x = abs(distance.x)
        distance_y = abs(distance.y)

        if distance_x < self.threshold and distance_y < self.threshold:
            self.organism.velocity *= 0
            return True
        
        direction = np.sign(self.waypoint - position)
        norm_dir = np.where(direction != 0, np.sign(direction), 0)

        self.organism.velocity = norm_dir * self.organism.speed

        return False
