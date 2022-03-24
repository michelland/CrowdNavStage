import logging
from crowd_sim.envs.utils.state import ObservableState


class Obstacle(object):
    def __init__(self, config, section, px, py):
        """
        Base class for obstacles
        """
        self.px = px
        self.py = py
        self.radius = config.getfloat(section, 'radius')

    def print_info(self):
        logging.info(f"Obstacle is in position ({self.px},{self.py})")

    def get_position(self):
        return self.px, self.py

    def set_position(self, position):
        self.px = position[0]
        self.py = position[1]

    def get_observable_state(self):
        return ObservableState(self.px, self.py, 0, 0, self.radius)
