import random as rnd 
kast = {
    1: 1,
    2: 2,
    3: 7,
    4: 4,
    5: 0,
    6: 0}



for i in range(100000):
    die = rnd.randint(1,6)
    kast[die]+=1

print(f'frekvenstabell:\n{kast}')
