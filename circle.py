two = 2
pi = 3.14
rad = 8
def circle_circumference(two, pi, rad):
    two, pi, rad = int(2), int(3.14), int(8)
    c_c = two * pi * rad
    return c_c

print(circle_circumference(two, pi, rad))

def print_circle_circumference(circle_circumference: int) -> int:
    ''' 
    Print circle circumference takes in a circle circumference variable as a integer, and returns
    tot the user a formatted integer, letting them know how big their circle is!
    '''
    return f' My lawn is in the shape of a circle and the size is {circle_circumference}!'
