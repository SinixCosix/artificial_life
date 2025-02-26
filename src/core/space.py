class Space:
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def update(self, dt=1.0):
        for object in self.objects:
            if hasattr(object, "rigidbody"):
                object.rigidbody.update(dt)

            object.update()
