from dataclasses import dataclass

# data class of base config for usb report 
@dataclass
class BaseConfig:
    ANIMATION_TYPE: oct
    ANIMATION_SPEED: oct
    ANIMATION_BRIGHTNESS: oct
    ANIMATION_GREEN: oct
    ANIMATION_RED: oct
    ANIMATION_BLUE: oct
    ANIMATION_RAINBOW: oct
    ANIMATION_SLEEP_DURATION: oct