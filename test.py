if __name__ == "__main__":
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
    file.close()
    buy = []
    sell = []
    buy.append(0)
    sell.append(0)
    for p in price:
        buy.append(p / 0.991 / 0.9)
        sell.append(p * 0.991 * 0.9)
    file = open("RS.txt", "r")
    gain = 0
    behind = 0
    front = 0
    capB = 0
    capF = 0
    line = file.readline().replace("\n", "")
    info = line.split(" ")
    front = int(info[0])
    capF = int(info[1])
    ls = []
    distance = 0
    intstuctor = file.readline().replace("\n", "")
    while intstuctor:
        line = file.readline().replace("\n", "")
        info = line.split(" ")
        behind = int(info[0])
        distance = max(distance, behind - front)
        capB = int(info[1])
        if intstuctor == "B":
            gain += (capF - capB) * buy[behind]
        elif intstuctor == "S":
            gain += (capF - capB) * sell[behind]
        ls.append(gain)
        front = behind
        capF = capB
        intstuctor = file.readline().replace("\n", "")
    file.close()
    # file = open("g.txt", "w")
    # for g in ls:
    #     file.write(str(g) + "\n")
    # file.close()
    print(gain)
    print(distance)


