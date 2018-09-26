import json
import os
from collections import defaultdict

class InstructionDict(defaultdict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __missing__(self, key):
        value = self[key] = (None or key) \
                            and Instruction(mnemonic="ERROR_IMMEDIATE", length=1, cycles=[1], addr=key, func="UNKOWN")
        return value

class Instruction:
    def __init__(self, mnemonic=None, length=None, cycles=None, flags=None, addr=None,
                 operand1=None, operand2=None, func=None):
        self.mnemonic = mnemonic
        self.length = length
        self.cycles = cycles
        self.flags = flags
        self.addr = addr
        self.operand1 = operand1
        self.operand2 = operand2
        self.func = func

    def __repr__(self):
        return self.func

class Instructions:
    def __init__(self):

        self.instructions = InstructionDict()

        rootpath = os.path.abspath(__file__).replace(os.path.basename(__file__), "")
        opspath = rootpath + "opcodes.json"

        with open(opspath, "r") as jsonfile:
            instruction_set = json.load(jsonfile)
            for i_dict in instruction_set["unprefixed"].values():
                instruction = Instruction(**i_dict)

                op1 = instruction.operand1
                if op1 is not None:
                    op1 = "_" + op1
                else:
                    op1 = ""

                op2 = instruction.operand2
                if op2 is not None:
                    op2 = "_" + op2
                else:
                    op2 = ""

                instruction.func = str(instruction.mnemonic) + op1 + op2
                instruction.addr = int(instruction.addr, 16)
                self.instructions[instruction.addr] = instruction

    def defaultIntruction(self, key):
        return Instruction(mnemonic="ERROR_IMMEDIATE", length=1, cycles=1, flags=None, addr=key)