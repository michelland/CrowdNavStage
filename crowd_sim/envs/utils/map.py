import logging

import numpy as np

from crowd_sim.envs.utils.obstacle import Obstacle
from crowd_sim.envs.utils.obstacle import ObstacleRectangle
from crowd_sim.envs.utils.obstacle import ObstacleCircle


class Map(object):
    def __init__(self, config, path):
        self.radius = config.getfloat('obstacles', 'radius')
        self.grid = np.loadtxt(path, dtype=int)
        self.obstacles = []
        self.size = int(path.split(sep='_')[1])
        print(f'map size : {self.size}')
        for i in range(0,(2 * self.size) + 1):
            for j in range(0,(2 * self.size) + 1):
                if self.grid[i,j] == 1:
                    self.obstacles.append(ObstacleCircle(j - self.size, self.size - i, self.radius))
                elif self.grid[i,j] == 2:
                    self.obstacles.append(ObstacleRectangle(j - self.size, self.size - i, self.radius))

    def print_info(self):
        info = "obstacles at positions :"
        print(len(self.obstacles))
        for o in self.obstacles:
            info += f" {o.get_position()}({type(o)}"
        print(info)




