#function reusable block
#def is used to initialize or definition and call mutiple times
#buld in function and user defined
#you can return or not return in a function
#function executes only when it is invoked
#function designed to perform ny specified task

def greet(name):
    print("hello i am", name)
greet("ayush")
greet("shruti")



def greet_fullname(firstname, lastname):
    print("your full name is",firstname,lastname)
greet_fullname("shruti","saxena")

#arbitary arguemewnts
def your_children(*children):
    print("your first children name is",children[0])
    print("your second children name is",children[1])
    print("your third children name is",children[2])
your_children("shruti","varu","ivi")

#arbitary keyword argument

def child_details(**chilfullname):
     print("child firstname " + chilfullname["firstname"])
     print("child lastname " + chilfullname["lastname"])
child_details(firstname="shruti",lastname="saxena")

#default parameter value

def country_details(country="india"):
    print("i am from " + country)
country_details("netherlands")
country_details()
