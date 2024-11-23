immutable_var =(1, 2, 'a', 'b')
print(immutable_var)
# immutable_var [0] = 20
# print(immutable_var)
# значения элементов кортежа нельзя изменять, так как кортеж (tuple) является неизменяемым типом данных
mutable_list = [5, 6, 'c', 1.25]
print(mutable_list)
mutable_list[2] = False
mutable_list.append('Urban')
mutable_list.extend('year')
print(mutable_list)