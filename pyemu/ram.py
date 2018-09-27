from pyemu.gb_specs import *

class RAM:
    def __init__(self, adress_space, memory):
        self.adress_space = adress_space
        self.memory = memory

    def hex_str_to_int(self, addr):
        if type(addr) is str:
            return int(addr, 16)
        elif type(addr) is int:
            return addr


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
        byte = self.adress_space[self.hex_str_to_int(addr)]
        return byte

    def read_16_bit_at_adress(self, addr):
        """
        Fetch two, two digit hexadecimal numbers in a touple from adress_space
        :return: touple of two digit hexadecimal numbers
        """
        byte1, byte2 = self.adress_space[self.hex_str_to_int(addr)], self.adress_space[self.hex_str_to_int(addr) + 1]
        return byte1, byte2

    def store_8_bit_at_adress(self, addr, value):
        self.adress_space[addr] = value

    # Special Values
    def get_cartridge_type(self):
        return CartridgeType(self.read_8_bit_at_adress("147"))

    def get_rom_size(self):
        return ROMSize(self.read_8_bit_at_adress("148"))

    def get_destination_code(self):
        return DestinationCode(self.read_8_bit_at_adress("14A"))

    def get_rom_version_number(self):
        return self.read_8_bit_at_adress("14C")

    def get_header_checksum(self):
        return self.read_8_bit_at_adress("14D")

    #not working
    def calculate_header_checksum(self):
        x = 0

        for i in range(self.hex_str_to_int("134"), self.hex_str_to_int("14C")):
            x = x - self.hex_str_to_int(self.read_8_bit_at_adress(i)) - 1

        x = '{0:08b}'.format(int(x) % 2**8).replace("-", "")

        return x
