my_list = ['apple', 'banana', 'cherry']
it  = ["".append(t for t in my_list)]
print(it)
my_string = "".join(it for it in my_list)
print(my_string)
print(type(my_list))
string = ""
string += str(my_list)
print (string)