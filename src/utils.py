import hid
from .config import Config

# utility class for RK Color Utility
class RKCU:
    def __init__(self, vid, pid):
        self.device = self.find_kb_hid(vid, pid)
    
    def find_kb_hid(self, vid, pid):
        rk61 = hid.enumerate(vid, pid)
        kb_path = rk61[1].get('path') # serial path for keyboard usb
        h = hid.device()
        h.open_path(kb_path)
        return h
    
    def apply_config(self, config: Config):
        self.device.send_feature_report(bytes(config.report()))
    
    def close_kb(self):
        self.device.close()