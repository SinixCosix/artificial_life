import numpy as np
from OpenGL.GL import *


class Painter:
    def draw(self, object):
        glColor3f(*np.array(object.color) / 255.0)
        glBegin(GL_QUADS)

        size = object.size
        glVertex2f(object.body.position[0] - size, object.body.position[1] - size)
        glVertex2f(object.body.position[0] + size, object.body.position[1] - size)
        glVertex2f(object.body.position[0] + size, object.body.position[1] + size)
        glVertex2f(object.body.position[0] - size, object.body.position[1] + size)

        glEnd()
