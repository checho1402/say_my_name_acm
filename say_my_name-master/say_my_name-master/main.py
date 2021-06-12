from os import listdir
from os.path import isfile, join
from characters import *

characters_path = "./characters/"
character_names = [fname[:-3] for fname in listdir(characters_path)
                   if isfile(join(characters_path, fname))
                   and not fname.startswith('_')
                   and not fname.endswith('.pyc')]

for cname in character_names:
    character = eval(cname + '.' + cname + "()")
    character.SayName()
