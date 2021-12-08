'''
Xinyi Di
2021-12-04
Exercise 2.3
'''

'''
Main project
Implement and test compare functions in class 
'''


class Person(object):
    def __init__(self, name, gender, age):
        self._name = name
        self._gender = gender
        self._age = age
        
    def __eq__(self, another) -> bool:
        return self._name == another._name and self._gender == another._gender and self._age == another._age
    
    def __ne__(self, another) -> bool:
        return self._name != another._name or self._gender != another._gender or self._age != another._age
    
    def __ge__(self, another) -> bool:
        return self._age >= another._age
    
    def __le__(self, another) -> bool:
        return self._age <= another._age
    
    def __str__(self) -> str:
        return "Name: {}; Gender: {}; Age: {};".format(self._name, self._gender, self._age)
    
    
 
def main():
    personA = Person("Tom", "Male", 30)  
    
    print('\n=============== Exercise 2.3 ===============')

    # Separator
    print('\n')
    
    # Test __eq__ and __ne__ function"
    print("Testing __eq__ and __ne__ funciton")
    print("Person information: ")
    personB = Person("Tom", "Male", 30)  
    personC = Person("Tim", "Male", 30) 
    personD = Person("Tom", "Female", 30)  
    personE = Person("Tom", "Male", 31) 
    print("A: " + str(personA))
    print("B: " + str(personB))
    print("C: " + str(personC))
    print("D: " + str(personD))
    print("E: " + str(personE))
    if personA == personB:
        print("A == B: " + str(personA == personB))
    else:
        print("A == B should be True, test failed.")
        return
    
    if personA != personC:
        print("A == C: " + str(personA == personC))
    else:
        print("A == C should be False, test failed.")
        return
    if personA != personD:
        print("A == D: " + str(personA == personD))
    else:
        print("A == D should be False, test failed.")
        return
    if personA != personE:
        print("A == E: " + str(personA == personE))
    else:
        print("A == E should be False, test failed.")
        return
    if not personA != personB:
        print("A != B: " + str(personA != personB))
    else:
        print("A != B should be False, test failed.")
        return
    if personA != personC:
        print("A != C: " + str(personA != personC))
    else:
        print("A != C should be True, test failed.")
        return
    if personA != personD:
        print("A != D: " + str(personA != personD))
    else:
        print("A != D should be True, test failed.")
        return
    if personA != personE:
        print("A != E: " + str(personA != personE))
    else:
        print("A != E should be True, test failed.")
        return
    # Separator
    print("TEST 1 PASSED")
    print('\n')
    # Test __repr__ function, expected output should be "Person(__repr__) Name: Tom; Gender: Male; Age: 30;"
    
    personX = Person("Tom", "Male", 20)
    personY = Person("Jack", "Male", 20)
    personZ = Person("Jack", "Male", 30)
    print("Testing __ge__ and __le__ funciton")
    print("Person information: ")
    print("X: " + str(personX))
    print("Y: " + str(personY))
    print("Z: " + str(personZ))
    if personX <= personY:
        print("X <= Y: " + str(personX <= personY))
    else:
        print("X <= Y should be True, test failed.")
        return
    if personX >= personY:
        print("X >= Y: " + str(personX >= personY))
    else:
        print("X >= Y should be True, test failed.")
        return
    if not personX >= personZ:
        print("X >= Z: " + str(personX >= personZ))
    else:
        print("X >= Z should be False, test failed.")
        return
    if personX <= personZ:
        print("X <= Z: " + str(personX <= personZ))
    else:
        print("X <= Z should be True, test failed.")
        return
    
    # Separator
    print("TEST 2 PASSED")
    print('\n')

if __name__ == '__main__':
    main()