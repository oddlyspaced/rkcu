import hid
from src.config import BaseConfig

RK61_VID = 0x258a
RK61_PID = 0x004a

config = BaseConfig()
report = config.report()

print("Sending report to Keyboard: " + report.hex(" "))

rk61 = hid.enumerate(RK61_VID, RK61_PID)
kb_path = rk61[1].get('path')

h = hid.device()
h.open_path(kb_path)

h.send_feature_report(bytes(report))
h.close()