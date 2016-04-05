# Session 2 - 11 March 2016

## Other sessions

- [Session 1](/worklog/Session_1.md) : Powering the board, power use, first (bad) trigging and echoes (06 March 2016)
- [Session 2](/worklog/Session_2.md) : Non-controlled pulsing, inverters, better echoes (11 March 2016)
- [Session 3](/worklog/Session_3.md) : Getting controlled pulsing, but width not controlled (15 March 2016)
- [Session 4](/worklog/Session_4.md) : Width of the pulses is getting controlled =) (19 March 2016)
- [Session 4b](/worklog/Session_4b.md) : Simple data visualisation with BitScope (19 March 2016)
- [Session 5](/worklog/Session_5.md) : moving the transducer to get the first image (20 March 2016)
- [Session 6](/worklog/Session_6.md) : ***Getting a clinically usable image*** (28 March 2016)
- [Session 7](/worklog/Session_7.md) : Getting cleaner images - code improvements  (3 April 2016)

## Today 

### ^^
_ Getting nice pulses._

### TL;DR
- OK with the breadboard alim - need to power it with 9V
- Pulser behavior still buggy - there's a lower cap to the pulser
- We have nice echoes of Vcc ~1V with Vin of 50V

## Technical points

### Power uses

In the previous Session, we realized that the 5V and 3.3V were lower than expected... of course, we had 5V in, with 9V we get a proper alim.

### Pulser: the HV7360

Same setup as [Session 1](/worklog/Session_1.md).

Only difference is the introduction of the CD74HC4049E inverter, with a 5V, 6ns delay, to get the pulse. US_P_P is completed with US_P_N which is the inverse of USPP.

We set the pulse width to the minimum to avoid a pulse out of control. Out of 300us period, that's a 3% duty cycle. Maybe that's the GBF, even if the oscillo says no?

### Discussion and issues

#### Discussion

- At 50V, we observed interesting echoes from the 4MHz transducer. An echo at 82us means that there was an obstacle at (1540*82e-6)/2, that's 63mm away from the transducer... where we put a reflector! Success.
- Echoes before and after the MD0100 are basically the very same. No attenuation.
With the jumper on on J1 (TGC), on the high amplification, we do see the signals on P2/P3. But nothing after, on P5/P6. That would translate in a signal on P7.
- Just behind the MD0100, there's a +-10V swing, which is completely attenuated by the CL component just behind it, to avoid to fry the TGC.

#### ISSUES
- The pulser is still an issue.
- Inverter is quick enough for our needs

## Images

#### Echoes after MD0100 vs the pulse
![TEK_04](/worklog/Images/Session_2/TEK0004.JPG)

#### Comparison of echoes before and after the MD0100
![TEK_05](/worklog/Images/Session_2/TEK0005.JPG)


### Inverter
![TEK_01](/worklog/Images/Session_2/TEK0001.JPG)

### Pulse control
#### Pulse with too thin a command pulse
![TEK_00](/worklog/Images/Session_2/TEK0000.JPG)

#### Pulse with a good.. but long command pulse
![TEK_02](/worklog/Images/Session_2/TEK0002.JPG)

#### Pulse with a borderline pulse.. the cap
![TEK_03](/worklog/Images/Session_2/TEK0003.JPG)

