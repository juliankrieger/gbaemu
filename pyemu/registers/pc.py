from pyemu.registers.single_register import SingleRegister


class PC(SingleRegister):
    def __init__(self):
        super().__init__(0x100)

    @property
    def pc(self):
        return self._val

    @pc.setter
    def pc(self, count):
        self._val = count
