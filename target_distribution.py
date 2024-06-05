import jax.numpy as np
from jax import vmap

class TargetDistribution(object):
    def __init__(self, pmap) -> None:
        self.n = 2
        self.domain = np.meshgrid(
            *[np.linspace(.03,.97,100)]*self.n
        )
        pmap=pmap.reshape((1, 10000))
        pmap=pmap[0]
        self._s = np.stack([X.ravel() for X in self.domain]).T
        self.evals = (
            self.p(pmap) , self._s
        )
    def p(self, map):
        return map
        # return np.exp(-60.5 * np.sum((x[:2] - 0.2)**2)) \
        #             + np.exp(-60.5 * np.sum((x[:2] - 0.75)**2)) \
        #             + np.exp(-60.5 * np.sum((x[:2] - np.array([0.2, 0.75]))**2)) \
        #             + np.exp(-60.5 * np.sum((x[:2] - np.array([0.75, 0.2]))**2))

    def update(self):
        pass