# PossibleChar.py

import cv2
import numpy as np
import math

###################################################################################################
class PossibleChar:

    # constructor #################################################################################
    def __init__(self, contour):
        self.contour = contour

        self.boundingRect = cv2.boundingRect(self.contour)

        [x, y, w, h] = self.boundingRect

        self.intBoundingRectX = x
        self.intBoundingRectY = y
        self.intBoundingRectWidth = w
        self.intBoundingRectHeight = h

        self.intBoundingRectArea = self.intBoundingRectWidth * self.intBoundingRectHeight

        self.intCenterX = (self.intBoundingRectX + self.intBoundingRectX + self.intBoundingRectWidth) // 2
        self.intCenterY = (self.intBoundingRectY + self.intBoundingRectY + self.intBoundingRectHeight) // 2

        self.fltDiagonalSize = math.sqrt((self.intBoundingRectWidth ** 2) + (self.intBoundingRectHeight ** 2))

        self.fltAspectRatio = float(self.intBoundingRectWidth) / float(self.intBoundingRectHeight)
    # end constructor

# end class








