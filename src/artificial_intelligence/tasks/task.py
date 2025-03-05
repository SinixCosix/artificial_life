import numpy as np


class Task:
    def do(self, *args, **kwargs) -> bool:
        raise NotImplementedError

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



class RouteTask(Task):
    def __init__(self, waypoints, organism):
        self.waypoints = [WaypointTask(waypoint, organism) for waypoint in waypoints]

    def do(self):
        if not self.waypoints:
            return True

        task = self.waypoints[0]
        
        if task.do():
            self.waypoints.pop(0)
            
            if not self.waypoints:
                return True

        return False
    
