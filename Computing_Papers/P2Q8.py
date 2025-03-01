import numpy as np

class Rosenbrock:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def f(self, x):
        return (self.a- x[0])**2 + self.b*(x[1]- x[0]**2)**2 
    
    def g(self, x): 
        return np.array([-2*(self.a- x[0])- 4*x[0]*self.b*(x[1]- x[0]**2), 2*self.b*(x[1]- x[0]**2)]) 


    def J(self, x): 
        ddf_ddx = 2- 4*self.b*(x[1]- x[0]**2) + 8*self.b*x[0]**2 
        ddf_dxdy =-4*self.b*x[0] 
        ddf_ddy = 2*self.b 
        return np.array([[ddf_ddx, ddf_dxdy], [ddf_dxdy, ddf_ddy]])



