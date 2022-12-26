import hid
import sys

print(sys.argv[1])

merged = {}
f = open(sys.argv[1], "r")
lines = f.readlines()
for line in lines:
    spl = line.strip().split(",")
    merged[spl[0]] = spl[1:]
f.close()

print(merged)

key_sequence = ['NULL', 'Esc', 'Tab', 'Caps_Lock', 'Shift_L', 'Ctrl_L', 'NULL', '1', 'Q', 'A', 'Z', 'Super', 'NULL', '2', 'W', 'S', 'X', 'Alt_L', 'NULL', '3', 'E', 'D', 'C', 'NULL', 'NULL', '4', 'R', 'F', 'V', 'NULL', 'NULL', '5', 'T', 'G', 'B', 'Space', 'NULL', '6', 'Y', 'H', 'N', 'NULL', 'NULL', '7', 'U', 'J', 'M', 'NULL', 'NULL', '8', 'I', 'K', '<', 'Alt_R', 'NULL', '9', 'O', 'L', '>', 'Menu', 'NULL', '0', 'P', ':', '?', 'Ctrl_R', 'NULL', '-', '[', "'", 'NULL', 'NULL', 'NULL', '=', ']', 'NULL', 'NULL', 'NULL', 'NULL', 'Backspace', '\\', 'Enter', 'Shift_R', 'Fn']
sequence_starts = [6, 3, 3, 3, 3, 3, 3]
sequences = [bytearray(65), bytearray(65), bytearray(65), bytearray(65), bytearray(65), bytearray(65), bytearray(65)]

colors = []

for key in key_sequence:
    if key == 'NULL':
        colors.append(0x00)
        colors.append(0x00)
        colors.append(0x00)
    else :
        merged[key]
        colors.append(int(merged[key][0])) # G
        colors.append(int(merged[key][1])) # R
        colors.append(int(merged[key][2])) # B

key_index = 0

# prepping byte arrays
for index in range(0, 7):
    sequences[index][0] = 0x0a
    sequences[index][1] = 0x07
    sequences[index][2] = index + 1

sequences[0][3] = 0x03
sequences[0][4] = 0x7e
sequences[0][5] = 0x01

for index in range(0, 7):
    seq = sequences[index]
    for ind in range(sequence_starts[index], 65):
        if (key_index == len(colors)):
            break
        seq[ind] = colors[key_index]
        key_index += 1

vid = 0x258a
pid = 0x004a

rk61 = hid.enumerate(vid, pid)
kb_path = rk61[1].get('path') # serial path for keyboard usb
h = hid.device()
h.open_path(kb_path)

for seq in sequences:
    h.send_feature_report(bytes(seq))

h.close()