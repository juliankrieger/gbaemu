from pyemu.registers.single_register import SingleRegister
from enum import Enum


class FlagStates(Enum):
    ZERO = 0
    OPERATION = 1
    HALFCARRY = 2
    CARRY = 3

class Flags(SingleRegister):
    def __init__(self):
        super().__init__(0)

    @property
    def flag(self):
        return self._val

    @flag.setter
    def flag(self, state):
        self._val = state

    def set_zero(self):
        """
        use if the last instruction produces a result of 0. Sets Flag to 0
        :return:
        """
        self.flag = FlagStates.ZERO

    def set_operation(self):
        """
        use if last operation was instruction
        :return:
        """
        self.flag = FlagStates.OPERATION

    def set_half_carry(self):
        """
         Set if, in the result of the last operation, the lower half of the byte overflowed past 15
        :return:
        """
        self.flag = FlagStates.HALFCARRY

    def set_carry(self):
        """
         Set if the last operation produced a result over 255 (for additions) or under 0 (for subtractions).
        :return:
        """
        self.flag = FlagStates.CARRY

