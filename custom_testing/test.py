f = open("custom_led_dump.txt", 'r')
lines = f.readlines()
f.close()

labels = lines[0]
col = lines[1]

for i in range(0, 756, 9):
    # if len(str(labels[i:i+9]).strip()) > 0:
        print(str(labels[i:i+9]).strip() + " " + str(i))
        print(col[i:i+9])
        print()