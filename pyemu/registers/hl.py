from pyemu.registers.pair_register import PairRegister


class HL(PairRegister):
    def __init__(self):
        super().__init__(0, 0)

    @property
    def h(self):
        return self._first

    @h.setter
    def h(self, val):
        if val is None:
            raise ValueError("val must not be None")
        if val > 256 or val < 0:
            raise ValueError("val must be in range 0,256")
        self._first = val

    @property
    def l(self):
        return self._second

    @l.setter
    def l(self, val):
        if val is None:
            raise ValueError("val must not be None")
        if val > 256 or val < 0:
            raise ValueError("val must be in range 0,256")
        self._second = val
