from time import sleep
from typing import Callable

from pyemu.memory import Memory
from pyemu.decoder import Decoder
from pyemu.instruction import Instructions, Instruction

import logging

class CPU:
    """
    CPU class
    """

    def __init__(self, adress_space: list):
        """
        Initialise CPU
        :param adress_space: adress space is a X long bytestream, split into a 2 digit byte list
        """

        self.memory = Memory()
        self.adress_space = adress_space
        self.instructions = Instructions().instructions
        self.decoder = Decoder(self.instructions)

        self.matcher = {
            0: self.NOP,
            1: self.BASE_COMMAND,
            2: self.BASE_COMMAND,
            3: self.BASE_COMMAND,
            4: self.BASE_COMMAND,
            5: self.BASE_COMMAND,
            6: self.BASE_COMMAND,
            7: self.BASE_COMMAND,
            8: self.BASE_COMMAND,
            9: self.BASE_COMMAND,
            10: self.BASE_COMMAND,
            11: self.BASE_COMMAND,
            12: self.BASE_COMMAND,
            13: self.BASE_COMMAND,
            14: self.BASE_COMMAND,
            15: self.BASE_COMMAND,
            16: self.BASE_COMMAND,
            17: self.BASE_COMMAND,
            18: self.BASE_COMMAND,
            19: self.BASE_COMMAND,
            20: self.BASE_COMMAND,
            21: self.BASE_COMMAND,
            22: self.BASE_COMMAND,
            23: self.BASE_COMMAND,
            24: self.BASE_COMMAND,
            25: self.BASE_COMMAND,
            26: self.BASE_COMMAND,
            27: self.BASE_COMMAND,
            28: self.BASE_COMMAND,
            29: self.BASE_COMMAND,
            30: self.BASE_COMMAND,
            31: self.BASE_COMMAND,
            32: self.BASE_COMMAND,
            33: self.BASE_COMMAND,
            34: self.BASE_COMMAND,
            35: self.BASE_COMMAND,
            36: self.BASE_COMMAND,
            37: self.BASE_COMMAND,
            38: self.BASE_COMMAND,
            39: self.BASE_COMMAND,
            40: self.BASE_COMMAND,
            41: self.BASE_COMMAND,
            42: self.BASE_COMMAND,
            43: self.BASE_COMMAND,
            44: self.BASE_COMMAND,
            45: self.BASE_COMMAND,
            46: self.BASE_COMMAND,
            47: self.BASE_COMMAND,
            48: self.BASE_COMMAND,
            49: self.BASE_COMMAND,
            50: self.BASE_COMMAND,
            51: self.BASE_COMMAND,
            52: self.BASE_COMMAND,
            53: self.BASE_COMMAND,
            54: self.BASE_COMMAND,
            55: self.BASE_COMMAND,
            56: self.BASE_COMMAND,
            57: self.BASE_COMMAND,
            58: self.BASE_COMMAND,
            59: self.BASE_COMMAND,
            60: self.BASE_COMMAND,
            61: self.BASE_COMMAND,
            62: self.BASE_COMMAND,
            63: self.BASE_COMMAND,
            64: self.BASE_COMMAND,
            65: self.BASE_COMMAND,
            66: self.BASE_COMMAND,
            67: self.BASE_COMMAND,
            68: self.BASE_COMMAND,
            69: self.BASE_COMMAND,
            70: self.BASE_COMMAND,
            71: self.BASE_COMMAND,
            72: self.BASE_COMMAND,
            73: self.BASE_COMMAND,
            74: self.BASE_COMMAND,
            75: self.BASE_COMMAND,
            76: self.BASE_COMMAND,
            77: self.BASE_COMMAND,
            78: self.BASE_COMMAND,
            79: self.BASE_COMMAND,
            80: self.BASE_COMMAND,
            81: self.BASE_COMMAND,
            82: self.BASE_COMMAND,
            83: self.BASE_COMMAND,
            84: self.BASE_COMMAND,
            85: self.BASE_COMMAND,
            86: self.BASE_COMMAND,
            87: self.BASE_COMMAND,
            88: self.BASE_COMMAND,
            89: self.BASE_COMMAND,
            90: self.BASE_COMMAND,
            91: self.BASE_COMMAND,
            92: self.BASE_COMMAND,
            93: self.BASE_COMMAND,
            94: self.BASE_COMMAND,
            95: self.BASE_COMMAND,
            96: self.BASE_COMMAND,
            97: self.BASE_COMMAND,
            98: self.BASE_COMMAND,
            99: self.BASE_COMMAND,
            100: self.BASE_COMMAND,
            101: self.BASE_COMMAND,
            102: self.BASE_COMMAND,
            103: self.BASE_COMMAND,
            104: self.BASE_COMMAND,
            105: self.BASE_COMMAND,
            106: self.BASE_COMMAND,
            107: self.BASE_COMMAND,
            108: self.BASE_COMMAND,
            109: self.BASE_COMMAND,
            110: self.BASE_COMMAND,
            111: self.BASE_COMMAND,
            112: self.BASE_COMMAND,
            113: self.BASE_COMMAND,
            114: self.BASE_COMMAND,
            115: self.BASE_COMMAND,
            116: self.BASE_COMMAND,
            117: self.BASE_COMMAND,
            118: self.BASE_COMMAND,
            119: self.BASE_COMMAND,
            120: self.BASE_COMMAND,
            121: self.BASE_COMMAND,
            122: self.BASE_COMMAND,
            123: self.BASE_COMMAND,
            124: self.BASE_COMMAND,
            125: self.BASE_COMMAND,
            126: self.BASE_COMMAND,
            127: self.BASE_COMMAND,
            128: self.BASE_COMMAND,
            129: self.BASE_COMMAND,
            130: self.BASE_COMMAND,
            131: self.BASE_COMMAND,
            132: self.BASE_COMMAND,
            133: self.BASE_COMMAND,
            134: self.BASE_COMMAND,
            135: self.BASE_COMMAND,
            136: self.BASE_COMMAND,
            137: self.BASE_COMMAND,
            138: self.BASE_COMMAND,
            139: self.BASE_COMMAND,
            140: self.BASE_COMMAND,
            141: self.BASE_COMMAND,
            142: self.BASE_COMMAND,
            143: self.BASE_COMMAND,
            144: self.BASE_COMMAND,
            145: self.BASE_COMMAND,
            146: self.BASE_COMMAND,
            147: self.BASE_COMMAND,
            148: self.BASE_COMMAND,
            149: self.BASE_COMMAND,
            150: self.BASE_COMMAND,
            151: self.BASE_COMMAND,
            152: self.BASE_COMMAND,
            153: self.BASE_COMMAND,
            154: self.BASE_COMMAND,
            155: self.BASE_COMMAND,
            156: self.BASE_COMMAND,
            157: self.BASE_COMMAND,
            158: self.BASE_COMMAND,
            159: self.BASE_COMMAND,
            160: self.BASE_COMMAND,
            161: self.BASE_COMMAND,
            162: self.BASE_COMMAND,
            163: self.BASE_COMMAND,
            164: self.BASE_COMMAND,
            165: self.BASE_COMMAND,
            166: self.BASE_COMMAND,
            167: self.BASE_COMMAND,
            168: self.BASE_COMMAND,
            169: self.BASE_COMMAND,
            170: self.BASE_COMMAND,
            171: self.BASE_COMMAND,
            172: self.BASE_COMMAND,
            173: self.BASE_COMMAND,
            174: self.BASE_COMMAND,
            175: self.BASE_COMMAND,
            176: self.BASE_COMMAND,
            177: self.BASE_COMMAND,
            178: self.BASE_COMMAND,
            179: self.BASE_COMMAND,
            180: self.BASE_COMMAND,
            181: self.BASE_COMMAND,
            182: self.BASE_COMMAND,
            183: self.BASE_COMMAND,
            184: self.BASE_COMMAND,
            185: self.BASE_COMMAND,
            186: self.BASE_COMMAND,
            187: self.BASE_COMMAND,
            188: self.BASE_COMMAND,
            189: self.BASE_COMMAND,
            190: self.BASE_COMMAND,
            191: self.BASE_COMMAND,
            192: self.BASE_COMMAND,
            193: self.BASE_COMMAND,
            194: self.BASE_COMMAND,
            195: self.BASE_COMMAND,
            196: self.BASE_COMMAND,
            197: self.BASE_COMMAND,
            198: self.BASE_COMMAND,
            199: self.BASE_COMMAND,
            200: self.BASE_COMMAND,
            201: self.BASE_COMMAND,
            202: self.BASE_COMMAND,
            203: self.BASE_COMMAND,
            204: self.BASE_COMMAND,
            205: self.BASE_COMMAND,
            206: self.BASE_COMMAND,
            207: self.BASE_COMMAND,
            208: self.BASE_COMMAND,
            209: self.BASE_COMMAND,
            210: self.BASE_COMMAND,
            211: self.BASE_COMMAND,
            212: self.BASE_COMMAND,
            213: self.BASE_COMMAND,
            214: self.BASE_COMMAND,
            215: self.BASE_COMMAND,
            216: self.BASE_COMMAND,
            217: self.BASE_COMMAND,
            218: self.BASE_COMMAND,
            219: self.BASE_COMMAND,
            220: self.BASE_COMMAND,
            221: self.BASE_COMMAND,
            222: self.BASE_COMMAND,
            223: self.BASE_COMMAND,
            224: self.BASE_COMMAND,
            225: self.BASE_COMMAND,
            226: self.BASE_COMMAND,
            227: self.BASE_COMMAND,
            228: self.BASE_COMMAND,
            229: self.BASE_COMMAND,
            230: self.BASE_COMMAND,
            231: self.BASE_COMMAND,
            232: self.BASE_COMMAND,
            233: self.BASE_COMMAND,
            234: self.BASE_COMMAND,
            235: self.BASE_COMMAND,
            236: self.BASE_COMMAND,
            237: self.BASE_COMMAND,
            238: self.BASE_COMMAND,
            239: self.BASE_COMMAND,
            240: self.BASE_COMMAND,
            241: self.BASE_COMMAND,
            242: self.BASE_COMMAND,
            243: self.BASE_COMMAND,
            244: self.BASE_COMMAND,
            245: self.BASE_COMMAND,
            246: self.BASE_COMMAND,
            247: self.BASE_COMMAND,
            248: self.BASE_COMMAND,
            249: self.BASE_COMMAND,
            250: self.BASE_COMMAND,
            251: self.BASE_COMMAND,
            252: self.BASE_COMMAND,
            253: self.BASE_COMMAND,
            254: self.BASE_COMMAND,
            255: self.BASE_COMMAND,
        }

    def run(self, cycletime=0, runtime=None):
        """
        Runs for the duration of specified runtime.
        :param runtime: if none is given, runs through until it no longer finds a byte to interpret
        :param cycletime: Set the time the gameboy cpu will cycle. Should be defaulted to a low value
        :return: None
        """
        for cont in self.cpu_range(runtime):
            if cont:
                instr: Instruction
                func: Callable

                # Fetch command
                byte = self.read_8_bit()
                # Instruction decode
                instr = self.decodeByte(byte)

                #Execute command
                self.execute(instr, cycletime)
            else:
                break

    @staticmethod
    def cpu_range(runvar=None):
        """
        boolean generator for running the cpu for a specified rntime
        :param runvar: number for steps to generate True values
        :return: True/False
        """
        x = 0

        if not runvar:
            #Always yield true if no runvar is specified
            while(True):
                yield True
        else:
            while(x < runvar):
                x += 1
                yield True
            else:
                yield False

    def decodeByte(self, byte):
        """
        Decode byte instruction
        :param byte: 2 digit hexadecimal number
        :return: Instruction class instance with specified values
        """
        return self.decoder.decode_instruction(byte)

    def read_8_bit(self):
        """
        Fetch two digit hexadecimal number from actual program counter position
        :return: two digit hexadecimal number, either opcode or Immediate via GB ISA
        """
        byte = self.adress_space[self.memory.pc]
        return byte

    def read_16_bit(self):
        """
        Fetch two, two digit hexadecimal numbers in a touple from adress_space
        :return: touple of two digit hexadecimal numbers
        """
        byte1, byte2 = self.adress_space[self.memory.pc], self.adress_space[self.memory.pc + 1]
        return byte1, byte2

    def read_8_bit_at_adress(self, addr):
        """
        Fetch two digit hexadecimal number from actual program counter position
        :return: two digit hexadecimal number, either opcode or Immediate via GB ISA
        """
        byte = self.adress_space[self.eval_adrr(addr)]
        return byte

    def read_16_bit_at_adress(self, addr):
        """
        Fetch two, two digit hexadecimal numbers in a touple from adress_space
        :return: touple of two digit hexadecimal numbers
        """
        byte1, byte2 = self.adress_space[self.eval_adrr(addr)], self.adress_space[self.eval_adrr(addr) + 1]
        return byte1, byte2

    def store_8_bit_at_adress(self, addr, value):
        self.adress_space[addr] = value


    # Execute

    def execute(self, instruct: Instruction, cycletime):
        """
        Match Instruction instance to actual implementation and execute it
        :param instruct: Instruction instance
        :param cycletime: Time to multiple in instructions cycle
        :return: None
        """
        if instruct is None:
            logging.warn("Cant find instruction in ISA")
            return

        func = self.matcher.get(instruct.addr)
        if func is None:
            return

        if not callable(func):
            return

        #Execute
        func(instruct)
        #Wait cycles
        sleep(instruct.cycles[0] * cycletime)

    #Helpers
    def eval_adrr(self, addr):
        return int(addr, 16)

    # hit immediate, which is not associated with a command


    # Base
    def BASE_COMMAND(self, instruct:Instruction):
        logging.warn("PC: {} OP: {}  NAME: {}. NOT_IMPLEMENTED".format(self.memory.pc, instruct.addr, instruct.func))
        self.memory.pc += instruct.length or 1

    #0
    def NOP(self, instruct:Instruction):
        logging.warn("PC: {} OP: {}  NAME: {}".format(self.memory.pc, instruct.addr, instruct.func))
        self.memory.pc += instruct.length

    #1
    def LD_BC_d16(self, instruct:Instruction):
        logging.log("PC: {} OP:  NAME: {}".format(self.memory.pc, instruct.addr, instruct.func))
        self.memory.BC.b, self.memory.BC.c = self.read_16_bit()
        self.memory.pc += instruct.length

    #2
    def LD_EVAL_BC_A(self, instruct:Instruction):
        logging.log("PC: {} OP:  NAME: {}".format(self.memory.pc, instruct.addr, instruct.func))
        self.memory.sp = self.memory.BC.b + self.memory.BC.C
        self.store_8_bit_at_adress(self.memory.sp, self.memory.AF.a)
        self.memory.pc += instruct.length



