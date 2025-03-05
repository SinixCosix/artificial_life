import numpy as np

from .task import Task


class WaypointTask(Task):
    def __init__(self, waypoint, organism):
        self.waypoint = np.array(waypoint, dtype=float)
        self.threshold = 1.01
        self.organism = organism

    def do(self):
        position = self.organism.transform.position
        distance_x = abs(position[0] - self.waypoint[0])
        distance_y = abs(position[1] - self.waypoint[1])

        if distance_x < self.threshold and distance_y < self.threshold:
            self.organism.velocity *= 0
            return True
        
        direction = np.sign(self.waypoint - position)
        norm_dir = np.where(direction != 0, np.sign(direction), 0)

        self.organism.velocity = norm_dir * self.organism.speed

        return False
