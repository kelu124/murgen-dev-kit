# Session 1 - 06 March 2016

## Other sessions

- [Session 1](/worklog/Session_1.md) : Powering the board, power use, first (bad) trigging and echoes (06 March 2016)
- [Session 2](/worklog/Session_2.md) : Non-controlled pulsing, inverters, better echoes (11 March 2016)
- [Session 3](/worklog/Session_3.md) : Getting controlled pulsing, but width not controlled (15 March 2016)
- [Session 4](/worklog/Session_4.md) : Width of the pulses is getting controlled =) (19 March 2016)
- [Session 4b](/worklog/Session_4b.md) : Simple data visualisation with BitScope (19 March 2016)
- [Session 5](/worklog/Session_5.md) : moving the transducer to get the first image (20 March 2016)
- [Session 6](/worklog/Session_6.md) : ***Getting a clinically usable image*** (28 March 2016)
- [Session 7](/worklog/Session_7.md) : Getting cleaner images - code improvements  (3 April 2016)
- [Session 8](/worklog/Session_8.md) : Comparing acquisition speeds (3 May 2016)

## ^^
_ Happy to get the board and play with it._

## TL;DR

* Setup of if 5V on stabilized. Power use within the 2.5W so far.
* Pulser behavior to dig
* Some echoes appear 

# Some pics with the BeagleBone black

![DSC_0152](/Images/Session_1/DSC_0152.JPG)

![DSC_0153](/Images/Session_1/DSC_0153.JPG)

![DSC_0154](/Images/Session_1/DSC_0154.JPG)

# Technical points

## Power uses

### Setup

To play it safe, we had the voltage control, P1, at 2.3 kOhm, so to get at ~50/60V output, to avoid being above the 100V limit from the pulser.

### Sources
If used on a standard alim as we had, voltages get too low:

* 3.75V instead of 5V
* 2.88V instead of 3.3V

The buffer led gives light, that's because the ref voltage is too low.

### Power
Once the 5V on a stabilized source, we read that it consumes ~135mA without a pulse, or 143mA with a 500ns, 50V pulse every 300us.

## Pulser: the HV7360

### Setup
HV7360 is fed by HVOUT - and HV7360 is controled by 

- US_Pulse_P on InA
- US_Pulse_N on InB

Discussing with Sofian, I had connected USPN on GND, USPP on a 3.1V, 250ns pulse, at 300us macroperiod. That should take care of the pulse for the transducer.

### Discussion and issues
Observations

- Connecting USP-N on GND does not control the pulse width. 
- Connecting USP-N and USP-P on a 2V-pulse seems to control (at least make thinner) the pulse. 
- With the transducer on / off, it seems there is still a voltage baseline (500mV)

- It seems that pulsing on USP-N shuts the pulser off.
- We need to control the pulser to send a clean pulse. We already have some echoes, but their birth is dirty.

### In practice

### USPN on ground. Blue is the trigger, Yellow is the pulse. 3.1V. 50/60V easily, but does not decrease with time.

#### Without piezo

![TEK_00](/worklog/Images/Session_1/TEK0000.JPG)

![TEK_01](/worklog/Images/Session_1/TEK0001.JPG)

#### With a piezo

![TEK_11](/worklog/Images/Session_1/TEK0011.JPG)

#### Some echoes

![TEK_06](/worklog/Images/Session_1/TEK0006.JPG)

#### Averaged

![TEK_05](/worklog/Images/Session_1/TEK0005.JPG)

#### Detailed

![TEK_04](/worklog/Images/Session_1/TEK0004.JPG)

### Decreasing pulse to 2V, and connecting USPP and USPN to the pulse.

#### Without the piezo

![TEK_02](/worklog/Images/Session_1/TEK0002.JPG)

#### With the piezo

![TEK_03](/worklog/Images/Session_1/TEK0003.JPG)

### Pulse to 3.1V, and connecting USPP and USPN to the pulse.

#### Without the piezo

![TEK_10](/worklog/Images/Session_1/TEK0010.JPG)

#### With the piezo

![TEK_09](/worklog/Images/Session_1/TEK0009.JPG)
