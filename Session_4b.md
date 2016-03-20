# Session 4b - 19 March 2016 - BitScope version

### Goal
_ Getting images through the BitScope tool. _

### TL;DR
- Getting images, but more series of points.

### Setup
### Hardware
- Murgen 1.0
- Hackaday Trinket Pro
- 5/3.3V alim
- Bitscope micro (BS05)

#### Give me files

- Troubleshooting for the install of bitscope is at bitscope/InstallingBitScope.readme
- The code lies at bitscope/acquire.py
- The data is at bitscope/bitscope_data/*.log

#### Remarks 
- Same setup as [Session 4](Session_4.md), and same remarks apply.
- Even though  ```MY_SIZE = 18000```, ```wc -l``` indicates 12000 items. At 20MHz, that's 600us worth of data, or a full two signals

### Discussion and issues

#### Discussion
- Getting our first pulses with the BitScope DSO:

![BitScope_15](/Images/Session_4b/BitScope15.png)

- Getting the first logs using BitScope Python API

#### Issues
- BitScope only trigs on "wide" pulses, so we had to add a 10us pulse from the Arduino so to trig on this signal, not on errors from the Arduino pulser. We got Pin11 do this, still playing with PORTB.
- On the following image, we see on the first line that the first pulse is quite wide because the double echo we see at 60us is characteristic of a wide pulse.

![BitScope_16](/Images/Session_4b/BitScope016.png)

#### Next steps
- Trigging from Ch A to get Ch B.
- Getting more info in the files:
-- Time of pulse
-- Sampling frequency
-- Number of pulse
-- ...

## Images
#### Getting a pulse
![BitScope_15](/Images/Session_4b/BitScope015.png)
#### Issues with trigging from a short pulse: it only triggs on "wide" pulses
![BitScope_16](/Images/Session_4b/BitScope016.png)
#### Solving the issue of the trigger
![BitScope_20](/Images/Session_4b/BitScope20.png)





