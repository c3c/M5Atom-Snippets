# scrolls some text over the screen

import time
from machine import Pin
from neopixel import NeoPixel
LED_GPIO = const(27)

np = NeoPixel(Pin(LED_GPIO),25)

import font

def torgb(x):
        if type(x) == tuple or type(x) == list:
                return x
        if x == "x":
                return (20,20,20)
        else:
                return (0,0,0)

scrolltext1 = "HELLO WORLD    "
mapped1 = map(lambda x: [[j for j in i] for i in font.font[x]], scrolltext1)
restext = [sum(i,[]) for i in zip(*mapped1)]

while True:
        posleds = 0
        while posleds < len(restext[0])-5:

                for i in range(5):
                        np[0 + 5*i] = torgb(restext[i][posleds+0])
                        np[1 + 5*i] = torgb(restext[i][posleds+1])
                        np[2 + 5*i] = torgb(restext[i][posleds+2])
                        np[3 + 5*i] = torgb(restext[i][posleds+3])
                        np[4 + 5*i] = torgb(restext[i][posleds+4])

                np.write()

                posleds += 1
                time.sleep(0.2)
