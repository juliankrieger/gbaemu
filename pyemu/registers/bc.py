from pyemu.registers.pair_register import PairRegister


class BC(PairRegister):
    def __init__(self):
        super().__init__(0, 0)

    @property
    def b(self):
        return self._first

    @b.setter
    def b(self, val):
        if val is None:
            raise ValueError("val must not be None")
        if val > 256 or val < 0:
            raise ValueError("val must be in range 0,256")
        self._first = val

    @property
    def c(self):
        return self._second

    @c.setter
    def c(self, val):
        if val is None:
            raise ValueError("val must not be None")
        if val > 256 or val < 0:
            raise ValueError("val must be in range 0,256")
        self._second = val
