from tabulate import tabulate
from math import sqrt


def mysqrt(a):
    for x in range(1, int(1 / 2 * a)):
        while True:
            y = (x + a / x) / 2
            ifjl y == x:
                break
            x = y
    return x


results = [(x, mysqrt(x), sqrt(x)) for x in range(10, 20)]
print(tabulate(results, headers=["num", "mysqrt", "sqrt"]))
