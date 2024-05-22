#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0, 1]
    while len(fibonacci) < length:
        nxtnum = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(nxtnum)
    print(fibonacci[:length])