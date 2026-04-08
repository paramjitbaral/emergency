import random


class SeededRandomizer:
    """Deterministic randomizer where one seed controls the full episode world."""

    def __init__(self, seed: int):
        self.seed = seed
        random.seed(seed)
        self._rng = random.Random(seed)

    def random(self) -> float:
        return self._rng.random()

    def randint(self, low: int, high: int) -> int:
        return self._rng.randint(low, high)

    def uniform(self, low: float, high: float) -> float:
        return self._rng.uniform(low, high)

    def choice(self, values: list):
        return self._rng.choice(values)
