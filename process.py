# import xlrd
# from datetime import datetime
# import time
# 1514764800.0 1628985600.0
# file = open("time.txt", "w")
# for i in range(1514764800, 1628987400, 1800):
#     file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(i)) + "\n")
# file.close()

file = open("solution.txt", "r")
f = open("RS.txt", "w")
line = file.readline()
ls = []
while line:
    ls.append(line)
    line = file.readline()
ls.append("B\n")
ls.append("1 0\n")
file.close()
for i in range(len(ls) - 1, -1, -1):
    f.write(ls[i])
f.close()

file = open("RS.txt", "r")
f = open("cap.txt", "w")
infos = []
ls = []
line = file.readline()
info = line.split(" ")[0:2]
info[0] = int(info[0])
info[1] = int(info[1])
infos.append(info)
line = file.readline()
while line:
    line = file.readline()
    info = line.split(" ")[0:2]
    info[0] = int(info[0])
    info[1] = int(info[1])
    infos.append(info)
    line = file.readline()
file.close()
for i in range(1, len(infos)):
    for j in range(infos[i - 1][0], infos[i][0]):
        f.write(str(infos[i - 1][1]) + ".0" + "\n")
f.write("0.0\n")
f.close()


file = open("cap.txt", "r")
f = open("power.txt", "w")
cap = []
line = file.readline().replace("\n", "")
while line:
    cap.append(float(line))
    line = file.readline().replace("\n", "")
file.close()
for i in range(1, len(cap)):
    diff = cap[i] - cap[i - 1]
    if diff > 0:
        f.write(str(-diff * 20 / 9) + "\n")
        if abs(-diff * 20 / 9) > 301:
            print(i)
    elif diff < 0:
        f.write(str(-diff * 2) + "\n")
        if abs(-diff * 2) > 301:
            print(i)
    else:
        f.write("0.0\n")
f.write("0.0\n")
f.close()


file = open("result.csv", "w")
f1 = open("time.txt", "r")
f2 = open("power.txt", "r")
f3 = open("cap.txt", "r")
l1 = []
l2 = []
l3 = []
line = f1.readline().replace("\n", "")
while line:
    l1.append(line)
    line = f1.readline().replace("\n", "")
f1.close()
line = f2.readline().replace("\n", "")
while line:
    l2.append(line)
    line = f2.readline().replace("\n", "")
f2.close()
line = f3.readline().replace("\n", "")
while line:
    l3.append(line)
    line = f3.readline().replace("\n", "")
f1.close()
file.write("datetime,power,capacity\n")
for i in range(len(l1)):
    file.write(l1[i] + "," + l2[i] + "," + l3[i] + "\n")
file.close()
