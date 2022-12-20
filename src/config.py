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

    def report(self) -> bytearray:
        report = bytearray(65)
        report[0] = 0x0a
        report[1] = 0x01
        report[2] = 0x01
        report[3] = 0x02
        report[4] = 0x29
        report[5] = self.ANIMATION_TYPE
        report[6] = 0x00
        report[7] = self.ANIMATION_SPEED

        report[8] = self.ANIMATION_BRIGHTNESS
        report[9] = self.ANIMATION_GREEN
        report[10] = self.ANIMATION_RED
        report[11] = self.ANIMATION_BLUE
        report[12] = self.ANIMATION_RAINBOW
        report[13] = self.ANIMATION_SLEEP_DURATION

        return report