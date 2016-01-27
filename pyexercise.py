import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(x)*sy.sin(2*x), (x,0, np.pi))
    return ans

def my_solution():
   A = np.array( [[5,7,6,9,6,21,15,-16,26,3],[8,6,9,13,7,	8,1,-5,20,8],[4,1,-7,5,-5,-9,4,11,	1,2],[-8,12,-1,2,	6,9,7,12,33,-9],[15,4,2,1,-8,-12,3,27,-5,-8],[9,7,8,4,4,8,7,26,4,13],[5,9,	7,-7,-6,8,24,27,27,8],[4,16,	26,3,	5,7,17,5,7,	21],[7,-6,18,1,1,2,4,8	,8,7],[4,-8,21,8,	2,12,	-1,2,	5,8]])
   b = np.array([470,409,71,457,33,554,741,625,304,299])
   x = np.linalg.solve(A,b) # Solve Ax = b
   return x

if __name__ == '__main__':
    your_id = 1400368
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id )))
    print('Integral = ' , my_integral())
    print('Solution = ', my_solution())
    
   