import math # noqa

def integrate(f,a,b,x,w):
  integral=0
  for i in range(len(x)):
    integral += f(x[i])*w[i]
  return (b-a)*integral

def f(x):
  return x**3 + x**2

a,b=0,10

exact_solution= 8500/3

print("For the trapezoidal rule:")
x=[a,b]
w=[0.5,0.5]
integral = integrate(f,a,b,x,w)
print("The approximate solution is", integral, "and the error is", round(exact_solution-integral, 3))

print("")

print("For the Simpson's rule:")
x=[a,(a+b)/2,b]
w=[1/6,2/3,1/6]
integral = integrate(f,a,b,x,w)
print("The approximate solution is", integral, "and the error is", round(exact_solution-integral, 3))

print("")

print("For the Gauss rule:")
x = ((a+b)/2- (b-a)/(2*math.sqrt(3)), (a + b)/2 + (b- a)/(2*math.sqrt(3))) 
w = (1/2, 1/2)
integral = integrate(f,a,b,x,w)
print("The approximate solution is", integral, "and the error is", round(exact_solution-integral, 3))