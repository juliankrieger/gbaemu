from pyemu.registers.pair_register import PairRegister


class DE(PairRegister):
    def __init__(self):
        super().__init__(0, 0)

    @property
    def d(self):
        return self._first

    @d.setter
    def d(self, val):
        if val is None:
            raise ValueError("val must not be None")
        if val > 256 or val < 0:
            raise ValueError("val must be in range 0,256")
        self._first = val

    @property
    def e(self):
        return self._second

    @e.setter
    def e(self, val):
        if val is None:
            raise ValueError("val must not be None")
        if val > 256 or val < 0:
            raise ValueError("val must be in range 0,256")
        self._second = val
