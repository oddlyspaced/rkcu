from dataclasses import dataclass
from .enums import Speed, Brightness, RainbowMode, Sleep

# data class of base config for usb report 
@dataclass
class BaseConfig:
    ANIMATION_TYPE: oct
    ANIMATION_SPEED: Speed
    ANIMATION_BRIGHTNESS: Brightness
    ANIMATION_GREEN: int
    ANIMATION_RED: int
    ANIMATION_BLUE: int
    ANIMATION_RAINBOW: RainbowMode
    ANIMATION_SLEEP_DURATION: Sleep

    def __init__(self, speed: Speed = Speed.SPEED_5, brightness: Brightness = Brightness.BRIGHTNESS_5, red: int = 255, green: int = 255, blue: int = 255, is_rainbow: RainbowMode = RainbowMode.OFF, sleep: Sleep = Sleep.SLEEP_NEVER) -> None:
        self.ANIMATION_TYPE = 0x01
        self.ANIMATION_SPEED = speed
        self.ANIMATION_BRIGHTNESS = brightness
        self.ANIMATION_RED = red
        self.ANIMATION_GREEN = green
        self.ANIMATION_BLUE = blue
        self.ANIMATION_RAINBOW = is_rainbow
        self.ANIMATION_SLEEP_DURATION = sleep

    def report(self) -> bytearray:
        report = bytearray(65)
        report[0] = 0x0a
        report[1] = 0x01
        report[2] = 0x01
        report[3] = 0x02
        report[4] = 0x29
        report[5] = self.ANIMATION_TYPE
        report[6] = 0x00
        report[7] = self.ANIMATION_SPEED.value

        report[8] = self.ANIMATION_BRIGHTNESS.value
        report[9] = self.ANIMATION_GREEN
        report[10] = self.ANIMATION_RED
        report[11] = self.ANIMATION_BLUE
        report[12] = self.ANIMATION_RAINBOW.value
        report[13] = self.ANIMATION_SLEEP_DURATION.value

        return report