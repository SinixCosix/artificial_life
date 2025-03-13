from .waypoint_task import WaypointTask
from .task import Task


class RouteTask(Task):
    def __init__(self, organism, waypoints):
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
    
