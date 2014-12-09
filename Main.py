from FunctionPackages.TEST import test_ALL

from FunctionPackages.convert_Flash import cStep_Flash
from FunctionPackages.convert_RAM import cStep_RAM
from FunctionPackages.convert_ExternVar import cStep_Extern
from FunctionPackages.convert_Bitmaps import cStep_Bitmaps

DEBUG = False
# DEBUG = True

def Main():

    if DEBUG == True:
        test_ALL()

    else:
        previous = input('What is the name of the previous bitmap?: ')
        chunk_Extern = cStep_Extern()
        chunk_Flash = cStep_Flash(previous)
        chunk_RAM = cStep_RAM()

        cStep_Bitmaps()
        print('DONE')

Main()