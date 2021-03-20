with open('provresultat.txt', 'r', encoding='utf-8') as f:
    # a)
    resultat=f.read()
    print(resultat)

with open('provresultat.txt', 'w'):
    # b)
    resultat=resultat.split('\n')
    resultat.sort()
    print(resultat)
    for i in resultat:
        f.write(f'\n{resultat}')