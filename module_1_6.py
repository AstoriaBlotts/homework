my_dict = {'Edward' : 1901, 'Bella' : 1987, 'Jacob' : 1990}
print(my_dict)
print(my_dict['Bella'])
print(my_dict.get('Renesmee'))
my_dict.update({'Carlisle' : 1640, 'Esme' : 1895})
werewolf = my_dict.pop('Jacob')
print(werewolf)
print(my_dict)
my_set = {'lumos', 3.14, 42, 3.14, 'lumos', 42, 3.14}
print(my_set)
my_set.add('nox')
my_set.add(9.75)
my_set.discard(42)
print(my_set)