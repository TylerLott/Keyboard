import busio
import gc
from typing import List
from abc import ABC, abstractmethod

import adafruit_displayio_ssd1306
import displayio
import terminalio
from adafruit_display_text import label

from kmk.extensions import Extension
from PIL import Image

class OledData:
    '''
    Stores the current bitmap data
    '''
    def __init__(self, height=128, width=32):
        self.height = height
        self.width = width
        self.image = Image.new(1, (self.width,self.height), 0)

    def update(x: int, y: int, new_data: Image):
        self.image.paste(new_data, (x,y))

class OledComponent(ABC):
    def __init__(x, y):
        self.x = x 
        self.y = y

    @abstractmethod
    def update(self, oled_data: OledData):
        '''updates the screen where the component exists'''
        pass

    @abstractmethod
    def clear(self, oled_data: OledData):
        '''clear the screen where component exists'''
        pass

class Animation(OledComponent):
    '''
    Animation based on bitmap files
    '''
    def __init__(self, x:int, y:int, frames: List[str]):
        super().__init__(x,y)
        self.animation = []
        self.cur_frame = 0

    def update(self, oled_data: OledData):
        oled_data.update(self.x,self.y,self.animation[self.cur_frame])
        self.cur_frame += 1

    def clear(self):
        pass

class Text(OledComponent):
    def __init__(self, x:int, y:int, font):
        super().__init__(x,y)

class Image(OledComponent):
    def __init__(self, x:int, y:int, font):
        super().__init__(x,y)


class Oled(Extension):
    '''
    Main kmk extension
    '''
        def __init__(
        self,
        views,
        toDisplay=OledDisplayMode.TXT,
        oWidth=128,
        oHeight=32,
        flip: bool = False,
    ):
        displayio.release_displays()
        self.rotation = 180 if flip else 0
        self._views = views.data
        self._toDisplay = toDisplay
        self._width = oWidth
        self._height = oHeight
        self._prevLayers = 0
        gc.collect()

    def updateOLED(self, sandbox):
        gc.collect()

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, keyboard):
        displayio.release_displays()
        i2c = busio.I2C(keyboard.SCL, keyboard.SDA)
        self._display = adafruit_displayio_ssd1306.SSD1306(
            displayio.I2CDisplay(i2c, device_address=0x3C),
            width=self._width,
            height=self._height,
            rotation=self.rotation,
        )
        return

    def before_matrix_scan(self, sandbox):
        if sandbox.active_layers[0] != self._prevLayers:
            self._prevLayers = sandbox.active_layers[0]
            self.updateOLED(sandbox)
        return

    def after_matrix_scan(self, sandbox):

        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return

