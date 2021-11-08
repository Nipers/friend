'''
CSC373 Fall 2021
Problem Set 2, How Many Ways?
University of Toronto Mississauga
'''

# Do NOT add any "import" statements

def num_ways(t, p, k):
    '''t, p, and n are as described in the handout.

    Return the number of matches.
    '''

    m = len(t)
    n = len(p)
    if k > n:
        return 0
    table = []
    for i in range(m):#initialize the table
        table.append([])
        for j in range(n):
            table[i].append([])
            for x in range(k + 1):
                table[i][j].append(0)

    for i in range(m):# t's prefix t[0, i]
        for j in range(min(i + 1, n)): #p's prefix p[0, j]
            for x in range(1, min(i + 1, k) + 1):
                if i == 0:# edge condition: only one character
                    if t[i] == p[j]:
                        table[i][j][1] = 1
                else:
                    table[i][j][x] += table[i - 1][j][x] #t[0, i - 1]'s solutions are all legal for t[0, i]
                    if t[i] != p[j]:#No common suffix
                        continue
                    length = 0
                    while length <= i and length <= j and t[i - length] == p[j - length]:#find the same suffix's length
                        length += 1 
                    
                    for l in range(1, length):# Sum up
                        table[i][j][x] += table[i - l][j - l][x - 1]
                    if length == j + 1:# If t[0, i] = p[0, j]
                        if x == 1:
                            table[i][j][x] += 1    
                    else:
                        table[i][j][x] += table[i - length][j - length][x - 1]
    
    # for i in range(m):# [0,i] of t
    #     print(i, end= " :")
    #     for j in range(min(i + 1, n)):
    #         print(table[i][j], end=" ")
    #     print("")
    return table[m-1][n-1][k]
            


if __name__ == '__main__':

    # some small test cases
    # Case 1
    print(num_ways('hyperlooloopahehyperloophypperloohyperhyphyperhypperhyerlloop', 'hyperloop', 5))  # Answer should be 15193

    # print(num_ways('hyperlooloopahehyperloophypperloohyperhyphyperhypperhyerlloopp', 'hyp', 3))  # Answer should be 238

    # print(num_ways('hyperlooloopahehyperloophypperloohyperhyphyperhypperhyerlloopp', 'hyp', 7))  # Answer should be 0

    # print(num_ways('hyperlooloopahehyperloophypperloohyperhyphyperhypperhyerlloopp', 'hyper', 2))  # Answer should be 108

    # print(num_ways('hyperlooloopahehyperloophypperloohyperhyphyperhypperhyerlloopp', 'loop', 4))  # Answer should be 476

    # print(num_ways('hyperlooloopahehyperloophypperloohyperhyphyperhypperhyerlloopp', 'looh', 1))  # Answer should be 1
    # t = "hyperlooloopahehyperloophypperloohyperhyphyperhypperhyerlloop"
    # l = len(t)
    # s = 0
    # for i in range(l-1, -1, -1):
    #     if t[i] == "p":
    #         sum = 0
    #         print(i, end=": ")
    #         for j in range(i - 1, -1, -1):
    #             if t[j] == "y":
    #                 for k in range(j - 1, -1, -1):
    #                     if t[k] == "p":
    #                         s += 1
    #                         sum += 1
    #         print(sum)
    # print(s)


    # print(num_ways('hyperlooloopahehyperloophypperloohyperhyphyperhypperhyerlloop', 'hyper', 2))  # Answer should be 108

    # print(num_ways('hyperlooloopahehyperloophypperloohyperhyphyperhypperhyerlloop', 'loop', 4))  # Answer should be 476
