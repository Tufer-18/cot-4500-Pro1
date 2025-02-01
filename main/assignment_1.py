import math

#Approximation----------------------------------------------------------------------
def approximation(x0, tol = ...): # Tolerance is adjusted here.
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
print(approximation(guess)) #Enter a value here.

# Bisection---------------------------------------------------------------------------
def bisection_method(func, a, b, tol=..., max_iter=...): #Tolerance and max iterations can be changed here.
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
func = lambda x:  #Change function here.
print(bisection_method(func, a value, b value))




# Fixed point------------------------------------------------------------------------
def fixed_point_iteration(p0, tol, N0):
    result = "Failure"
    for i in range(1, N0+1):
        #p = enter equation here, where x = p0.
        if math.isnan(p):
            print("\nResult diverges")
            break
        print(f"{i} : {p}")
        if abs(p - p0) < tol:
            result = "Success"
            break
        p0 = p
    print(f"\n{result} after {i} iterations")
p0 = ...
tol = ... # Enter your values here.
N0 = ...
fixed_point_iteration(p0, tol, N0)




#NewtonR----------------------------------------------------------------------------
from sympy import cos
import sympy as sym


x = sym.symbols('x')
exp =  # Here is the test equation. Enter the expression in terms of x.

derivative1_x = sym.diff(exp, x)
p0 = ...
tol = ... # Enter the relevant values here.
N0 = ...
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
