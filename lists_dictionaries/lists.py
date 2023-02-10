pokemon = ['Pikachu', 'Charmander', 'Squirtle'] # This is a list. It allows you to store multiple values in a single variable.

pokemon.append('Bulbasaur')  # This will add Bulbasaur to the end of the list.

print(pokemon) # This will print the list again and you should see that Bulbasaur has been added.

pokemon.remove('Squirtle') # This will remove Squirtle from the list. Python will only remove the first instance of Squirtle.

print(pokemon)

print(pokemon.index('Charmander')) # This will print the index of Charmander in the list. the index is the position. The first item in the list is at index 0.

print(pokemon)

pokemon.insert(1, 'Squirtle') # This will insert Squirtle at index 1 in the list.


# I have created a while loop that will take the name of a pokemon and check if it is in the list.
# I would like you to alter this while loop so that you can add pokemon to the list, remove pokemon from the list and print the list

while True:
    print('Enter the name of a Pokemon: (or enter nothing to quit)')
    name = input() # This will take the name of a pokemon from the user.
    if name == '': # This will check if the user has entered nothing.
        break # This will exit the while loop.
    if name in pokemon: # This will check if the name of the pokemon is in the list.
        print('Yes, ' + name + ' is in the Pokemon list.') # This will print the name of the pokemon and the fact that it is in the list.
    else: # This will run if the name of the pokemon is not in the list.
        print('No, ' + name + ' is not in the Pokemon list.') # This will print the name of the pokemon and the fact that it is not in the list.
