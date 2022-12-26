f = open("merged.txt", "r")
lines = f.readlines()
f.close()

for i in range (0, 256, 15):
    print(i)
    f = open("L_" + str(i) + ".txt", "w+")
    lines[21] = "L,0," + str(i) + ",0\n"
    f.writelines(lines)
    f.close()

f = open("merged.txt", "r")
lines = f.readlines()
f.close()

for i in range (0, 256, 15):
    print(i)
    f = open("O_" + str(i) + ".txt", "w+")
    lines[24] = "O,0," + str(i) + ",0\n"
    f.writelines(lines)
    f.close()

f = open("merged.txt", "r")
lines = f.readlines()
f.close()

for i in range (0, 256, 15):
    print(i)
    f = open("D_" + str(i) + ".txt", "w+")
    lines[13] = "D,0," + str(i) + ",0\n"
    f.writelines(lines)
    f.close()

f = open("merged.txt", "r")
lines = f.readlines()
f.close()

for i in range (0, 256, 15):
    print(i)
    f = open("U_" + str(i) + ".txt", "w+")
    lines[30] = "U,0," + str(i) + ",0\n"
    f.writelines(lines)
    f.close()