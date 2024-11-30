immutable_var = (1, 2, 'a', 'b')
print(immutable_var)
Mutable_list = [1, 2, 'a', 'b', 'Modified']
print(Mutable_list)

food = ["appele", "coconate", "banana"]
print(food)
print(food[0])
food [2] = "ice cream"
print(food)
food.append(123)
print(food)
food.extend("banana")
print(food)
food.extend(["banana", 321])
print(food)
food.remove("coconate")
print(food)
tuple_ = 1, 2, 3, 4
tuple_2 = 1, 2, 3, 4
tuple_3 = ([1, 2, 3, 4])
print(tuple_)
print(tuple_2)
print(tuple_3)
print(tuple_3[1])
tuple_ = ([1, 2,], 3, 4)
print(tuple_)
tuple_[0] [1] = 3
print(tuple_)
tuple_ = (1, 2, 3) * 2
print(tuple_)