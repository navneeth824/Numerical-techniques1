# newton forward and backward interpolation derivative
  
# calculating u mentioned in the formula 
def u_cal(u, n): 
  
    temp = u; 
    for i in range(1, n): 
        temp = temp * (u - i); 
    return temp; 
  
# calculating factorial of given number n 
def fact(n): 
    f = 1; 
    for i in range(2, n + 1): 
        f *= i; 
    return f; 
  
# Driver Code 
  
# Number of values given 
n = 6; 
x = [ 1, 2, 3, 4, 5, 6 ]; 
h = x[1] - x[0];      
# y[][] is used for difference table 
# with y[][0] used for input 
y = [[0 for i in range(n)] 
        for j in range(n)]; 
y[0][0] = 4; 
y[1][0] = 12; 
y[2][0] = 27; 
y[3][0] = 50;
y[4][0] = 75;
y[5][0] = 108;
  
# Calculating the forward difference 
# table 
for i in range(1, n): 
    for j in range(n - i): 
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]; 
  
# Displaying the forward difference table 
for i in range(n): 
    print(x[i], end = "\t"); 
    for j in range(n - i): 
        print(y[i][j], end = "\t"); 
    print("");

#input value
value=5.5;
u=(value-x[5])/h
d11=0;
d21=0;
#for derivatives at a point in the table
if(value<x[3]):
    d11=(y[1][1]+(u-0.5)*y[1][2]+(3*u**2-6*u+2)*y[1][3]/6+(4*u**3-18*u**2+22*u-6)*y[1][4]/24)#change 1 to suitable preceeding number
    d1=d11/h
    print("1st Derivative is",d1);
    d21=(y[1][2]+(u-1)*y[1][3]+(6*u**2-18*u+11)*y[1][4]/12)   #change 1 to suitable preceeding number (y[1][2]-y[1][3]+y[1][4]*(11/12)-y[1][5]*(5/6))
    d2=d21/(h**2)
    print("2nd Derivative is",d2);
    d31=(y[1][3]+y[1][4]*(u-1.5))             #change 1 to suitable preceeding number
    d3=d31/(h**3)
    print("3rd Derivative is",d3);


if(value>x[3]):
    d11=(y[n-2][1]+(u+0.5)*y[n-3][2]+(3*u**2+6*u+2)*y[n-4][3]/6+(4*u**3+18*u**2+22*u+6)*y[n-5][4]/24)#
    d1=d11/h
    print("1st Derivative is",d1);
    d21=(y[n-3][2]+(u+1)*y[n-4][3]+(6*u**2+18*u+11)*y[n-5][4]/12)   # (y[1][2]-y[1][3]+y[1][4]*(11/12)-y[1][5]*(5/6))
    d2=d21/(h**2)
    print("2nd Derivative is",d2);
    d31=(y[n-4][3]+y[n-5][4]*(u+1.5))             #
    d3=d31/(h**3)
    print("3rd Derivative is",d3);
       

