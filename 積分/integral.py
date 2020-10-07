from sympy import *

t = symbols('t')
x = symbols('x')
t_y = 3*t -2
x_y = integrate(t_y,(t, -1, x))
print(diff(x_y,x))