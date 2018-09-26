from pyemu.registers.single_register import SingleRegister


class SP(SingleRegister):
    def __init__(self):
        super().__init__(0xFFFE)

    @property
    def sp(self):
        return self._val

    @sp.setter
    def sp(self, count):
        self._val = count
