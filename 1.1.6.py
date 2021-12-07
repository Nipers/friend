'''
Xinyi Di
2021-11-07
Exercise 1.1.6
'''

'''
This program takes the base and height of a triangle from the user and returns the area of it
'''
def main():

    print('\n=============== Exercise 1.1.6 ===============')

    # Ask the user for the base and the height of a triangle
    base = input('Enter the base')
    height = input('Enter the height')

    # Convert the input to a number using float
    base = float(base)
    height = float(height)

    # Calculate the area of triangle
    areaoftriangle = base * height / 2

    #Check that the input values are valid for the sides of a triangle
    if base <= 0:
        print('Error: the side of triangle should be greater than 0')
    elif height <= 0:
        print('Error: the height of triangle should be greater than 0')
    # Return the area of triangle
    else:
        print('*** Triangle Area ***')
        print(areaoftriangle)



if __name__ == '__main__':
    main()