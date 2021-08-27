import cv2
import numpy
def check(node):
    return node[0] >= 0 and node[0] < 500 and node[1] >=0 and node[1] < 500

def same(x, y):
    sum1 = 0
    sum1 += x[0]
    sum1 += x[2]
    sum1 += x[1]
    sum2 = 0
    sum2 += y[0]
    sum2 += y[2]
    sum2 += y[1]
    return abs(sum1 - sum2) < 300
    

def findEdge(x, y):
    direction = [[1,0], [-1,0],[0,1],[0,-1]]
    img = cv2.imread("in.jpg", 1)
    print(img[77][120])
    nodeList = []
    table = numpy.zeros([500, 500],dtype=numpy.int8)
    edgeNode = []
    node = [x, y]
    if check(node):
        nodeList.append(node)
        table[x][y] = 1
    while len(nodeList) != 0:
        table[nodeList[0][0]][nodeList[0][1]] = 1
        for i in range(4):
            n = [x, y]
            n[0] = nodeList[0][0]
            n[1] = nodeList[0][1]
            n[0] += direction[i][0]
            n[1] += direction[i][1]
            if check(n) and table[n[0]][n[1]] == 0:
                if same(img[n[0]][n[1]], img[x][y]):
                    nodeList.append(n)
                    table[n[0]][n[1]] = 1
                else:
                    edgeNode.append(n)
                    table[n[0]][n[1]] = 1
        nodeList.pop(0)
    return edgeNode           

def process():
    img = cv2.imread("input.jpg", 1)
    print(img[77][120])
    for i in range(500):
        for j in range(500):            
            sum = 0
            sum += img[i][j][0]
            sum += img[i][j][1]
            sum += img[i][j][2]
            if (sum < 300):
                img[i][j][0] = img[i][j][1] = img[i][j][2] = 0
            else:
                img[i][j][0] = img[i][j][1] = img[i][j][2] = 255
    cv2.imwrite("in.jpg", img)
    print(img[77][120])

# if __name__ == "__main__":
#     edgeNode = findEdge(257, 288)
#     edgeNode1 = findEdge(260, 310)
#     table = numpy.zeros([500, 500],dtype=numpy.int8)
#     for n in edgeNode1:
#         table[n[0]][n[1]] = 1    
#     file = open("10.txt", "w")
#     for n in edgeNode:
#         if table[n[0]][n[1]] != 1 and table[n[0] - 1][n[1]] != 1 and table[n[0] + 1][n[1]] != 1 and table[n[0]][n[1] - 1] != 1 and table[n[0]][n[1] + 1] != 1:
#             file.write(str(n[0]))
#             file.write(" ")
#             file.write(str(n[1]))
#             file.write("\n")
#     file.close()
#     file = open("t.txt", "w")
#     t = numpy.zeros([500, 500],dtype=numpy.int8)
#     for n in edgeNode:
#         if table[n[0]][n[1]] != 1 and table[n[0] - 1][n[1]] != 1 and table[n[0] + 1][n[1]] != 1 and table[n[0]][n[1] - 1] != 1 and table[n[0]][n[1] + 1] != 1:
#             t[n[0]][n[1]] = 1
#     for i in range(500):
#         for j in range(500):
#             if t[i][j] == 1:
#                 file.write("-")
#             else:                
#                 file.write(" ")
#         file.write("\n")
#     file.close()
#     # process()

if __name__ == "__main__":
    t = numpy.zeros([500, 500],dtype=numpy.int8)
    file = open("edges/1.txt", "r")
    line = file.readline()
    while(line):
        nums = line.split(" ")
        t[int(nums[0])][int(nums[1])] = 1
        line = file.readline()
    file.close()
    file = open("edges/2.txt", "r")
    line = file.readline()
    while(line):
        nums = line.split(" ")
        t[int(nums[0])][int(nums[1])] = 1
        line = file.readline()
    file.close()
    file = open("t.txt", "w")
    for i in range(500):
        for j in range(500):
            if t[i][j] == 1:
                file.write("-")
            else:                
                file.write(" ")
        file.write("\n")
    file.close()