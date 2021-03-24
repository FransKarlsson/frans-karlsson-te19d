# a)
with open('provresultat.txt', 'r', encoding='utf-8') as f:
    resultat=f.read()
    print(resultat)


# b)
with open('provresultat.txt', 'w', encoding='utf-8') as f:  
    resultat=resultat.split('\n')
    resultat.sort()
    print(resultat)
    for i in resultat:
        f.write(f'\n{i}')

     



