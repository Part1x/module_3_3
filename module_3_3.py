def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(10, False)
values_list = [1, 'Yes', 2]
values_dict = {'a': 1, 'b': 2, 'c': 3}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)