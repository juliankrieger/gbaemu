import logging
from pyemu.instruction import Instruction

class Decoder:
    def __init__(self, instructions):
        self.ops = instructions

    def decode_instruction(self, byte):
        instr:Instruction = self.ops[(int(byte, 16))]
        if instr is None:
            logging.warn("Couldn't find matching opcode for \"0x{}\". May be Immediate?".format(byte))
        return instr
