import numpy as np
from OpenGL.GL import *


class Painter:
    def draw(self, object):
        glColor3f(*np.array(object.color) / 255.0)
        glBegin(GL_TRIANGLE_FAN)

        position = object.position
        size = object.size

        glVertex2f(position[0], position[0])

        # Draw circle segments
        num_segments = 8  # More segments for a smoother circle
        for i in range(num_segments + 1):
            angle = 2 * np.pi * i / num_segments
            glVertex2f(position[0] + np.cos(angle) * size, position[0] + np.sin(angle) * size)

        glEnd()
