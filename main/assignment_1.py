import math

def approximation(x0, tol = 0.000001)
  x = x0
  diff = x0
  iter = 0

  print("f{iter} : {x}")

  while diff >= tol:
    iter += 1
    y = x
    x = (x/2) + (1/x)
    print("f{iter} : {x}")
    diff = abs(x-y)
  print(f"\nConvergence after {iter} iterations")
  return x

print(approximation(1.5))
