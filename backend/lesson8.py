

def decorator_sssss(func_to_decorate):
    def wrapper():
        print('22222')
        one = func_to_decorate()
        print('3333333')
        return one
    return wrapper

@decorator_sssss
def one():
    print('print one 11111111')
    return '121212'


@decorator_sssss
def two():
    print('print two aaaaa')
    return 'bbbb'

one_var = one()
print(one_var)
two()