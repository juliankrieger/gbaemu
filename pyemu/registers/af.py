from pyemu.registers.pair_register import PairRegister


class AF(PairRegister):
    def __init__(self):
        super().__init__(0, 0)

    @property
    def a(self):
        return self._first

    @a.setter
    def a(self, val):
        if val is None:
            raise ValueError("val must not be None")
        if val > 256 or val < 0:
            raise ValueError("val must be in range 0,256")
        self._first = val

    @property
    def f(self):
        return self._second

    @f.setter
    def f(self, val):
        if val is None:
            raise ValueError("val must not be None")
        if val > 256 or val < 0:
            raise ValueError("val must be in range 0,256")
        self._second = val
