# Session 5 - 20 March 2016 - Getting images, BitScope version

## Previous sessions

- [Session 1](Session_1.md) : Powering the board, power use, first (bad) trigging and echoes (06 March 2016)
- [Session 2](Session_2.md) : Non-controlled pulsing, inverters, better echoes (11 March 2016)
- [Session 3](Session_3.md) : Getting controlled pulsing, but width not controlled (15 March 2016)
- [Session 4](Session_4.md) : Width of the pulses is getting controlled =) (19 March 2016)
- [Session 4b](Session_4b.md) : Simple data visualisation with BitScope (19 March 2016)
- [Session 5](Session_5.md) : moving the transducer to get the first image ! (20 March 2016)

## Today

### Goal
_ Getting an actual image through the BitScope tool. _

### TL;DR
- Not too bad =)

![BitScopeFullImage](/bitscope/full_image/20160320-020140-Signal-bitscope-DATA.log-SC.png)

### Setup
#### Organization

- Overall lab place

![DSC_0226.JPG](/Images/Session_5/DSC_0226.JPG)

- Detail of the transducer pool, along with the servo, and the servo/transducer cables

![DSC_0227.JPG](/Images/Session_5/DSC_0227.JPG)

- Detail of the transducer head and the rotating device. Yes, it's cracked, but it works!

![DSC_0228.JPG](/Images/Session_5/DSC_0228.JPG)


#### Hardware
- Murgen 1.0
- Hackaday Trinket Pro
- 5/3.3V alim
- Bitscope micro (BS05)
- A haribo box
- A servo
- A transducer

#### Remarks 
- Same setup as [Session 4](Session_4.md), and same remarks apply.
- The servo is added
- We are not tapping into the full HighVoltage potential of the board, **we could still get a clearer image**.

#### Give me files

- The code lies at ```bitscope/acquire_image.py``` to acquire a full image
- Repeated measurements for a line are at ```bitscope/bitscope_data/single_line/*.log```
- The data for images is at ```bitscope/bitscope_data/full_image/*.log```
- Creating images from the logs is at ```bitscope/bitscope_data/full_image/CreateImage.py```
- Bulking image creations is at ```bitscope/bitscope_data/full_image/BatchImage```

#### Give me an image

![BitScopeFullImage](/bitscope/full_image/20160320-020140-Signal-bitscope-DATA.log-SC.png)

### Discussion and issues

#### Discussion
- The Acquire_Image.py script is listening on both the Pin11 of the trinket (to get the "Position Pulse" and hence determine where the line is) but also from the TestPoints 2/3 on the murgen board. Therefore, the BitScope needs to listen on both Analog channels, and it imposes that the framerate is divided to 5MHz.
- Getting the first logs using BitScope Python API
- Getting the first raw image
- Getting the first SC:
--length of each image is custom, as the header containing the position changes
--ScanConversion is heavy, so we are proposing a decimation
#### Issues
- BitScope only trigs on "wide" pulses, so we had to add a 10us pulse from the Arduino so to trig on this signal, not on errors from the Arduino pulser. We got Pin11 do this, still playing with PORTB.
- Python is slow... so if we look at the full image logs, we see that the image takes 2.5s roughly to get 60 lines. Thanks to Python. We are missing a couple of the lines. Thanksfully, we know were each line was shot!

#### Next steps
- Using the SPI on the TGC, controlled via the Trinket
- How to work only on 1 channel, so that we can get 20Msps with the BitScope instead of the 5Msps ?
- Use a better ScanConversion
- Having TP5/6 work =)

## Images
#### Getting an image (Decimation of 2, cutting the lower half)
![RawImage](/bitscope/full_image/20160320-020140-Signal-bitscope-DATA.med.png)
#### ScanConverting it
![ScanConverting](/bitscope/full_image/20160320-020140-Signal-bitscope-DATA.med-SC.png)






