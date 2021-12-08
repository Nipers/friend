'''
Xinyi Di
2021-12-04
Exercise 2.2
'''

'''
Main project
Implement __str__ and __repr__ function in class
'''

class Person(object):
    def __init__(self, name, gender, age):
        self._name = name
        self._gender = gender
        self._age = age
    
    def __str__(self) -> str:
        return "Person(__str__) Name: {}; Gender: {}; Age: {};".format(self._name, self._gender, self._age)
    
    
    def __repr__(self) -> str:
        return "Person(__repr__) Name: {}; Gender: {}; Age: {};".format(self._name, self._gender, self._age)
    
def main():
    personA = Person("Tom", "Male", 30)   
    
    print('\n=============== Exercise 2.2 ===============')

    # Separator
    print('\n')
    
    # Test __str__ function, expected output should be "Person(__str__) Name: Tom; Gender: Male; Age: 30;"
    print("Testing __str__ function")
    expect = "Person(__str__) Name: Tom; Gender: Male; Age: 30;"
    if str(personA) != expect:
        print("expect \'{}\', get \'{}\', there is something wrong".format(expect, str(personA)))
    else:
        print(str(personA))
        print("The __str__ function works fine, test passed!")# Test __str__ function, expected output should be "Person(__str__) Name: Tom; Gender: Male; Age: 30;"
    
    # Separator
    print('\n')
    # Test __repr__ function, expected output should be "Person(__repr__) Name: Tom; Gender: Male; Age: 30;"
    print("Testing __repr__ function")
    expect = "Person(__repr__) Name: Tom; Gender: Male; Age: 30;"
    if personA.__repr__() != expect:
        print("expect \'{}\', get\'{}\', there is something wrong".format(expect, personA.__repr__()))
    else:
        print(personA.__repr__())
        print("The __repr__ function works fine, test passed!")
    

if __name__ == '__main__':
    main()
    