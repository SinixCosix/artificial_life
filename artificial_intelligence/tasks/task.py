import numpy as np


class Task:
    def update(self, *args, **kwargs):
        raise NotImplementedError


class RouteTask(Task):
    def __init__(self, waypoints, organism, threshold=5.01):
        self.waypoints = [np.array(p, dtype=float) for p in waypoints]
        self.threshold = threshold
        self.organism = organism

    def update(self):
        if not self.waypoints:
            self.organism.velocity = np.array([0, 0])
            return

        point = self.waypoints[0]
        current_pos = self.organism.transform.position

        if (abs(current_pos[0] - point[0]) < self.threshold
                and abs(current_pos[1] - point[1]) < self.threshold):
            self.waypoints.pop(0)
            return

        direction = np.sign(point - current_pos)
        norm_dir = np.where(direction != 0, np.sign(direction), 0)

        self.organism.velocity = norm_dir * self.organism.speed
        print(norm_dir)
