---
layout: post
title: Tutorial on using Murgen, part III
---

## Somes MD notes

(original [was there](https://github.com/ZTaylor39/murgen-dev-kit/commit/9a707c84962db230d2ac2d488242ef0409cef663))

Over the past week I've been working to get my first image using the Murgen board and arduinos.  
Currently, the Murgen board is powered by and pulsed by an Arduino.  The Servo motor for the transducer is controlled by another arduino.
I gathered the data at TP2 using BitScope, and collected it in MATLAB.  The goal was to get an image from the Murgen board, by whatever means necessary.
I collected the data in MATLAB, but since I'll likely be using Python in the future I reconstructed the image in Python.
Since I did a radial scan with the Servo motor, I had to convert my data from polar to rectangular.
After that, the image was still noise, but I made the image greyscale with a logarithmic scale and I got a very nice image!

##### What I now know:

- I know how to reconstruct 2D images from the Murgen board.
- Python works for image reconstruction.

##### Next Steps:

- Image enhancement; what I've got now is good, but there is still work to be done.
- Control Murgen board from Python.
- Gathering data and reconstructing the image at once: preferably in Python but maybe in MATLAB.
- Real-time imaging.
- Gather data from Murgen board via BeagleBone.
- Power, pulse, and gather data from Murgen board via BeagleBone.

![Alt text](https://github.com/ZTaylor39/murgen-dev-kit/worklog/Zach/Images/IMG_1180.JPG?raw=true "Transducer Setup")

![Alt text](https://github.com/ZTaylor39/murgen-dev-kit/worklog/Zach/Images/FirstImage.png?raw=true "First Image")

## 2016-06-21 Some image processing !

I just logged my progress from the past couple days for you to see.  I've been working on the image reconstruction side of my project for a while, and I think I'm in a good spot for that: got my first image!  If you have any thoughts or input, please email me back and let me know!
A couple questions: how did you get the Murgen board to ride on the BeagleBone and have the BeagleBone pulse it?  I'd like to use the BeagleBone for image processing, but struggling to get it to communicate with the Murgen board.
I've got a list of my next steps in the latest file I logged on GitHub.  If you've got any advice, I'd love to hear it!

## 2016-06-21 Some questions

I'm reading you've used bitscope to get the data from TP2 .. does that mean between TP2 and TP3 ? Were you using a gain into TP4?
To use the BBB, you'll need to go downstream on the electronic processing.
I'd suggest the following:
- trying to get a good echo on your fantom (I'd put the interface on its focal zone, to get the best image possible, the same way you can't read a book too close of your eyes)
- Measuring this echoe between TP2 and TP3, screenshoting it (I got one nice this saturday : https://github.com/kelu124/echomods/blob/master/retro10PV/images/DSC_0681.JPG )
- Without touching anything, measuring between TP5 and TP6, screenshotting
- If everything goes fine, doing the same for TP7 and TP8. For TP8 you should get the enveloppe of your signal, which is what you need to get the image.

Afterwards, this signal is sent to the ADC, the analog to digital convertor, which processes the analog signal into a digital one that can be read by the BBB. It is therefore really important to get a clean signal at this stage. I know the bitscope can add some noise, but don't worry, you'll be able to get rid of it soon. Indeed, once we know you have a good signal at TP8, that means you are ready to start on BBB.

## 2016-06-22 Moving forward

Thanks for posting the info / code you did!
Quick questions though :
- Can you publish the data itself (first_acq_murgen.mat ? ) ?
- Moreover, are you really at 100e6 (100MHz) at acquisition? It would rather be 10MHz with the bitscope?
- Last but not least: I trust you are plotting the "raw data" without getting its enveloppe before. This is a necessary step (see http://starfishmedical.com/2015/02/19/pros-cons-two-popular-ultrasound-signal-processing-techniques/ ) - which I usually do with a Hilbert transform or filtering directly the signal in the Fourrier space, but you could do so also by squaring the signal and getting it through a low pass filter.

Hope you'll have fun with this signal processing!

BTW, did you get the chance to get signals from the other TPs?
