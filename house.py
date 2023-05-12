def square_footage(length, width):
    length, width = int(), int()
    answer = length * width
    return answer

print(square_footage(length,width))

def print_square_footage(square_footage: int, length, width) -> int:
    '''
    Print house square footage in a square footage variable as a integer, and return to the user 
    a formatted string, letting someone know the size of their home!
    '''
    return f'My home is {square_footage} . Its big enough for myself and my dog!'
