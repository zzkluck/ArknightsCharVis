from copy import deepcopy
from typing import List
from dataclasses import dataclass
from math import sqrt
import numpy as np
from numpy import ndarray

@dataclass
class Circle:
    x: float
    y: float
    r: float

def circle_collide_sim(circles: List[Circle], step=1, lr=0.35):
    # circles = deepcopy(circles)
    # TODO: 这里应该可以有某种优化手段
    while step > 0:
        movement: List[ndarray] = [ np.array([0., 0.]) for _ in range(len(circles)) ]
        for i in range(len(circles)):
            for j in range(i+1, len(circles)):
                c0, c1 = circles[i], circles[j]
                overlap = c0.r + c1.r - sqrt((c0.x-c1.x)**2+(c0.y-c1.y)**2)
                #print(overlap)
                if overlap > 0:
                    movement[i] += np.array([(c0.x-c1.x), (c0.y-c1.y)]) * (overlap/c0.r)**2 * lr
                    movement[j] += np.array([(c1.x-c0.x), (c1.y-c0.y)]) * (overlap/c1.r)**2 * lr
        for i in range(len(circles)):
            circles[i].x += movement[i][0]
            circles[i].y += movement[i][1]
        step -= 1
    # return circles