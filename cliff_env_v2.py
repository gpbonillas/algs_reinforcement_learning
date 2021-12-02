import gym
from gym import spaces


class CliffEnv(gym.Env):
    def __init__(self):
        self.height = 5
        self.width = 11
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Tuple((
            spaces.Discrete(self.width),
            spaces.Discrete(self.height)
        ))
        self.moves = {
            0: (0, -1),   # up
            1: (1, 0),   # right
            2: (0, 1),  # down
            3: (-1, 0),  # left
        }

        # begin in start state
        self.reset()

    def step(self, action):
        x, y = self.moves[action]
        self.S = self.S[0] + x, self.S[1] + y

        self.S = max(0, self.S[0]), max(0, self.S[1])
        self.S = (min(self.S[0], self.width - 1),
                  min(self.S[1], self.height - 1))

        if self.S == (self.width - 1, 0):
            return self.S, -1, True, {}
        elif self.S[0] != 0 and self.S[1] == 0:
            # the cliff
            return self.reset(), -500, False, {}
        return self.S, -1, False, {}

    def reset(self):
        self.S = (0, 0)
        return self.S

    def set_state(self, state):
        self.S = state
        return
