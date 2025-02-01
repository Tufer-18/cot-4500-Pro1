import math

def approximation(x0, tol = 0.000001):
  x = x0
  diff = x0
  iter = 0

  print(f"{iter} : {x}")

  while diff >= tol:
    iter += 1
    y = x
    x = (x/2) + (1/x)
    print(f"{iter} : {x}")
    diff = abs(x-y)
  print(f"\nConvergence after {iter} iterations")
  return ""
print(approximation(1.5))

# Bisection
def bisection_method(func, a, b, tol=0.001, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("Function must have different signs at a and b")
    iter_count = 0
    while abs(b - a) > tol and iter_count < max_iter:
        iter_count += 1
        p = (a + b) / 2.0
        if func(p) == 0:
            return p
        elif func(a) * func(p) < 0:
            b = p
        else:
            a = p
    print(f"{iter_count} iterations")        
    return (a + b) / 2.0
func = lambda x: x**3 + 4*x**2 -10
print(bisection_method(func, 1, 2))




# Fixed point
def fixed_point_iteration(p0, tol, N0):
    result = "Failure"
    for i in range(1, N0+1):
        #p = p0 - p0*p0*p0 - 4*p0*p0 + 10
        #or
        #p = math.sqrt(10 - p0*p0*p0)/2
        if math.isnan(p):
            print("\nResult diverges")
            break
        print(f"{i} : {p}")
        if abs(p - p0) < tol:
            result = "Success"
            break
        p0 = p
    print(f"\n{result} after {i} iterations")
p0 = 1.5
tol = 0.000001
N0 = 50
fixed_point_iteration(p0, tol, N0)




#NewtonR
from sympy import cos
import sympy as sym


x = sym.symbols('x')
exp = cos(x) - x 

derivative1_x = sym.diff(exp, x)
p0 = 3.14159265/4
tol = 0.000000000001
N0 = 23
i = 0
while i <= N0:
  v = derivative1_x.subs(x,p0)
  print(f"{i}  {p0:.10f}")
  i+=1
  if v != 0:
      pN = p0 - exp.subs(x,p0)/v
      if abs(pN-p0) < tol:
          print(f"{i}  {pN:.10f}  ")
          break
      p0 = pN
  else:
    print("Unsuccessful (max iteration performed). Done.")
