# Number of values given 
 
x = [ 0, 1, 2, 5 ];
n = len(x);
      
# y[][] is used for difference table 
# with y[][0] used for input 
r = [1 for i in range(n)] ; 
y = [ 2, 3, 12, 147 ]

# Value to interpolate at 
value = 3;
sum=0;
for i in range(n):
    term=y[i];
    for j in range(n):
        if (i!=j):
            term = term*((value - x[j]) / (x[i] - x[j]));
    sum=sum+term;
  
print("\nValue at", value,  
      "is", round(sum, 6)); 
