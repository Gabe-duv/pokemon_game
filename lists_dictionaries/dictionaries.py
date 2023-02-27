
pikachu =  {
    'name': 'pikachu',
    'attack': 55,
    'defense': 40,
    'hp': 40,
    'type': 'electric'
}
ekans =  {
    'name': 'ekans',
    'attack': 60,
    'defense': 35,
    'hp': 45,
    'type': 'psychic'
}

charmander =  {
    'name': 'charmander',
    'attack': 52,
    'defense': 43,
    'hp': 40,
    'type': 'fire'
}
Squirtle = { 
    'name': 'Squirtle',
    'attack': 47,
    'defense': 40,
    'hp': 45,
    'type': 'water'
}
Bulbasaur = {
    'name': 'Bulbasaur',
    'attack': 50,
    'defense': 55,
    'hp': 40,
    'type': 'grass'
}
eevee = {
    'name': 'eevee',
    'attack': 58,
    'defense': 37,
    'hp': 35,
    'type': 'normal'
}
pokemons = [pikachu , eevee , Bulbasaur , charmander , Squirtle , ekans]
while True:
    print( 'Enter the name of a pokemon you wont to see the stats of(or type nothing to quit)')
    name = input()
    if name == '':
        break
    for pokemon in pokemons:
        if pokemon['name'] == name:
            print("attack : " + str(pokemon['attack']))
            print("defense : " + str(pokemon['defense']))
            print("hp : " + str(pokemon['hp']))
            print("type : " + pokemon['type'])
if eevee['name'] == "name: 'eevee'":
    print("true")
else:
    print("false")