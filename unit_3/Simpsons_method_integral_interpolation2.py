# Python3 code to implement Trapezoidal rule 
import math 
# A sample function whose definite  
# integral's approximate value is  
# computed using simpsons rule 
def y( x ): 
      
    # Declaring the function  
    # f(x) = 1/(1+x*x) 
    return ( math.cos(x)/(1+x*x*x)) 
      
# Function to evalute the value of integral 
def simpsons (a, b, n): 
      
    # Grid spacing 
    h = (b - a) / n 
      
    #Calculating result 
    res = 0
    i = 0
    while i<= n: 
        if i == 0 or i == n: 
            res+= y(a+i*h) 
        elif i % 3 != 0: 
            res+= 3 * y(a+i*h) 
        else: 
            res+= 2 * y(a+i*h) 
        i+= 1
    res = res * (3*h / 8) 
    return res 
  
# Driver code to test above function 
# Range of definite integral 
x0 = 0
xn = math.pi
  
# Number of grids. Higher value means 
# more accuracy 
n = 6
print ("Value of integral is ", 
     "%.4f"%simpsons(x0, xn, n)) 
  
