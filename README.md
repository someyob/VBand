This is my CircuitPython implementation of the VBand interface.  https://hamradio.solutions/vband/
My thanks to them for creating such a useful resource.  If you want to support them, you can buy their VBand interface as an alternative to this.

![PXL_20251125_161237552](https://github.com/user-attachments/assets/eb60c857-1c45-4734-a13b-58c6c3f1b028)

![PXL_n](https://github.com/user-attachments/assets/3f8ea57e-bf10-4858-99fc-c1a3edd5cfd0)

My thanks also to KD8RTT at https://kd8rtt.com/2024/04/28/diy-paddle-interface-for-vband-cw-practice-website/ and
OZ1JHM http://www.oz1jhm.dk/content/hamradio-solutions-vband-interface for the inspiration and some helpful hints.

I built and tested this on an Adafruit Feather RP2040, just because it was capable of running as an HID device, and I had it kicking around my parts bin with nothing better to do.  It's very overpowered for this application, but so be it.  
You could probably also get this running on another RP2040 board, such as the Rasberry Pi Pico.

It's a very trivial little program, as you will see from the src file.  CircuitPython doesn't support interrupts in a straightforward way, so I abandoned attempts to get it working with interrupts.
The polling method seems to work fine, but I'd be very appreciative if anyone finds any issues to let me know.

A few provisos:
1. You need to have the VBand window in focus for the keystrokes [ and ] to be transmitted to the website.
2. This implementation can use either a straight key or paddle.  The jack is stereo, so either one will work if you set VBand for 
the appropriate kind of key.
3. The feather (or Pico if that's what you're using) will want to connect to your PC as a storage device.  This doesn't hurt anything, but if you choose, there are ways to prevent that behaviour.
4. The case in the 3mf folder was designed for my protoboard, so may not work for you.
5. The key/paddle left and right are wired to A0 and A1, with sleeve of the jack going to ground.  Be sure to adapt the code to your wiring.
