import time
from neopixel import NeoPixel
from machine import Pin
LED_GPIO = const(27)

np = NeoPixel(Pin(LED_GPIO),25)

heart = [
        [(0,0,0), (211,55,62), (0,0,0), (211,55,62), (0,0,0)],
        [(211,55,62), (234,147,145), (211,55,62), (234,147,145), (211,55,62)],
        [(211,55,62), (232,139,138), (239,171,165), (234,147,145), (211,55,62)],
        [(0,0,0), (211,55,62), (233,140,139), (211,55,62), (0,0,0)],
        [(0,0,0), (0,0,0), (211,55,62), (0,0,0), (0,0,0)]
]

icon = heart
maxpixval = max([max(i) for i in icon])

# scale back RGB values to be at most "20" (as higher could break the device)
for l in range(len(icon)):
	icon[l] = list(map(lambda i: int(i // (maxpixval/20)), icon[l]))

# show pixels
for l in range(len(icon)):
	np[l] = icon[l]

np.write()
