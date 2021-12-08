'''
Xinyi Di
2021-12-04
Exercise 2.6
'''

'''
Main project
Test Mixin class.
'''

class MappingMixin:
    def __getitem__(self, key):
        return self.__dict__.get(key)

    def __setitem__(self, key, value):
        self.__dict__[key] =  value

class StrMixin:
    def __str__(self) -> str:
        s = ""
        for k, v in self.__dict__.items():
            s += '{}: {}; '.format(k, v)
        return s
    
class Person(MappingMixin, StrMixin):
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
        else:
            self._gender = Person._gender
        if age != None:
            self._age = age
        else:
            self._age = Person._age
    
    
def main():
    print('\n=============== Exercise 2.6 ===============')
    personA = Person()
    print("\n")
    # Test the MappingMixin class.
    print("Test __getitem__ and __setitem__ function in the MappingMixin class.")
    if (personA["_name"] != "Tom"):
        print("expect \'Tom\', get {}. Test failed.".format(personA["_name"]))
        return
    print("A's name is " + personA["_name"])
    print("Change A's name to John")
    personA["_name"] = "John"
    if (personA["_name"] != "John"):
        print("expect \'John\', get {}. Test failed.".format(personA["_name"]))
        return
    print("Now, A's name is " + personA["_name"])
    
    print("Test MappingMixin OK")
    print("\n")
    
    print("Test __str__ function in the StrMixin class.")
    if str(personA) != "_name: John; _gender: Male; _age: 30;":
        print("")
    print("personA's information: " + str(personA))
    
    print("Test StrMixin OK")
    
    print()
    print("TEST PASSED")
    
    
    
    
    


if __name__ == '__main__':
    main()