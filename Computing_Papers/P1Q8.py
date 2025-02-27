import math
import random

b=1
a=1

def f(x,y):
  return math.exp(x*y)*(math.cos(y)**2)*(math.sin(x**2))

N=10**6

sum=0
for i in range(N):
  x=random.uniform(-a,a)
  y=random.uniform(-b,b)
  sum+=f(x,y)
approx=(4*a*b)*(1/N)*sum

print("The approximation to the integral is", approx)

def f(x,y):
  return (3*x**2)/(1+y**2)

sum=0
for i in range(N):
  x=random.uniform(-a,a)
  y=random.uniform(-b,b)
  sum+=f(x,y)
approx=(4*a*b)*(1/N)*sum

print("The approximation to pi is", approx)