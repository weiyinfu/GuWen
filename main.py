from fu import json
from os.path import *

folder = dirname(__file__)
x = json.load(join(folder, 'guwen.json'))
print(len(x))
