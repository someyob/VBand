This is my CircuitPython implementation of the VBand interface.  https://hamradio.solutions/vband/
My thanks to them for creating such a useful resource.  If you want to support them, you can buy their VBand interface as an alternative to this.

My thanks also to KD8RTT at https://kd8rtt.com/2024/04/28/diy-paddle-interface-for-vband-cw-practice-website/ and
OZ1JHM http://www.oz1jhm.dk/content/hamradio-solutions-vband-interface for the inspiration and some helpful hints.

I built and tested this on an Adafruit Feather RP2040, just because it was capable of running as an HID device, and I had it kicking around my parts bin with nothing better to do.  It's very overpowered for this application, but so be it.  
You could probably also get this running on another RP2040 board, such as the Rasberry Pi Pico.

A couple of provisos:
1. You need to have the VBand window in focus for the keystrokes [ and ] to be transmitted to the website.
2. This implementation can use either a straight key or paddle.  The jack is stereo, so either one will work if you set VBand for 
the appropriate kind of key.
