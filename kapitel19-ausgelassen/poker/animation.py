import time
import itertools


class DieRollAnimation:
    _CYCLE = itertools.cycle(range(1, 7))

    def __init__(self, roll_duration_s):
        self._roll_duration_s = roll_duration_s

    def _cycle_seconds(self, seconds):
        start = time.time()
        now = time.time()
        while now - start < seconds:
            yield next(self._CYCLE)
            now = time.time()

    def _typewrite(self, pre, boundary):
        for current in self._cycle_seconds(self._roll_duration_s):
            buffer_ = f'{pre}{current}'
            print(f'\r{buffer_}', end='')
        return f'{pre}{boundary}'

    def animate(self, dice):
        pre = '🎲 '
        for die in dice:
            pre = self._typewrite(pre, int(die)) + ' '
        print(f'\r{pre}')


if __name__ == '__main__':
    DieRollAnimation([1, 2, 3, 4, 5, 6], 0.5).animate()
