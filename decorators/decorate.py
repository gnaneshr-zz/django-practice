#!/usr/bin/env python3

def square(x):
    return x * x

def sumof(f, x, y):
    return f(x) + f(y)

def make_adder(x):
    def add(y):
        return x + y
    return add

def strjoin(sep, *words):
    return sep.join(words)

def add(x, y):
    return x + y

def info(*args):
    print("[INFO]", *args)

# def one(f):
#     print("one")

# @one
# def two():
#     print("two")

def trace(f):
    def g(*x):
        print(f.__name__, x)
        return f(*x)
    return g

@trace
def sq(x):
    return x * x

@trace
def sum_of_squares(x, y):
    return sq(x) + sq(y)

level = 0
def trace2(f):
    def g(*args):
        global level
        prefix = "| " * level + "|--"
        strargs = ", ".join(repr(a) for a in args)
        print("{} {}({})".format(prefix, f.__name__, strargs))
        level += 1
        result = f(*args)
        level -= 1
        return result
    return g

@trace2
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(square(4))
    f = square
    print(f(5))
    print(sumof(lambda x: x + 2, 2, 3))
    five_adder = make_adder(5)
    print(five_adder(4))
    print(strjoin("-", "one", "two"))
    args = [3, 4]
    print(add(*args))
    info(args)
    print(sq(5))
    print(sum_of_squares(4, 5))

    print(fib(5))
