import numpy as np

def newton(g, J, x0, tol, max_it=100): 
    r0 = np.linalg.norm(g(x0)) # Could have used r0 = np.sqrt(g(x0).dot(g(x0))) 
    for i in range(max_it): 
        x = x0- np.linalg.solve(J(x0), g(x0)) # Compute x_{n+1} = x_n- J^-1 g_n 
        x0 = x # x_{n} <- x_{n+1} # Check for convergence 
        r = np.linalg.norm(g(x0)) 
        print("Relative residual: {}".format(r/r0)) 
        if r/r0 < tol: 
            return x 
    return None

def f(x): 
    return (a- x[0])**2 + b*(x[1]- x[0]**2)**2 

def g(x): 
    return np.array([-2*(a- x[0])- 4*x[0]*b*(x[1]- x[0]**2), 2*b*(x[1]- x[0]**2)]) 

a, b = 2, 100 

def J(x): 
    ddf_ddx = 2- 4*b*(x[1]- x[0]**2) + 8*b*x[0]**2 
    ddf_dxdy =-4*b*x[0] 
    ddf_ddy = 2*b 
    return np.array([[ddf_ddx, ddf_dxdy], [ddf_dxdy, ddf_ddy]])

x = newton(g, J, [1.1, 1.1], 1.0e-9) 
print("f_min:", f(x)) 
print("x at f_min:", x)


from P2Q8 import Rosenbrock

def newton(my_class, x0, tol, max_it=100): 
    r0 = np.linalg.norm(my_class.g(x0)) # Could have used r0 = np.sqrt(g(x0).dot(g(x0))) 
    for i in range(max_it): 
        x = x0- np.linalg.solve(my_class.J(x0), my_class.g(x0)) # Compute x_{n+1} = x_n- J^-1 g_n 
        x0 = x # x_{n} <- x_{n+1} # Check for convergence 
        r = np.linalg.norm(my_class.g(x0)) 
        print("Relative residual: {}".format(r/r0)) 
        if r/r0 < tol: 
            return x 
    return None

x = newton(Rosenbrock(2, 100), [1.1, 1.1], 1.0e-9) 
print("f_min:", Rosenbrock(2, 100).f(x)) 
print("x at f_min:", x)