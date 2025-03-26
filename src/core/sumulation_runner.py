import threading
import time


class SimulationRunner:
    def __init__(self, world, target_fps=60):
        self.world = world
        self.target_dt = 1.0 / target_fps
        self.running = False
        self.lock = threading.Lock()

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.simulation_thread, daemon=True)
            self.thread.start()

    def stop(self):
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()

    def simulation_thread(self):
        while self.running:
            start_time = time.time()
            with self.lock:
                self.world.update(self.target_dt)
                self.world.fixed_update(self.target_dt)

            elapsed = time.time() - start_time
            time.sleep(max(0.0, self.target_dt - elapsed))
