def fibonacci(n):
    '''
        Create a function called fibonacci. The function should have one parameter n.
          The function should return the nth value in the fibonacci series.
            You may implement the function using recursion or iteration.
          If you are feeling particularly frisky, do both as separate functions.
    '''
    
    if type(n) != int:
        return "Please Enter The number"
    elif n==0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def lucas(n):
    '''
        lucas that returns the nth value in the lucas numbers Again,
         you may use recursion or iteration,
         or both. Again, ensure that your function has a well-formed docstring.
    '''
    
    if type(n)!= int:
        return "Please Enter The number"
    elif n==0: 
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n,x=0,y=1):
    '''
       Both the fibonacci series and the lucas numbers are based on an identical formula.
         Add a third function called sum_series with one required parameter and two optional parameters.
           The required parameter will determine which element in the series to print.
             The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.
    '''
    if type(n)!= int:
        return "Please Enter The number"
    elif n==0:
        return x
    elif n==1:
        return y
    else:
        return sum_series(n - 1,x,y) + sum_series(n-2,x,y)
    