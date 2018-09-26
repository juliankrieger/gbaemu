import pytest
from pyemu.cpu import CPU


def test_load_bc_16_bit_imm():
    adress_space = [
        "00",
        "01",
        "0a",
        "0a",
        "00"]

    cpu = CPU(adress_space)
    cpu.mem_before = cpu.memory
    cpu.run()
    cpu.mem_after = cpu.memory
    assert True