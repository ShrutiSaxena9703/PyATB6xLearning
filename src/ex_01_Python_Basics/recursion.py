#recursion is function call itself again and again
#in recursion you should have an exit condition

def recursion_name(age):
    print(age)
    if(age==0):
        return 0
    else:
        return recursion_name(age-1)
recursion_name(5)


def factorial(number):

     print(number)
     if(number==1):
         return 1;
     else:
         return number*factorial(number-1)
print(factorial(5))