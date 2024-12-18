my_dict = {'Anton': 1995, 'Max': 2000, 'Misha': 2005}
print(my_dict)
print(my_dict['Anton'])
print(my_dict.get('Sasha'))
my_dict.update({'Masha': 2020,
                'Lesha': 20010})
print (my_dict.pop('Max'))
print(my_dict)

my_set = {1, 6.5, 'Hello',1, 2, 5, 'Hello', 2, 6.5, 5, (1, 2, 3)}
print(my_set)
my_set.update([7, 8])
my_set.remove(5)
print(my_set)
