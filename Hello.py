import sys


# operation in "+", "*", etc.
def sum_array(numbers, operation):
    x=0
    y=1
    for a in numbers:
        x+=a
        y*=a
    if operation=='+':
        return x
    elif operation=='*':
        return y
    else:
        sys.stderr.write("The operation '" + operation + "' is illegal.")

print(sum_array([1,210,1], '9'))



