---
layout: post
title: Tutorial on using Murgen, part I
---

First thing you could be interested in, is to get the schematics of the board, accessible at : https://github.com/kelu124/murgen-dev-kit/blob/master/hardware/Altium/Schematics/PDF/echOpen_ADC_Card_1.0.pdf . This maps at what pins / test points are connected where. Now, if you look at the expansion headers, on page 3 (get well once printed on A3, and easier to read one).

Before anything, you can then plug your transducer on the SMA plug.

The first step is to power on the board, you can use something [like this](https://github.com/kelu124/murgen-dev-kit/raw/master/worklog/Images/Session_4/TEK0000.JPG) to get the 3.3V and 5V that the board requires. But that could be any power source that has clean 3.3V and 5V. You can then plug the ground on the DGND pin of the board (one is enough), and 5V and 3.3V respectively to VDD_5V and VDD_3V3B. Once this is done, the power is here, and, be careful, high voltage as well. You can test it at TP10, using DGND or TP9 as ground. You should have a voltage at around 50V (usually enough for the tests, that's what I've used for my own images). This voltage can be set using the P1 potentiometer.

Once this obtained, the controls for the pulses are as follows: USPulseP (for +, activates) links to GPIO0_7 and CLKOUT2, which you can find on the expansion header 2 (which is the only one we use, this header being the only one we'll use at first). This is the one close to the recom (black block on the bottom of the board), but I assume you can also link to the BeagleBone Black headers as described in its specs (a print out of this image is [also useful](http://beagleboard.org/static/images/cape-headers.png)).  A pic of this setup is on [Session 3 page](https://github.com/kelu124/murgen-dev-kit/blob/master/worklog/Session_3.md). On this picture, I wasn't using a Arduino for the USPulseP and USPulseN to control the pulser, rather a signal generator.

A word about the controls. You need the USPulseP to say "Pulser HV  ON, please" and, after a period of time you may want to adjust with respect to your transducer, you'll need USPulseN to shut down the pulse. These two signals should be 3.3V sequential pulses, as shown [on this image](https://github.com/kelu124/murgen-dev-kit/raw/master/worklog/Images/Session_4/TEK0000.JPG). The results of this pulse are shown here [on this image](https://github.com/kelu124/murgen-dev-kit/raw/master/worklog/Images/Session_4/TEK0002.JPG). With the transducer plugged in, you'll have [echoes](https://github.com/kelu124/murgen-dev-kit/raw/master/worklog/Images/Session_4/TEK0013.JPG) measured on testpoint 1 (the closest to the SMA). [All is on this log](https://github.com/kelu124/murgen-dev-kit/blob/master/worklog/Session_4.md). (you can skip the first logs, I was trying out things, but the core is on Session 3 and 4).

That should be a good day of work, but I'll remain at your disposal!

Don't hesitate to fork the https://github.com/kelu124/murgen-dev-kit/ account if you play with git, but in any case don't hesitate as well to ping me, and I'll follow up with your experiment with murgen!
