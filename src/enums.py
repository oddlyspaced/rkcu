from enum import Enum

class Speed(Enum):
    SPEED_1 = 0x01
    SPEED_2 = 0x02
    SPEED_3 = 0x03
    SPEED_4 = 0x04
    SPEED_5 = 0x05

class Brightness(Enum):
    BRIGHTNESS_0 = 0x00
    BRIGHTNESS_1 = 0X01
    BRIGHTNESS_2 = 0X02
    BRIGHTNESS_3 = 0X03
    BRIGHTNESS_4 = 0X04
    BRIGHTNESS_5 = 0X05

class RainbowMode(Enum):
    OFF = 0x00
    ON = 0x01

class Sleep(Enum):
    SLEEP_5_MIN = 0x01
    SLEEP_10_MIN = 0x02
    SLEEP_20_MIN = 0x03
    SLEEP_30_MIN = 0x04
    SLEEP_NEVER = 0x05