import hid
import time
from src.config import BaseConfig
from src.enums import Animation

RK61_VID = 0x258a
RK61_PID = 0x004a

for i in Animation:
    print(i)
    config = BaseConfig()
    config.ANIMATION_TYPE = i
    report = config.report()
    print("Sending report to Keyboard: " + report.hex(" "))
    rk61 = hid.enumerate(RK61_VID, RK61_PID)
    kb_path = rk61[1].get('path')
    h = hid.device()
    h.open_path(kb_path)
    h.send_feature_report(bytes(report))
    h.close()
    time.sleep(5)