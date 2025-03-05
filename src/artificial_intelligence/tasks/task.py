import numpy as np


class Task:
    def update(self, *args, **kwargs):
        raise NotImplementedError

class WaypointTask(Task):
    def __init__(self, waypoint, organism):
        self.waypoint = waypoint
        self.threshold = 1.01
        self.organism = organism

    def update(self):
        position = self.organism.transform.position
        distance_x = abs(position[0] - self.waypoint[0])
        distance_y = abs(position[1] - self.waypoint[1])

        if distance_x < self.threshold and distance_y < self.threshold:
            self.organism.velocity *= 0
            return True
        
        direction = np.sign(self.waypoint - position)
        norm_dir = np.where(direction != 0, np.sign(direction), 0)

        self.organism.velocity = norm_dir * self.organism.speed



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
        current_pos = self.organism.position

        if (abs(current_pos[0] - point[0]) < self.threshold
                and abs(current_pos[1] - point[1]) < self.threshold):
            self.waypoints.pop(0)
            return

        direction = np.sign(point - current_pos)
        norm_dir = np.where(direction != 0, np.sign(direction), 0)

        self.organism.velocity = norm_dir * self.organism.speed
        print(norm_dir)
