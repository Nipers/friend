
import time


if __name__ == "__main__":
 
    localtime1 = time.localtime(time.time())
    price = []
    file = open("data.txt", "r")
    line = file.readline()
    x = 0
    while line:
        x += 1
        price.append(float(line))
        line = file.readline()
        if x > 63456:
            break
    buy = []
    sell = []
    buy.append(0)
    sell.append(0)
    for p in price:
        buy.append(p / 0.991 / 0.9)
        sell.append(p * 0.991 * 0.9)
    dayNum = len(price) + 1
    nodes = []
    for i in range(dayNum):
        nodes.append({})
        nodes[i][0] = [0.0, 0]
    for i in range(1, dayNum):
        for j in range(max(0, i - 40), i):
            for cap in nodes[j]:
                s1 = min(cap, 150)
                s2 = cap - s1
                b1 = min(135, 580 - cap)
                b2 = cap + b1
                gain = nodes[j][cap][0]
                b = gain - b1 * buy[i]
                s = gain + s1 * sell[i]
                if nodes[i].get(b2) == None or b > nodes[i][b2][0]:
                    nodes[i][b2] = [b, j]
                if nodes[i].get(s2) == None or s > nodes[i][s2][0]:
                    nodes[i][s2] = [s, j]
                if nodes[i].get(cap) == None or nodes[j][cap][0] > nodes[i][cap][0]:
                    nodes[i][cap] = [nodes[j][cap][0], j]
        print(i)
    gain = 0
    front = 0
    cap = 0
    for key in nodes[dayNum - 1]:
        if nodes[dayNum - 1][key][0] > gain:
            gain = nodes[dayNum - 1][key][0]
            front = nodes[dayNum - 1][key][1]
            cap = key
    behind = dayNum - 1
    path = []
    # print([behind, cap])
    file = open("solution.txt", "w")
    file.write(str(behind) + " " + str(cap) + " " + str(gain))
    while front != 0:
        for key in nodes[front]:
            if key > cap and abs(nodes[behind][cap][0] - nodes[front][key][0] - (key - cap) * sell[behind]) < 1:
                behind = front
                cap = key
                front = nodes[front][key][1]
                file.write("\nS\n")
                file.write(str(behind) + " " + str(cap) + " " + str(nodes[behind][cap][0]))
                # print(nodes[behind])
                # print(cap)
                # print(front)
                # print(nodes[front])
                break
            elif key < cap and abs(nodes[behind][cap][0] - nodes[front][key][0] - (key - cap) * buy[behind]) < 1:
                behind = front
                cap = key
                front = nodes[front][key][1]
                file.write("\nB\n")
                file.write(str(behind) + " " + str(cap) + " " + str(nodes[behind][cap][0]))
                # print(nodes[behind])
                # print(cap)
                # print(front)
                # print(nodes[front])
                break
            elif nodes[front][key][0] == nodes[behind][cap][0]:
                behind = front
                cap = key
                front = nodes[front][key][1]
                file.write("\nN\n")
                file.write(str(behind) + " " + str(cap) + " " + str(nodes[behind][cap][0]))
                # print(nodes[behind])
                # print(cap)
                # print(front)
                # print(nodes[front])
                break
    localtime2 = time.localtime(time.time())
    print(localtime1)
    print(localtime2)
        

    




