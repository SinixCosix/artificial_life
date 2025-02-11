import numpy as np
from OpenGL.GL import *


class Painter:
    def draw(self, object):
        glColor3f(*np.array(object.color) / 255.0)
        glBegin(GL_TRIANGLE_FAN)

        size = object.transform.scale[0]
        x = object.transform.position[0]
        y = object.transform.position[1]

        glVertex2f(x - size, y - size)
        glVertex2f(x + size, y - size)
        glVertex2f(x + size, y + size)
        glVertex2f(x - size, y + size)

        glEnd()
