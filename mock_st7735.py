BG_SPI_CS_FRONT = ""

from PIL import Image

class ST7735:
    def __init__(self,
        port=0,
        cs=BG_SPI_CS_FRONT,
        dc=9,
        backlight=25,
        rotation=270,
        spi_speed_hz=4000000
    ):
        pass

    def begin(self):
        pass

    def display(self, image: Image):
        image.show()