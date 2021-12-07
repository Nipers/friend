'''
Xinyi Di
2021-11-07
Exercise 1.1.4 to 1.1.5
'''

'''
This program takes input from the user
'''
def main():

    print('\n=============== Exercise 1.1.4 ===============')

    # To ask the user for his or her age
    age = input('Enter your age')
    print('*** User Age ***')
    print(age)

    print('\n=============== Exercise 1.1.5 ===============')

    # To display the type of the variable that contains the value that the user entered
    typeofinput = type(age)
    print('*** Type of the variable ***')
    print(typeofinput)


if __name__ == '__main__':
    main()



