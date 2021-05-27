# sorted
rand_list = [5, 7, 1, 3, 2, 8]
print(sorted(rand_list))
print(sorted(rand_list, reverse=True))

# sorted  len list
names_with_case = ['harry', 'suzy', 'al', 'mark']
new_list_1 = sorted(names_with_case, key=len)
print(new_list_1)

# sorted  len list revers
new_list = sorted(names_with_case, key=len, reverse=True)
print(new_list)

# sorted alphabetically
new_list_2 = sorted(names_with_case, reverse=True)
print(new_list_2)

# sort key lambda


class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Employee('Alex', 20)
a = Employee('Anna', 18)
x = Employee('David', 30)

lst = [s, a, x]

lst.sort(key=lambda x: x.age)
print([i.name for i in lst])
