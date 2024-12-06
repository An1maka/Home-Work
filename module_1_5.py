immutable_var= 1, 'hello', 1.5
print(immutable_var)
#immutable_var [0] = 3
#print(immutable_var) #так как данный тип данных это "кортеж" питон не дает нам заменить элементы внутри корьежа
mutable_list = [55, 'lomdon', 1.6]
print(mutable_list)
mutable_list [0] = 106
mutable_list [1] = 'birmingham'
mutable_list [2] = 14.2
print(mutable_list)
