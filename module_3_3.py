def print_params(a=1, b='строка', c=True):
    print(a, b, c)
list_ = [1, 'строка', True]
print_params(list_, c=True)

def values_list (a, b, c,):
    print(a, b, c)
    values_dict_ = {a = 1, b = 'строка', c = True }
    print_params (*values_list)