# Python3 code to implement Trapezoidal rule 
import math 
# A sample function whose definite  
# integral's approximate value is  
# computed using Trapezoidal rule 
def y( x ): 
      
    # Declaring the function  
    # f(x) = 1/(1+x*x) 
    return ( math.cos(x)/(1+x*x*x)) 
      
# Function to evalute the value of integral 
def trapezoidal (a, b, n): 
      
    # Grid spacing 
    h = (b - a) / n 
      
    # Computing sum of first and last terms 
    # in above formula 
    s = (y(a) + y(b)) 
  
    # Adding middle terms in above formula 
    i = 1
    while i < n: 
        s += 2 * y(a + i * h) 
        i += 1
          
    # h/2 indicates (b-a)/2n.  
    # Multiplying h/2 with s. 
    return ((h / 2) * s) 
  
# Driver code to test above function 
# Range of definite integral 
x0 = 0
xn = math.pi
  
# Number of grids. Higher value means 
# more accuracy 
n = 6
print ("Value of integral is ", 
     "%.4f"%trapezoidal(x0, xn, n)) 
  
