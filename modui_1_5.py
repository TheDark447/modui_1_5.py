from pkgutil import extend_path

immutable_var = 1, 2, 'a', 'b'
print((immutable_var) *2)
Mutable_list = [1, 2, 'a', 'b', 'Modified'] * 2
Mutable_list [2] = 3
Mutable_list [3] = 4
Mutable_list [4] = 5
Mutable_list.remove('Modified')
Mutable_list.extend('Fack')
print(Mutable_list)