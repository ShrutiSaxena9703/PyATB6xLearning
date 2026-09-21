#_can be a variable
age=30
_age=31
print(age)
print(_age)

_=30
print(_)
_=_+1
print(_)
#do not have a number as the first thing in a variable name
# 1age=30 but age1=30 is possible alphanumeric

_name="shruti saxena"
print(_name)
pi=3.14
print(pi)
_married=True

#Type gives the type of data type
print(type(pi)) #<class 'float'>
print(type(_married)) #<class 'bool'>
print(type(_name))  #<class 'str'>

#complex number
complex_number=1+2j
print(complex_number)
print(complex_number.real)
print(complex_number.imag)

