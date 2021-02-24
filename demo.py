#! /bin/python3
#  Spring 2020 (PJW)

import scipy.optimize as opt

#  Compute the difference between x cubed and y. We'll use this 
#  later to input a value of y and have the algorithm loop over
#  guesses of x until it finds one where x**3 is equal to y.
#
#  This is not how one would usually compute a cube root; rather
#  it's an illustration of how the algorithm works for a case where
#  you know what the answer should be.

def find_cube_root(x,y):
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