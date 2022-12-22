from dataclasses import dataclass
from .enums import Animation, Speed, Brightness, RainbowMode, Sleep

# data class of base config for usb report 
@dataclass
class Config:
    ANIMATION_TYPE: Animation
    ANIMATION_SPEED: Speed
    ANIMATION_BRIGHTNESS: Brightness
    ANIMATION_GREEN: int
    ANIMATION_RED: int
    ANIMATION_BLUE: int
    ANIMATION_RAINBOW: RainbowMode
    ANIMATION_SLEEP_DURATION: Sleep

    def __init__(self, animation: Animation, speed: Speed, brightness: Brightness, red: int, green: int, blue: int, is_rainbow: RainbowMode, sleep: Sleep) -> None:
        self.ANIMATION_TYPE = animation
        self.ANIMATION_SPEED = speed
        self.ANIMATION_BRIGHTNESS = brightness
        self.ANIMATION_RED = red
        self.ANIMATION_GREEN = green
        self.ANIMATION_BLUE = blue
        self.ANIMATION_RAINBOW = is_rainbow
        self.ANIMATION_SLEEP_DURATION = sleep
    
    def update(self, var: dict):
        self.ANIMATION_TYPE = Animation.from_value("neon_stream" if var['animation'] == None else var['animation'])
        self.ANIMATION_SPEED = Speed.from_value(5 if var['speed'] == None else int(var['speed']))
        self.ANIMATION_BRIGHTNESS = Brightness.from_value(5 if var['brightness'] == None else int(var['brightness']))
        self.ANIMATION_RED = int(255 if var['red'] == None else var['red'])
        self.ANIMATION_GREEN = int(255 if var['green'] == None else var['green'])
        self.ANIMATION_BLUE = int(255 if var['blue'] == None else var['blue'])
        self.ANIMATION_RAINBOW = RainbowMode.from_value(var['rainbow'])
        self.ANIMATION_SLEEP_DURATION = Sleep.from_value(5 if var['sleep'] == None else int(var['sleep']))

    def report(self) -> bytearray:
        report = bytearray(65)
        report[0] = 0x0a
        report[1] = 0x01
        report[2] = 0x01
        report[3] = 0x02
        report[4] = 0x29
        report[5] = self.ANIMATION_TYPE.value
        report[6] = 0x00
        report[7] = self.ANIMATION_SPEED.value

        report[8] = self.ANIMATION_BRIGHTNESS.value
        report[9] = self.ANIMATION_GREEN
        report[10] = self.ANIMATION_RED
        report[11] = self.ANIMATION_BLUE
        report[12] = self.ANIMATION_RAINBOW.value
        report[13] = self.ANIMATION_SLEEP_DURATION.value

        return report

def get_base_config() -> Config:
    config = Config(
        Animation.NEON_STREAM,
        Speed.SPEED_5,
        Brightness.BRIGHTNESS_5,
        255,
        255,
        255,
        RainbowMode.OFF,
        Sleep.SLEEP_NEVER
    )
    return config