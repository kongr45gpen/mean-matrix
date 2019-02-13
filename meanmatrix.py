#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import truecolor
import math

XMIN = -5
XMAX = 5
YMIN = -5
YMAX = 5

#width = xmax - xmin
#height = ymax - ymin
mmin = XMIN - XMAX
mmax = YMAX - YMIN

class Element:
    """An element in the 2-dimensional matrix"""
    immutable = False
    value = 0

    def set(self, value):
        self.immutable = True
        self.value = value


Matrix = [[Element() for y in range(mmin, mmax)] for x in range(mmin, mmax)]

Matrix[2][2].set(0)
Matrix[-2][-2].set(-2)
Matrix[-4][0].set(2)


maxrange = XMAX * YMAX * 10
maxrange = 1500
for r in range(maxrange):
    if r % 10 == 0:
        print("Calculating repetition %d (%.2f%%)" % (r, 100 * r/float(maxrange)))
    for x in range(XMIN - 1, XMAX + 1):
        for y in range(YMIN - 1, YMAX + 1):
            element = Matrix[x][y]
            sum = 0.0
            count = 0
            if not element.immutable:
                if x + 1 <= XMAX:
                    sum += Matrix[x + 1][y].value
                    count += 1
                if y + 1 <= YMAX:
                    sum += Matrix[x][y+1].value
                    count += 1
                if x - 1 >= XMIN:
                    sum += Matrix[x-1][y].value
                    count += 1
                if y - 1 >= YMIN:
                    sum += Matrix[x][y-1].value
                    count += 1

                element.value = sum / count

# Find min and max values
minv = math.inf
maxv = - math.inf
for x in range(XMIN - 1, XMAX + 1):
    for y in range(YMIN - 1, YMAX + 1):
        element = Matrix[x][y]
        if element.value > maxv:
            maxv = element.value
        if element.value < minv:
            minv = element.value

def calcColour(value):
    normalised = (value - minv) / float(maxv - minv)
    return int(255 * normalised), int(255 * (1 - normalised)), 0

# Display the matrix
for y in range(YMIN - 1, YMAX + 1):
    for x in range(XMIN - 1, XMAX + 1):
        element = Matrix[x][y]

        display = "{0: 7.2f}".format(element.value)
        if element.immutable:
            display = truecolor.color_text(display, truecolor.PALETTE['black'], calcColour(element.value))
        else:
            display = truecolor.fore_text(display, calcColour(element.value))

        print(display, end=' ')
    print(' ')
