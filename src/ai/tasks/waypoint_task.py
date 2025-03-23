import numpy as np
import pymunk

from .task import Task


class WaypointTask(Task):
    def __init__(self, waypoint, organism):
        self.waypoint = pymunk.Vec2d(*waypoint)
        self.threshold = 1.1
        self.organism = organism

    def do(self):
        distance = self.waypoint - self.organism.position
        distance_x = abs(distance.x)
        distance_y = abs(distance.y)

        if distance_x < self.threshold and distance_y < self.threshold:
            self.organism.velocity = pymunk.Vec2d(0, 0)
            return True

        distance_length = distance.length 

        if distance_length > 0:
            norm_dir = distance.normalized()
        else:
            norm_dir = pymunk.Vec2d(0, 0)

        max_speed = min(self.organism.speed, distance_length) 
        self.organism.velocity = norm_dir * max_speed

        return False