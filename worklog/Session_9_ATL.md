# Session 9 - 3rd July 2016 - Playing with ATL10PV 

## Previous sessions

- [Session 1](/worklog/Session_1.md) : Powering the board, power use, first (bad) trigging and echoes (06 March 2016)
- [Session 2](/worklog/Session_2.md) : Non-controlled pulsing, inverters, better echoes (11 March 2016)
- [Session 3](/worklog/Session_3.md) : Getting controlled pulsing, but width not controlled (15 March 2016)
- [Session 4](/worklog/Session_4.md) : Width of the pulses is getting controlled =) (19 March 2016)
- [Session 4b](/worklog/Session_4b.md) : Simple data visualisation with BitScope (19 March 2016)
- [Session 5](/worklog/Session_5.md) : moving the transducer to get the first image (20 March 2016)
- [Session 6](/worklog/Session_6.md) : ***Getting a clinically usable image*** (28 March 2016)
- [Session 7](/worklog/Session_7.md) : Getting cleaner images - code improvements  (3 April 2016)
- [Session 8](/worklog/Session_8.md) : Comparing acquisition speeds (3 May 2016)
- [Session 9](/worklog/Session_9.md) : Playing with ATL10PV (3 July 2016)

# Aim of today

## Is the ATL 10PV working?

### Test of the piezos with echOpen's analog processing chain

Overall echo at 20cm

![Details of the echo](/worklog/Images/Session_9/DSC_0680.JPG)

Zooming in

![Details of the echo](/worklog/Images/Session_9/DSC_0681.JPG)

Zooming in

![Details of the echo](/worklog/Images/Session_9/DSC_0678.JPG)

Details of the echo

![Details of the echo](/worklog/Images/Session_9/DSC_0679.JPG)

### Preparing the probe

Some linseed oil was used as a impedance matching material. Works great.. but be sure to overfill the reservoir, since too low oil will result in an oil/air emulsion.. really not usefull to work with.

### Setup

Murgen was plugged to the 10PV, its lower piezo aiming downwards (in the axis of the probe). There were some echoes:

![5Msps](/worklog/Images/Session_9/9a/20160703-105257-raw.png)

![5Msps](/worklog/Images/Session_9/9a/20160703-111651-raw.png)

These images are lines shot in continuous mode while murgen is aiming at the bottom of a glass.

## Is it working when rotating?

### Getting data

Having 12V put into the motor, and sorting the matrix of acquisition (1000samples, 5Msps, 1000 pts / lines), shooting at 250us intervals) with a little magic, we see three behaviors. That would fit with 3 piezos. Raw data,bzipped, are available at [the archive page](/worklog/Images/Session_9/9b/).

![Sorted](/worklog/Images/Session_9/9b/20160703-132948-threepiezos.log.png)

If cleaning the behavior these 3 behavior, the data becomes

![Cleaned](/worklog/Images/Session_9/9b/20160703-132948-Signal-bitscope-DATA.log.png)

### Conclusions

We see echoes on the oscillo, before the enveloppe detection... that's where the signal is. So:

* Murgen is equipped with a enveloppe detection at 3.5MHz, so it's quite normal that it doesn't see the 5, 7.5 and 10MHz.
* The pulser works
* We see clearly 3 behaviors... how come? Since the piezo should be all 
* Maybe 12V continuous is too rapid for the motor: I can't see to know where the signal is at what moment. Should be using the second channel of the bitscope to get a saw signal, hence knowing when the lines are shot.


## Arty - drawing with ultrasounds

Done with the smart-materials 3.5MHz piezos  ad imaging a grape passing in front of a piezo

Light one

![Light](/worklog/Images/Session_9/9c/20160703-171434-light-DATA.log.png)

Heavy one

![Heavy](/worklog/Images/Session_9/9c/20160703-172709-heavy-DATA.log.png)






