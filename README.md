# M5Atom-Snippets
Some cruft for the M5Stack Atom

First flash the mciropython firmware:
`esptool.py --chip esp32 write_flash -z 0x1000 esp32-idf4-20191220-v1.12.bin`

Then use `mpfshell` as a REPL, or `ampy` to put files.

NBs:
- Don't set LED RGB values higher than 20. According to M5 that will break your LEDs.
- The (current) Arduino library for M5Atom uses GRB instead of RGB.
- The FTDI for the Atom appears to be FT232R. If your device isn't recognized (e.g. Windows) try that. [Tutorial](https://www.usb-drivers.org/ft232r-usb-uart-driver.html).
