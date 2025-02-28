from P2Q3 import two_sided_diff
import numpy as np

hlist = [10**(-9),10**(-12),10**(-15)]

xlist = [10**n for n in range(5)]

def func(y):
    return y**2*np.sin(y**2)

def derivative_f(x):
    return 2*x * np.sin(x**2) + 2*x**3 * np.cos(x**2)

def comp_step(func, x, h):
    comp = complex(x,h)
    val = func(comp)
    return val.imag/h

comp_step1 = []
two_sided_diff1 = []
for h in hlist:
    for x in xlist:
        val = comp_step(func, x, h)
        error = val - derivative_f(x)
        tup = (h,x,val,error)
        comp_step1.append(tup)

        val1 = two_sided_diff(func, x, h)
        error1 = val1 - derivative_f(x)
        tup1 = (h,x,val1,error1)
        two_sided_diff1.append(tup1)

print("The complex step method:")
for cont in comp_step1:
    print(f"x:{float(cont[1])}, h:{float(cont[0])}, Value and Error:", float(cont[2]), float(cont[3]))


print("The two sided differentiation method:")
for cont1 in two_sided_diff1:
    print(f"x:{float(cont1[1])}, h:{float(cont1[0])}, Value and Error:", float(cont1[2]), float(cont1[3]))


