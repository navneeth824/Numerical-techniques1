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
value=5;
d11=0;
d21=0;
#for derivatives at a point in the table
if(value<x[3]):
    for j in range(1,n):
        d11+=((-1)**(j+1))*y[1][j]/j
    d1=d11/h
    print("1st Derivative is",d1);
    d21=(y[1][2]-y[1][3]+y[1][4]*(11/12))   #change term (y[1][2]-y[1][3]+y[1][4]*(11/12)-y[1][5]*(5/6))
    d2=d21/(h**2)
    print("1st Derivative is",d2);
    d31=(y[1][3]-y[1][4]*(3/2))             #change term
    d3=d31/(h**3)
    print("1st Derivative is",d3);


if(value>=x[3]):
    for j in range(1,n):
        d11+=y[n-j-1][j]/j
    d1=d11/h
    print("1st Derivative is",d1);
    d21=(y[n-3][2]+y[n-4][3]+y[n-5][4]*(11/12)+y[n-6][5]*(5/6))   #change term
    d2=d21/(h**2)
    print("1st Derivative is",d2);
    d31=(y[n-4][3]+y[n-5][4]*(3/2))                               #change term
    d3=d31/(h**3)
    print("1st Derivative is",d3);
       
