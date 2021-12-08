'''
Xinyi Di
2021-12-04
Exercise 2.7
'''

'''
Main project
Test recursive function.
'''
def fibonacci(N):
    if type(N) is not int:
        print("N should be an integer")
        return None
    if N < 0:
        print("N should be a natural number")
        return None
    l = []
    l.append(1)
    l.append(1)
    while len(l) < N + 1:
        length = len(l)
        l.append(l[length - 2] + l[length - 1])
    return l[N]
    
        

def fibonacciRecursive(N):
    if type(N) is not int:
        print("N should be an integer")
        return None
    if N < 0:
        print("N should be a natural number")
        return None
    if N < 2:
        return 1
    else:
        return fibonacciRecursive(N - 2) + fibonacciRecursive(N - 1)


def main():
    
    print('\n=============== Exercise 2.7 ===============')
    
    # Show simple examples
    print("\n")
    print("Simple examples")
    
    print("Recursive versoin:")
    for i in range(11):
        print(fibonacciRecursive(i), end=", ")
    print("\nIteration version:")
    for i in range(11):
        print(fibonacci(i), end=", ")
    print()
    # Test edge case
    print("\n")
    print("Test edge case.")
    
    if fibonacciRecursive(-1) != None: 
        print("-1 should cause error, test failed.")
        return
    print("Test edge case OK.")
    print("\n")
    
    # Test correctness
    print("Test correctness.")
    for i in range(30):
        if fibonacci(i) != fibonacciRecursive(i):
            print("Diffierent Answer: Iteration: {}, Recursion: {}. Test failed.".format(fibonacci(i), fibonacciRecursive(i)))
            return
    print("Test correctness OK")
    
    print("\n")
    print("TEST PASSED")

if __name__ == '__main__':
    main()