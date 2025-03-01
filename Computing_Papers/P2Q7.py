import numpy as np

def comp_step(func, x, h):
    comp = complex(x,h)
    val = func(comp)
    return val.imag/h


def func(x):
    return 5*x**2+3*x

# Define x values
xlist = np.arange(-100, 100, 0.01)
xlist = np.round(xlist,2)


def der():
    return np.array([comp_step(func, x, 0.01) for x in xlist])

def second_derivative_central(xlist, deriv_list):
    """Computes second derivative using a two-sided (central) difference method."""
    double_deriv = np.zeros(len(xlist) - 2)  # Exclude first and last points

    for i in range(1, len(xlist) - 1):  # Only iterate over interior points
        double_deriv[i - 1] = (deriv_list[i + 1] - deriv_list[i - 1]) / (xlist[i + 1] - xlist[i - 1])

    return double_deriv


deriv = der()
double_deriv = second_derivative_central(xlist, deriv)

def newton(func, i):
    x_2 = xlist[i] - ((double_deriv[i])**(-1))*deriv[i]
    x_2_round = round(x_2,2)
    index = np.where(xlist == x_2_round)
    return (x_2_round,index)

def run():
    start = 3000

    der_x_0 = deriv[start]


    der_x_current = 1e10
    while abs(der_x_current/der_x_0) > 0.01:
        temp = newton(func, start)
        start = temp[1][0]
        der_x_current = comp_step(func, xlist[start], 0.01)
    return (xlist[start])

print(run())
