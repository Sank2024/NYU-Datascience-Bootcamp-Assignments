# Iterate through the following list of animals and print each one in all caps.
# animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
cap_animal =[] # Creating a empty list 

for i in animals: # Looping inside the animals list
    i = i.upper() # Capitalizing individual string on the list
    cap_animal.append(i) # Adding the capitalized word to the new list cap_animal

print(cap_animal)