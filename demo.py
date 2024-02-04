"""
demo.py
Spring 2020 PJW

Demonstrate calling functions with optional parameters, and demonstrate the
use of Newton's Method to solve an equation.
"""

import scipy.optimize as opt

#%% Calling functions

#  Sample function with two required arguments and one optional one.
#
#  Note the optional type hints. These are not required, but they
#  provide a way to document the function and to provide a check
#  on the input. The return type hint is also optional, but it's
#  a good idea to use it. The None indicates that this function
#  doesn't return anything.

def sample_function(payment:float, year:int, r:float = 0.05) -> None:
    pv = round( payment/(1+r)**year , 2 )
    print( f"PV of {payment} with T={year} and r={r} is ${pv}" )

#  Calling the function several ways

sample_function( 100, 10 )
sample_function( 100, 10, 0.03 )
sample_function( 100, 10, r=0.07 )

#%% Using Newton

#  Compute the difference between x cubed and y. We'll use this
#  later to input a value of y and have the algorithm loop over
#  guesses of x until it finds one where x**3 is equal to y.
#
#  This is not how one would usually compute a cube root; rather
#  it's an illustration of how the algorithm works for a case where
#  you know what the answer should be.

def find_cube_root(x:float ,y:int) -> float:
    miss = x**3 - y
    return miss

#  Now compute some cube roots. We'll set the starting guess of x to 1,
#  set the maximum number of iterations to 20 and will pass in the value
#  of y using the args keyword of the newton() call.

xinit = 1

#  Cube root of 8? Notice that there's a tiny bit of rounding error.
#  That's very common with iterative calculations.

y = 8
cr = opt.newton(find_cube_root,xinit,maxiter=20,args=[y])
print('\ncube root of',y,'is',cr)

#  Cube root of 27

y = 27
cr = opt.newton(find_cube_root,xinit,maxiter=20,args=[y])
print('\ncube root of',y,'is',cr)

#  Cube root of 64

y = 64
cr = opt.newton(find_cube_root,xinit,maxiter=20,args=[y])
print('\ncube root of',y,'is',cr)
