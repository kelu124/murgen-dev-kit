# Session 1 - 06 March 2016
## ^^
_ Happy to get the board and play with it._
## TL;DR
* Setup of if 5V on stabilized. Power use within the 2.5W so far.
* Pulser behavior to dig
* Some echoes appear 

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
HV7360 is fed by HVOUT 
* HV7360 is controled by 
** US_Pulse_P on InA
** US_Pulse_N on InB
Discussing with Sofian, I had connected USPN on GND, USPP on a 3.1V, 250ns pulse, at 300us macroperiod. That should take care of the pulse for the transducer.

### In practice

### USPN on ground. Blue is the trigger, Yellow is the pulse. 3.1V. 50/60V easily, but does not decrease with time.

![TEK_00](https://github.com/kelu124/murgen-dev-kit/tree/master/ImagesSession_1/TEK0000.jpg)

![TEK_01](https://github.com/kelu124/murgen-dev-kit/tree/master/ImagesSession_1/TEK0001.jpg)

#### Some echoes
![TEK_06](https://github.com/kelu124/murgen-dev-kit/tree/master/ImagesSession_1/TEK0006.jpg)
#### Averaged
![TEK_06](https://github.com/kelu124/murgen-dev-kit/tree/master/ImagesSession_1/TEK0006.jpg)
#### Detailed
![TEK_04](https://github.com/kelu124/murgen-dev-kit/tree/master/ImagesSession_1/TEK0004.jpg)
### Decreasing pulse to 2V, and connecting USPP and USPN to the pulse.
#### Without the piezo
![TEK_02](https://github.com/kelu124/murgen-dev-kit/tree/master/ImagesSession_1/TEK0002.jpg)
#### With the piezo
![TEK_03](https://github.com/kelu124/murgen-dev-kit/tree/master/ImagesSession_1/TEK0003.jpg)

### Pulse to 3.1V, and connecting USPP and USPN to the pulse.
#### Without the piezo
![TEK_10](https://github.com/kelu124/murgen-dev-kit/tree/master/ImagesSession_1/TEK0010.jpg)
#### With the piezo
![TEK_09](https://github.com/kelu124/murgen-dev-kit/tree/master/ImagesSession_1/TEK0009.jpg)
