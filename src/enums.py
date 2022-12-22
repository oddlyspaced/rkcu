from enum import Enum

class Speed(Enum):
    SPEED_1 = 0x01
    SPEED_2 = 0x02
    SPEED_3 = 0x03
    SPEED_4 = 0x04
    SPEED_5 = 0x05

    @staticmethod
    def from_value(value: int):
        values = {
            1: Speed.SPEED_1,
            2: Speed.SPEED_2,
            3: Speed.SPEED_3,
            4: Speed.SPEED_4,
            5: Speed.SPEED_5,
        }
        if value in list(values.keys()):
            return values[value]
        else :
            print("warning: unable to find specified speed, using Speed 5")
            return Speed.SPEED_5 # default value

class Brightness(Enum):
    BRIGHTNESS_0 = 0x00
    BRIGHTNESS_1 = 0X01
    BRIGHTNESS_2 = 0X02
    BRIGHTNESS_3 = 0X03
    BRIGHTNESS_4 = 0X04
    BRIGHTNESS_5 = 0X05

    @staticmethod
    def from_value(value: int):
        values = {
            0: Brightness.BRIGHTNESS_0,
            1: Brightness.BRIGHTNESS_1,
            2: Brightness.BRIGHTNESS_2,
            3: Brightness.BRIGHTNESS_3,
            4: Brightness.BRIGHTNESS_4,
            5: Brightness.BRIGHTNESS_5,
        }
        if value in list(values.keys()):
            return values[value]
        else :
            print("warning: unable to find specified brightness, using Brightness 5")
            return Brightness.BRIGHTNESS_5 # default value

class RainbowMode(Enum):
    OFF = 0x00
    ON = 0x01

    @staticmethod
    def from_value(value: bool):
        if value:
            return RainbowMode.ON
        else :
            return RainbowMode.OFF

class Sleep(Enum):
    SLEEP_5_MIN = 0x01
    SLEEP_10_MIN = 0x02
    SLEEP_20_MIN = 0x03
    SLEEP_30_MIN = 0x04
    SLEEP_NEVER = 0x05

    @staticmethod
    def from_value(value: int):
        values = {
            1: Sleep.SLEEP_5_MIN,
            2: Sleep.SLEEP_10_MIN,
            3: Sleep.SLEEP_20_MIN,
            4: Sleep.SLEEP_30_MIN,
            5: Sleep.SLEEP_NEVER,
        }
        if value in list(values.keys()):
            return values[value]
        else :
            print("warning: unable to find specified sleep value, using Never Sleep")
            return Sleep.SLEEP_NEVER # default value

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

    @staticmethod
    def from_value(value: str):
        values = {
            "neon_stream": Animation.NEON_STREAM,
            "ripples_shining": Animation.RIPPLES_SHINING,
            "sine_wave": Animation.SINE_WAVE,
            "rainbow_routlette": Animation.RAINBOW_ROULETTE,
            "stars_twinkle": Animation.STARS_TWINKLE,
            "layer_upon_layer": Animation.LAYER_UPON_LAYER,
            "rich_and_honored": Animation.RICH_AND_HONORED,
            "marquee_effect": Animation.MARQUEE_EFFECT,
            "rotating_storm": Animation.ROTATING_STORM,
            "serpentine_horse": Animation.SERPENTINE_HORSE,
            "retro_snake": Animation.RETRO_SNAKE,
            "diagonal_transformer": Animation.DIAGONAL_TRANSFORMER,
            "ambilight": Animation.AMBILIGHT,
            "streamer": Animation.STREAMER,
            "steady": Animation.STEADY,
            "breathing": Animation.BREATHING,
            "neon": Animation.NEON,
            "shadow_disappear": Animation.SHADOW_DISAPPEAR,
            "flash_away": Animation.FLASH_AWAY
        }
        if value in list(values.keys()):
            return values[value]
        else :
            print("warning: unable to find specified animation, using Neon Stream")
            return Animation.NEON_STREAM # default value