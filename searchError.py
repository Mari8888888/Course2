def foo(x, y):
    assert y != 3
    if y < x:
        return x/y
    else:
        return x**y


try:
    foo(3.0, 20000000)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")
