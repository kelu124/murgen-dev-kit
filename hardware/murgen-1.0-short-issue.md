Murgen 1.0 short circuit
===

25/02/2016: we received the boards, all seems good.

However, we realised there was a short circuit between 5V and GND, and not between 3.3V and GND (thanksfully !) 

TL;DR:
* There was a short
* We found that the RECOM was inverted -- to be amended for the 1.1
* Identified a possible short...
* Let's see !



## Transcript of the chat

>[2/26/2016 12:15:58 AM] Sofian: Of course it will be the mistake of the designer :smile: I have made a mistake with the Power supply module footprint, I have created it flipped, because I should have paid better attention to the datasheet
>
>[2/26/2016 12:17:53 AM] Sofian: The numbers of the pins show the bottom view and not top view, I have created it as a top view, this can still be solved by removing the power supply module and installing it from the bottom side, I am very sorry for this mistake, but I am not entirely sure it would create the short though, unless you have provided 5 volts to it.
>
>[2/26/2016 12:26:35 AM] Sofian: This is one possible location where a solder joint might happen between GND and 5V

![Possible short](/worklog/Images/PossibleShort.png)

>
>[2/26/2016 12:43:19 AM] Sofian: GND points
 
![GND Points 1](/worklog/Images/GND1.png)
![GND Points 2](/worklog/Images/GND2.png)
 
>[2/26/2016 12:45:39 AM] Sofian: VDD_5V
 
![5V Points 1](/worklog/Images/5V1.png)
![5V Points 2](/worklog/Images/5V2.png)
 
>[2/26/2016 1:14:33 AM] Sofian: This excel file contains the settings for the switch settings, it allows you to set various frequencies for sampling from 1MHz to 12MHz, which is not supported, so you can go upto around 9MHz with the selection I have given you.
>
>[2/26/2016 1:23:22 AM] Sofian: As for setting the voltage: First measure resistance between GND and Pin8 on the DC/DC module, adjust the pot until this value is zero Ohm
>
>[2/26/2016 1:23:46 AM] Sofian: Also make sure the value between pin 8 and pin 9 on the DC/DC module is around 5kOhm
>
>[2/26/2016 1:25:06 AM] Sofian: Please make sure of this many times, refer to the datasheet of the DC/DC module to make sure the pins you are checking are correct
and don't forget to flip the DC/DC module to the bottom side

>[2/26/2016 1:26:07 AM] Sofian: I hope you have not powered it, I also recommend that once you remove the DC/DC module you check the short again to make sure it went away or not, maybe the source is not the DC/DC module
>
>[2/26/2016 1:28:19 AM] Sofian: TP9 is GND pin by the way
>
>[2/26/2016 1:49:27 AM] Sofian: I also checked all other foorprints and pinouts to make sure I have no other mistakes, I could not find any

## Action

**Flipping the RECOM !**


## Resources

 * [murgen](https://github.com/kelu124/murgen-dev-kit) for the original board

