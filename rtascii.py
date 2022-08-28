import random
import os

path="arts"
files=os.listdir(path)
d='arts/' + random.choice(files)
print(d)
os.system( 'sh ' + d)
