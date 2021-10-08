file = open("S.txt", "r")
ls = []
line = file.readline()
while line:
    ls.append(line)
    line = file.readline()
file.close()
f = open("RS.txt", "w")
for i in range(len(ls) - 1, -1, -1):
    f.write(ls[i])
f.close()
