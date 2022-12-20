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

class Animation(Enum):
    NEON_STREAM = 0x01
    RIPPLES_SHINING = 0x02
    ROTATING_WINDMILL = 0x03
    SINE_WAVE = 0x04 
    RAINBOW_ROULETTE = 0x05
    STARS_TWINKLE = 0x06
    LAYER_UPON_LAYER = 0x07
    RICH_AND_HONORED = 0x08
    MARQUEE_EFFECT = 0x09
    ROTATING_STORM = 0x0a
    SERPENTINE_HORSE = 0x0b
    RETRO_SNAKE = 0x0c
    DIAGONAL_TRANSFORMER = 0x0d
    # CUSTOMIZE = 0x0e
    AMBILIGHT = 0x0f
    STREAMER = 0x10
    STEADY = 0x11
    BREATHING = 0x12
    NEON = 0x13
    SHADOW_DISAPPEAR = 0x14
    FLASH_AWAY = 0x15
    # MUSIC = 0x16