from pyemu.cpu import CPU
import os

def main():
    rootpath = os.path.abspath(__file__).replace(os.path.basename(__file__), "")
    gbpath = rootpath + "test.gb"

    file = open(gbpath, "rb")
    cartridge = file.read().hex()
    file.close()

    adress_space = [cartridge[i:i + 2] for i in range(0, len(cartridge), 2)]

    del cartridge

    cpu = CPU(adress_space)
    cpu.run(0.05)
    print(1)

if __name__ == '__main__':
    main()