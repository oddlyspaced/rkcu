import hid

vid = 0x258a
pid = 0x004a

rk61 = hid.enumerate(vid, pid)
kb_path = rk61[1].get('path') # serial path for keyboard usb
h = hid.device()
h.open_path(kb_path)

def gen_report(line: str):
    global h
    report = bytearray(65)
    spl = line.split(" ")
    for index in range(0, 65):
        report[index] = int(spl[index], 16)
    h.send_feature_report(bytes(report))

f = open('custom_led_dump.txt', 'r')
lines = f.readlines()
f.close()

for line in lines:
    if line[0] != '#':
        print(line)
        gen_report(line)