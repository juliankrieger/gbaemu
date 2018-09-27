from enum import Enum

# Specs of the gameboy as specified in http://gbdev.gg8.se/wiki/articles/The_Cartridge_Header

class SGBFlag(Enum):
    """
    Specifies whether the game supports SGB functions,
    """
    NO_SGB = "00"
    SGB = "03"


class CartridgeType(Enum):
    """
    Specifies which Memory Bank Controller (if any) is used in the cartridge,
    and if further external hardware exists in the cartridge.
    """
    # Memory Bank controller's and basic types
    ROM_ONLY = "00"
    MBC1 = "01"
    MBC1_RAM = "02"
    MBC1_RAM_BATTERY = "03"
    MBC2 = "05"
    MBC2_BATTERY = "06"
    ROM_RAM = "08"
    RAM_RAM_BATTERY = "09"
    MMM01 = "0B"
    MMM01_RAM = "0C"
    MMM01_RAM_BATTERY = "OD"
    MBC3_TIMER_BATTERY = "0F"
    MBC3_TIMER_RAM_BATTERY = "10"
    MBC3 = "11"
    MBC3_RAM = "12"
    MBC3_RAM_BATTERY = "13"
    MBC5 = "19"
    MBC5_RAM = "1A"
    MBC5_RAM_BATTERY = "1B"
    MBC5_RUMBLE = "1C"
    MBC5_RUMPLE_RAM = "1D"
    MBC5_RUMPLE_RAM_BATTERY = "1E"
    MBC6 = "20"
    MBC7_SENSOR_RUMBLE_RAM_BATTERY = "22H"

    # External Hardware
    POCKET_CAMERA = "FC"
    BANDAI_TAMA_5 = "FD"
    HUC3 = "FE"
    HUC1_RAM_BATTERY = "FF"

class ROMSize(Enum):
    #Even
    S_32_KBYTE = "00"
    S_64_KBYTE = "01"
    S_128_KBYTE = "02"
    S_256_KBYTE = "03"
    S_512_KBYTE = "04"
    S_1_MBYTE = "05"
    S_2_MBYTE = "06"
    S_4_MBYTE = "07"
    S_8_MBYTE = "08"

    #Odd
    S_1_1_MBYTE = "52"
    S_1_2_MBYTE = "53"
    S_1_5_MBYTE = "54"

class RAMSize(Enum):
    NONE = "00"
    S_2_KBYTES = "01"
    S_8_KBYTES = "02"
    S_32_KBYTES = "03"
    S_128_KBYTES = "04"
    S_64_KBYTES = "05"

class DestinationCode(Enum):
    JAPANESE = "00"
    NON_JAPANESE = "01"
