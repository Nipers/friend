if __name__ == "__main__":
    price = []
    file = open("data.txt", "r")
    line = file.readline()
    while line:
        price.append(float(price))
        line = file.readline()
    buy = []
    sell = []
    buy.append(0)
    sell.append(0)
    for p in price:
        buy.append(p / 0.991)
        sell.append(p * 0.0991 * 0.9)
    dayNum = len(price) + 1
    nodes = []
    for i in range(dayNum):
        nodes.append({})
        nodes[i][0] = [0.0, 0]
    for i in range(1, dayNum):
        for j in range(max(0, i - 100), i):
            for cap in nodes[j]:
                s1 = min(cap, 150), s2 = cap - s1
                b1 = max(135, 580 - cap), b2 = cap + b1
                gain = nodes[j][cap]
                b = gain - b1 * buy[i]
                s = gain + s1 * sell[i]
                if nodes[i].get(b2) == None or b > nodes[i][b2][0]:
                    if i <= 100 or b > 0:
                        nodes[i][b2] = [b, j]
                if nodes[i].get(s2) == None or b > nodes[i][s2][0]:
                    if i <= 100 or s > 0:
                        nodes[i][s2] = [s, j]
                if nodes[i].get(cap) == None or nodes[j][cap][0] > nodes[i][cap][0]:
                    if i <= 100 or nodes[j][cap][0] > 0:
                        nodes[i][cap] = [nodes[j][cap][0], j]
    gain = 0
    front = 0
    cap = 0
    for key in nodes[dayNum - 1]:
        if nodes[dayNum - 1][key][0] > gain:
            gain = nodes[dayNum - 1][key][0]
            front = nodes[dayNum - 1][key][1]
            cap = key
    print(gain)
    behind = dayNum - 1
    path = []
    path.append([behind, cap])
    while front != 0:
        for key in nodes[front]:
            if key > cap and nodes[front][key][0] - nodes[behind][cap][0] == (key - cap) * sell[behind]:
                behind = front, cap = key, front = nodes[front][key][1]
                break
            elif key < cap and nodes[front][key][0] - nodes[behind][cap][0] == (key - cap) * buy[behind]:
                behind = front, cap = key, front = nodes[front][key][1]
                break
            elif nodes[front][key][0] == nodes[behind][cap][0]:
                behind = front, cap = key, front = nodes[front][key][1]
                break
        path.append([behind, cap])
    for p in path:
        print(p)
        print("\n")
        

    




