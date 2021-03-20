import random as rnd
kast=[]
with open('diceRoll.txt', 'w') as f:
    
    f.write('Simulera 10 kast:')
    for i in range(10):
        r=rnd.randint(1,6)
        f.write(f'{r} ')
        kast.append(r)
    
    kast.sort()
    f.write(f'\nSortera kasten:')
    for i in kast:
        f.write(f'{i} ')

    femmor=0
    for i in kast:
        if i == 5:
            femmor+=1
    f.write(f'\nAntal femmor: {femmor}')
print('done')
