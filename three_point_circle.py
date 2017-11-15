#!/usr/bin/python
# -*- coding: utf-8 -*-

def f(n):
    if abs(n - int(n)) < 0.01:
        return int(n)
    else:
        return round(n, 2)

def circle_equation(note):
    xa, ya = eval(note)[0]
    xb, yb = eval(note)[1]
    xc, yc = eval(note)[2]
    
    x0 = ((xa * xa - xb * xb + ya * ya - yb * yb) * (ya - yc) - \
        (xa * xa - xc * xc + ya * ya - yc * yc) * (ya - yb)) / \
        (2 * (ya - yc) * (xa - xb) - 2 * (ya - yb) * (xa - xc))
    y0 = ((xa * xa - xb * xb + ya * ya - yb * yb) * (xa - xc) - \
        (xa * xa - xc * xc + ya * ya - yc * yc) * (xa - xb)) / \
        (2 * (ya - yb) * (xa - xc) - 2 * (ya - yc) * (xa - xb))
    
    r = pow((xa - x0) * (xa - x0) + (ya - y0) * (ya - y0), 0.5)
    
    return "(x-{})^2+(y-{})^2={}^2".format(f(x0), f(y0), f(r))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert circle_equation("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert circle_equation("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

    print("Use 'Check' to earn sweet rewards!")

