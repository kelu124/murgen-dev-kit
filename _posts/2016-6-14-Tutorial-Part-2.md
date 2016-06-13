---
layout: post
title: Tutorial on using Murgen, part II
---

## 2016-06-08 Zach's ideas

Finally got some echoes! Your most recent email led me to your trinket code... And I realized my issue was that I was waiting 300 milliseconds between pulses rather than 300 microseconds...
The transducer were using is 5 MHz, with a focal length of 5 centimeters approximately.

One thing though... I tried to adjust the board voltage by turning P1... But no matter how many rotations I did, the voltage never changed more than a volt or two...

Lastly- I would be happy to blog my progress on GitHub! I will start working on that tomorrow.

## 2016-06-13 Luc

Saw your echo, great! Now, to move forward..

Jumper 1 is used to select the level of gain of the signal at the amplification level. Try to see the echo using TP2 and TP3 (not GND, but use both probes to measure between these two points), using the jumper in the two positions. One should give a greater echo - use this one at first.

Then, using TP4, you can input 0 to 1V (beware, not much more!!) into the GAIN entry of the TGC (AD8331). Consider using a safe, stable source of voltage. At 0.5V, you should already have quite a boost at the signal level.

Once you have a good echo, have the same measure between TP5 and 6, and get the measurement. Then do the same between TP7 and GND.

If everything goes fine, between TP8 and GND, you should see the enveloppe of the very same signal.

## 2016-06-14 Feedback

Tried both of Jumper 1's positions as you suggested, and found that the original one was optimal.  I'm inputting a 0.5V voltage to TP4, and it seems to be reducing the noise which is good!  The signal itself didn't start to amplify until around 1V though, and I didn't want to break anything so I didn't exceed that 1V limit.

I didn't quite understand your last email: what should I measure at TP5 and 6? and TP7 and GND? and TP8 and GND?  I was confused as to what you meant.

I've uploaded a log of the day's work so far to GitHub.  The original file I created was too large to upload, so I uploaded a .zip instead that you can download and view.
I am getting a clear echo now

## 2016-06-14 Luc's back

Thanks for sharing the info. Don't hesitate to push on github the files the way I did for this ( https://github.com/ZTaylor39/murgen-dev-kit/blob/1f39a41f9740ee0d9ecdd18fb980ea4526b801bb/worklog/Zach/20160607-zach.md ) log. A markdown file is easy to read, and Github allows a neat render of the file (without mentioning an easy access to the pictures).

That being said, I'm curious to know what you used to introduce the 0.5V into TP4: a stabilized power supply? Do you know how many mA it fees into TP4? Insufficient current may limit the boost effect of the TP4. By the way, is that still the measure between TP2 and TP3 (meaning one croc is on TP2 and the other on TP3, not using the GND for this measurement)?

Indeed, the next step is to measure and compare with same scale (V and time) the look of this first echo. Beforehands, it should look like : https://github.com/ZTaylor39/murgen-dev-kit/blob/1f39a41f9740ee0d9ecdd18fb980ea4526b801bb/worklog/Images/Session_6/TEK0002.JPG or shorter in duration. It is essential to use at best the screen of your oscillo, it may reveal details about your signal of interest.

Once your echo on TP1 taking as much of the screen as possible, shift the measurement to between (TP2 and TP3), then (TP5 and TP6) and finally between (TP7 and GND) (here the probe is back on GND for GND and the croc on TP7), then between (TP8 and GND).
The zoom may be blurry, but if you look at https://raw.githubusercontent.com/ZTaylor39/murgen-dev-kit/61cf772e4a7915d606a14c878e415dbfab5014b2/worklog/Images/Session_5/DSC_0226.JPG , you'll see that none of the clips of the bitscope are attached to GND. One is attached to TP2 and the other on TP3.

This stage is summarized at https://github.com/ZTaylor39/murgen-dev-kit/blob/1f39a41f9740ee0d9ecdd18fb980ea4526b801bb/worklog/Session_6.md  - and you should obtain something similar. Have a check at the voltage you're using... and if the power supply delivers enough current to the TP4. At TP4: 480mV, I had 41mA going in.
