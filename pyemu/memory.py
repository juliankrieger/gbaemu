
from pyemu.registers.af import AF
from pyemu.registers.bc import BC
from pyemu.registers.de import DE
from pyemu.registers.hl import HL
from pyemu.registers.flags import Flags
from pyemu.registers.pc import PC
from pyemu.registers.sp import SP


class Memory:
    def __init__(self):
        self.AF = AF()
        self.BC = BC()
        self.DE = DE()
        self.HL = HL()
        self.flag = Flags().flag
        self.pc = PC().pc
        self.sp = SP().sp

