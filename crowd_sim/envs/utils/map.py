import logging

import numpy as np

from crowd_sim.envs.utils.obstacle import Obstacle


class Map(object):
    def __init__(self, path):
        # self.radius = config.getfloat(section, 'radius')
        self.grid = np.loadtxt(path, dtype=int)
        self.obstacles = []
        for i in range(0,13):
            for j in range(0,13):
                if self.grid[i,j] == 1:
                    self.obstacles.append(Obstacle(j - 6, 6 - i, 0.5))

    def print_info(self):
        info = "obstacles at positions :"
        print(len(self.obstacles))
        for o in self.obstacles:
            info += f" {o.get_position()}"
        print(info)




