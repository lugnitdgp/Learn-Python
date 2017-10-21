#defining the factorial function
def fatorial(n):                 
    if(n == 0 or n == 1):        
        return 1  
    #since factorial of 1 and 0 is 1
    else:                      
        return fatorial(n-1)*n
    #since n! = n*(n-1)!, we call function recursively

n = int(input("enter a num "))    
ans = fatorial(n)
#calling the function 'factorial' we created above and storing the returned value in 'ans'
print(ans)                        
