feet = 1
inches = 12

def change(feet,inches):
    inches, feet = int(12), int(1)
    change = inches * feet
    return change
print(change(inches, feet))



from change import inches, feet 
print(inches,feet)

def print_change(change: int) -> int:
     ''' 
    Print change takes in a change variable as a integer, and returns
    and tells the user a formatted integer, letting them know what their height is in inches
    '''
    return f' My height in inches is {change}!'