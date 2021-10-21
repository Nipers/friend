'''
CSC373 Fall 2021
Problem Set 2, Visiting All Squares
University of Toronto Mississauga
'''

# Do NOT add any "import" statements


def cheapest_cost(dist):
    '''
    dist[i][j] is the cost to move directly from square i to square j.
    dist[i][j] may be different than dist[j][i].
    dist[i][i] = 0 for all i.

    Playing the game involves starting on some square and visiting
    each other square exactly once, subject to the following rule:
    for each square v, you must visit all squares < v before visiting v
    or you must visit all squares < v after visiting v.
    For example, visiting squares in the order 1, 2, 0 is not allowed.

    Return the cheapest cost to play the game.
    '''
    pass  # TODO: implement this function

if __name__ == '__main__':

    # some small test cases
    # Case 1
    dist = [[0, 8, 2], [4, 0, 1], [3, 5, 0]]
    print(cheapest_cost(dist))  # Answer should be 6
    # To get 6, you can do 1 -> 0 -> 2
