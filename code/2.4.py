'''
Xinyi Di
2021-12-04
Exercise 2.4
'''

'''
Main project
Use and test attributes functions
'''

class Person(object):
    _name = "Tom"
    _gender = "Male"
    _age = 30
    def __init__(self, name = None, gender = None, age = None):
        if name != None:
            self._name = name
        if gender != None:
            self._gender = gender
        if age != None:
            self._age = age
    
    def __str__(self) -> str:
        return "Person(__str__) Name: {}; Gender: {}; Age: {};".format(self._name, self._gender, self._age)
    
    def setHeight(self):
        self._height = 175

def main():
    Tom = Person()
    attributes = ["_name", "_gender", "_age", "_height", "_weight"]
    result = []    
    print('\n=============== Exercise 2.4 ===============')
    print()
    print("Test hasattr and getattr function")
    for attribute in attributes:
        result.append(hasattr(Tom, attribute))
        if (hasattr(Tom, attribute)):
            print("Tom has attribute {}, the value is {}".format(attribute, getattr(Tom, attribute)))
        else:
            print("Tom has no attribute {} for now.".format(attribute))
    if result != [True, True, True, False, False]:
        print("Wrong result, test failed")
        return
    print()
    print("Set Tom's height by setHeight Function.")
    Tom.setHeight()
    if (hasattr(Tom, "_height")):
            print("Tom has attribute {}, the value is {}".format("_height", getattr(Tom, "_height")))
    else:
        print("Tom should have attribute _height now, test failed.")
    
    print()
    print("Set Tom's weight by setattr Function.")
    setattr(Tom, "_weight", 60)
    if (hasattr(Tom, "_weight")):
            print("Tom has attribute {}, the value is {}".format("_weight", getattr(Tom, "_weight")))
    else:
        print("Tom should have attribute _weight now, test failed.")
        
    print()
    print("Now show all attributes of Tom")
    result = []    
    for attribute in attributes:
        result.append(hasattr(Tom, attribute))
        if (hasattr(Tom, attribute)):
            print("Tom has attribute {}, the value is {}".format(attribute, getattr(Tom, attribute)))
        else:
            print("Tom has no attribute {} for now.".format(attribute))
    
    if result != [True, True, True, True, True]:
        print("Wrong result, test failed")
        return
    print("TEST PASSED")

if __name__ == '__main__':
    main()