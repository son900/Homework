# 1. Define the id of next variables:
int_a = 55
print(id(int_a))
str_b = 'cursor'
print(id(str_b))
set_c = {1, 2, 3}
print(id(set_c))
lst_d = [1, 2, 3]
print(id(lst_d))
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e))
# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.extend([4, 5])
print(id(lst_d))
# 3. Define the type of each object from step 1.
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))
# 4*. Check the type of the objects by using isinstance.
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))
# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(7, 3))
# 6. By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches.".format(7, 3))
# 7. By using keyword arguments into the curly braces.
print("Anna has {apples} apples and {peaches} peaches.".format(apples=7, peaches=3))
# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches.".format(3, 5))
# 9. With f-strings and variables
apples = 7
peaches = 3
print(f'Anna has {apples} apples and {peaches} peaches.')
# 10. With % operator
apples = 7
peaches = 3
print('Anna has %s apples and %s peaches.' % (apples, peaches))
# 11*. With variable substitutions by name (hint: by using dict)
data_dict = {"a": apples, "b": peaches}
print("Anna has %(a)s apples and %(b)s peaches." % data_dict)
#Comprehensions:
#(1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)

#(2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)
# 12. Convert (1) to list comprehension
list_comprehension1 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension1)
# 13. Convert (2) to regular for with if-else
lst1 = []
for i in range(10):
    if i % 2 == 0:
        lst1.append(i // 2)
    else:
        lst1.append(i *10)
print(lst1)
# (3)

d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

# (4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

# (5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)
# (6)
dict_comprehension_1 = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension_1)
# 14. Convert (3) to dict comprehension.
dict_comprehension_2 = {i: i ** 2 for i in range(10) if i % 2 == 1}
print(dict_comprehension_2)
# 15*. Convert (4) to dict comprehension.
dict_comprehension_3 = {x: x ** 2 if x % 2 ==1 else x // 0.5 for x in range(1, 11) }
print(dict_comprehension_3)
# 16. Convert (5) to regular for with if.
e = {}
for i in range(10):
    if i ** 3 % 4 == 0:
        e[i] = i ** 3
print(e)
# 17*. Convert (6) to regular for with if-else.
d = {}
for i in range(10):
    if i ** 3 % 4 == 0:
        d[i] = i ** 3
    else:
        d[i] = i
print(d)
# Lambda:

# (7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y
print(foo(3, 4))
# (8)
foo_1 = lambda x, y, z: z if y < x and x > z else y
print(foo_1(5, 6, 4))
# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y
print(foo(3, 4))
# 19*. Convert (8) to regular function
def foo_1(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo_1(5, 6, 4))


lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
print(sorted(lst_to_sort))
# 21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))
# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
new_lst = list(map(lambda x: x * 2, lst_to_sort))
print(new_lst)
# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
print(list(map(lambda a, b: a + b, list_A, list_B)))
# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
from functools import reduce
print(reduce(lambda x, y: x + y, lst_to_sort))
# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print(list(filter(lambda x: True if x % 2 == 1 else False, lst_to_sort)))
# Bogdan print(list(filter(lambda elem: (elem % 2 == 1), lst_to_sort)))
# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print(list(filter(lambda x: x < 0, range(-10, 10)))) # Тут пытался range(-10, 10)  всредину всунуть и if вставить
# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print(list(filter(lambda x: x in list_2, list_1)))
# Тут пытался всунуть range(len(list_1)) и list_2


print(list(filter(lambda x: (x % 2 == 1), lst_to_sort)))
