f = open("custom_led_dump.txt", 'r')
lines = f.readlines()
f.close()

# f = open("custom_keys.csv", "w+")

labels = lines[0]
col = lines[1]

count = 0

op = []

for i in range(0, 756, 9):
    if len(str(labels[i:i+9]).strip()) > 0:
        count += 1
        print(str(labels[i:i+9]).strip() + ",255,255,255")
        op.append(str(labels[i:i+9]).strip())
        # print(col[i:i+9])
        # print()
    # else:
    #     print("NULL")
    #     op.append("NULL")
        # print()
        # f.write(str(labels[i:i+9]).strip() + "," + str(col[i:i+9]).replace(" ", ",") + "\n")

# f.close()

print(count)
# print(op)