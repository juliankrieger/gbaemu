# <a id="GameBoy_Emlator_in_Python_0"></a>GameBoy Emlator in Python

### Current Roadmap

*   Fully implement [GameBoy Cartridge Header](http://gbdev.gg8.se/wiki/articles/The_Cartridge_Header#0148_-_ROM_Size) handling in [ram.py](https://github.com/juliankrieger/gbaemu/blob/master/pyemu/ram.py)  

*   Implement all Z80 Architecture Calls in [cpu.py](https://github.com/juliankrieger/gbaemu/blob/master/pyemu/ram.py) as specified by [GB ISA](http://marc.rawer.de/Gameboy/Docs/GBCPUman.pdf)  

*   Integrate [Licensee Codes](https://github.com/juliankrieger/gbaemu/blob/master/temp/licensee_codes_unformatted) into [ram.py](https://github.com/juliankrieger/gbaemu/blob/master/pyemu/ram.py)  

*   Move Program Counter handling to cpu.py

*   Move Commands to subclasses of a superclass that can handle setting program counter and memory adresses

*   Write a lot more unit and integration tests

### Distant Future

*   Video Output  

*   Sound Handling  

*   Save States

### Even More Distant Future

*   Integrate Cython compilation for a considerable speed-up

#### Literature

*   [Tomek’s Blog](https://blog.rekawek.eu/2017/02/09/coffee-gb/) on creating a GameBoy emulator  

*   [GameBoy Opcode Summary](http://gameboy.mongenel.com/dmg/opcodes.html)  

*   [Compact View of GameBoy Opcodes](http://www.pastraiser.com/cpu/gameboy/gameboy_opcodes.html)  

*   [Little Book of Python AntiPatterns](https://docs.quantifiedcode.com/python-anti-patterns/index.html)  

*   [History of the GameBoy](http://www.rickard.gunee.com/projects/playmobile/html/3/3.html) by Rickard Gunee (Good Explanation of Tilesets and Mapscrolling)

#### Resources

*   Immendes [handy compilation of GameBoy opcodes, their mnemonics, adresses and cycle length in JSON format](https://github.com/lmmendes/game-boy-opcodes)
