pokemon = 0
pokedex = {}
with open('pokemonlista.txt', 'r',encoding='utf8') as f:
    pokemon = f.read()
    pokemon = pokemon.split('\n')

for i in pokemon:
    i=i.split(' ')
    pokedex[i[1]] = i[0]+' '+i[2]
    
    
    
print(pokedex['Bulbasaur'])
    
    
    