def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')

def test_var_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

test_var_kwargs(name="yasoob", address="21 Jump Street")
