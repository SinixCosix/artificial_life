import random

from ai.tasks import *


class Brain:
    def __init__(self, organism ):
        self.organism = organism
        self.tasks: list[Task] = []

    def add_task(self, task: Task):
        # add priority for task type
        self.tasks.append(task)

    def update(self):
        if not self.tasks:
            self.generate_task()
            return
        
        current_task = self.tasks[0]
        if current_task.do():
            self.tasks.pop(0)

    def generate_task(self):
        radius = 150
        x = random.uniform(radius / 3, radius)
        x = self.organism.body.position.x + x * random.choice((1, -1))

        y = random.uniform(radius / 3, radius)
        y = self.organism.body.position.y + y * random.choice((1, -1))

        self.add_task(WaypointTask((x, y), self.organism))
