'''
Xinyi Di
2021-12-04
Exercise 2.4
'''

'''
Main project
Use and test dir function and metadata.
'''

class Person(object):
    _name = "Tom"
    _gender = "Male"
    _age = 30
    def __init__(self, name = None, gender = None, age = None):
        if name != None:
            self._name = name
        else:
            self._name = Person._name
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
    print('\n=============== Exercise 2.5 ===============')
    print("\n")
    print("Test dir function")
    print(dir(Tom))
    print("TEST dir function OK")
    print("\n")
    print("Test __class__ and __name__")
    if str(Tom.__class__) == "<class '__main__.Person'>":
        print(Tom.__class__)
    else:
        print("expect <class '__main__.Person'>, get {}. Test failed.".format(Tom.__class__))
        return    
    if Tom.__class__.__name__ == "Person":
        print(Tom.__class__.__name__)
    else:
        print("expect Person, get {}. Test failed.".format(Tom.__class__.__name__))
        return
    
    ClassInst = Tom.__class__
    Jack = ClassInst()
    if str(Jack.__class__) == "<class \'__main__.Person\'>":
        print(Jack.__class__)
    else:
        print("expect <class '__main__.Person'>, get {}. Test failed.".format(Jack.__class__))
        return
    print("TEST __class__ and __name__ OK")
    # Although there are _name, _gender and _age for Tom, if you don't set them explicitly, the __dict__ won't output the default value
    print("\n")
    print("Test __dict__")
    print("Initial Information:")
    print(Tom.__dict__)
    print("Set _height:")    
    Tom.setHeight()
    print(Tom.__dict__)
    print("Set _age:")  
    Tom._age = 29
    print(Tom.__dict__)
    print("TEST __dict__ OK")
    
    print("\n")
    print("Test __module__")
    if Jack.__module__ == "__main__":
        print(Jack.__module__)
    else:
        print("expect __main__, get {}, test failed.".format(Jack.__module__))
        return
    print("TEST __module OK")
    print()
    print("TEST PASSED")

if __name__ == '__main__':
    main()