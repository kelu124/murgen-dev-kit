Some work with my
AA813B03480B306D773BFD007800AA5F3D83C176E822C5096CA57632284D8D0E friend
;)

Work
----

### TODO

-   Validate board
-   Do PRU code
-   Do "datadump" code
-   Do Node.js
    -   Explore WebRTC
-   USB connection

### Pending

-   Transducer sourcing

### Done

-   Assembling a small team (24/11/15 -&gt; onwoards)
-   Pre BOM (30/11/15)
-   Prefeasibility study (4/12/15)
-   Finding PCB/PCBA suppliers (7/12/15)
-   BOM
-   Add to the list ADS803E or LTC2315-12
-   A PCB feasibility (Manu, S, A)
-   A PCB pre-design

### Cancelled

-   [Design thinking
    classes](https://www.coursera.org/learn/design-thinking-innovation/home/welcome)

### Thoughts

-   See below \^\^

Culture
-------

-   [Read Meaningful Making
    (PDF eBook)](http://fablearn.stanford.edu/fellows/sites/default/files/Blikstein_Martinez_Pang-Meaningful_Making_book.pdf)
-   [Here from Alessia
    Cara](https://www.youtube.com/watch?v=eyoSkZ-KODE)

Dimensioning the data
---------------------

+---------------------------+---------------------------+-----------------------+
| bgcolor="green"           | bgcolor="green"           | 1.  A pulse is sent   |
| width="30%" align =       | width="40%" align =       |     to the transducer |
| "center" valign="center"  | "center" valign="center"  |     (1st image)       |
| style="border: none;"|    | style="border: none;"| ![ | 2.  The transducer    |
|                           | 360px | center            |     listens to the    |
| -   **128** lines/image   | ](BBB6Signals.jpg  "fig:  |     echos, trains or  |
|     may be enough at      | 360px | center ")         |     packets of a      |
|     first - at **16       |                           |     couple of periods |
|     imgs/s** thats 2048   |                           |     at 3.5MHz . These |
|     lines/s               |                           |     trains are 4+     |
|     -   That's 488us per  |                           |     periods wide, and |
|         line              |                           |     are more          |
| -   (**15.77** cm x 2) /  |                           |     attenuated the    |
|     (154000 cm/s) =       |                           |     deeper they come  |
|     204.805 us - that's   |                           |     from (image 2)    |
|     **1024 pts at 5MHz**  |                           | 3.  The signal goes   |
|     -   That's 204.805 us |                           |     to a VGA to       |
|         per line          |                           |     rectify           |
|     -   That's 283.5 us   |                           |     attenuation (TGC) |
|         of idle time      |                           |     - output, the     |
| -   Final image is        |                           |     same frequencies, |
|     therefore             |                           |     amplitudes        |
|     **128\*1024** px      |                           |     corrected         |
|     -   **1024** pts for  |                           |     (image 3)         |
|         15.77cm is 6.49px |                           | 4.  This goes through |
|         / mm              |                           |     a low-pass -- to  |
|     -   That's            |                           |     remove all        |
|         **2.1Msps** on    |                           |     frequencies above |
|         average           |                           |     the 1.5 - 5 MHz   |
|                           |                           |     band of interest. |
|                           |                           | 5.  This goes through |
|                           |                           |     the enveloppe     |
|                           |                           |     detection         |
|                           |                           |     (image 4)         |
|                           |                           | 6.  This goes to the  |
|                           |                           |     ADC               |
|                           |                           | 7.  This is output to |
|                           |                           |     the buffer        |
|                           |                           |     (if needed)       |
+---------------------------+---------------------------+-----------------------+

This LOG
--------

### Nov 24th 2015

-   TLDR
    -   CapTech Workshop. Was great!
    -   Acted upon a split between a FPGA long-term approach, and a
        non-FPGA one. I remembered those good old times when this was
        a possibility.
    -   Damn it. What if I could dig into this? Not µC, rather an
        extension for an existing computer.. or mini computer.
    -   Saw some ideas on the Arduino's side. Separate ADC.
-   Resources
    -   [Is Pi powerful enough for an oscilloscope
        project?](http://raspberrypi.stackexchange.com/questions/4129/is-pi-powerful-enough-for-an-oscilloscope-project)
    -   [Raspberry Pi as an Oscilloscope @ 10
        MSPS](https://digibird1.wordpress.com/raspberry-pi-as-an-oscilloscope-10-msps/)

### Nov 27th 2015

-   <http://paul.sullivan.za.org/raspberry-pi-oscilloscope/EE-October-1991/>
    (pics below)
-   MagPi : ISSUE 24 - JUN 2014 (to print !!)
-   Follow up
    -   Discussion with
        4365D2F5E4EB59B6BAD0FC746506A6EADEC28BC264BDD78BC041D3417B0766F4
    -   Discussion with
        8620B4ADDED83F8C1E5EBC0F401D12BC327735D7A314336D24C3F3D88A16E3ED

### Nov 28th

-   Tamagotchi hive in a probe?
-   Thinking about the smile on the silkscreen. EO+OH+PI+Pirate?

### Dec 1st

+--------------------------------------+--------------------------------------+
| -   Thinking of deadlines            | ![](echOpen shield v2.jpg "echOpen s |
| -   PHH/BM discussions               | hield v2.jpg"){width="500"}          |
|     -   Rather be going onto SPI :   |                                      |
|         QuadSPI ?                    |                                      |
|     -   LTC5507ES6 to filter ? A     |                                      |
|         rajouter!                    |                                      |
|     -   Better ADC at LTC2315-12     |                                      |
|     -   DAC: a simple DAC i2c        |                                      |
| -   echOpen discussion               |                                      |
|     -   Pro/Cons of a shield         |                                      |
|         compared to                  |                                      |
|         FPGA/microcontrolleur        |                                      |
| -   Discussing over the architecture |                                      |
|     at [ this page, comments on the  |                                      |
|     pic                              |                                      |
|     below](:File:EchOpen_shield_v2.j |                                      |
| pg "wikilink")                       |                                      |
| -   Idea:                            |                                      |
+--------------------------------------+--------------------------------------+

### Dec 2nd

-   Rasberry Pirn
    -   Raspberry Pi Zero Headless Setup :
        <http://davidmaitland.me/2015/12/raspberry-pi-zero-headless-setup/>
    -   Installing Operating System Images on Linux
        <https://www.raspberrypi.org/documentation/installation/installing-images/linux.md>
-   BBB
    -   How to use it?
        -   <http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/05/22/bbb--working-with-the-pru-icssprussv2>
        -   For low-speed comms, conventional I2C or similar protocols
            can be used, and there is no need to use a PRU. For
            high-speed comms the PRU may be extremely useful because it
            can service the hardware with no interruptions due to Linux
            context switching, and no overhead is experienced by the
            main ARM processor. Here are some examples that should be
            feasible; basically quite a few possibilities, such as
            **interfacing to a fast ADC (e.g. analog capture)**,
    -   <https://theembeddedkitchen.net/beaglelogic-building-a-logic-analyzer-with-the-prus-part-1/449>
        BBB is a 100MHz logic analyzer on a BeagleBoneBlack
    -   Demo over the <http://beaglelogic.github.io/webapp/>
    -   <http://r.git.net/beagleboard/2013-10/msg00204.html>
        -   Can the PRU be used to interface the Beaglebone to external
            ADC? I need to capture 500 micro-seconds of data at a 5
            MHz rate.
        -   -&gt; *It depends on the interface to the ADC. There is a
            parallel capture interface that will easily run that fast,
            and you may be able to use the bit-shift interface to do
            serial or something like SPI if the PRU's capability lines
            up with what your ADC wants to see.*
    -   <http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/08/04/bbb--high-speed-data-acquisition-and-web-based-ui>
        -   *In its current state, it grabs analog data from an ADC, and
            dumps it into memory on the BBB, ready to be displayed or
            further processed. It could be used for gathering analog
            information from sensors, CCDs or other data
            acquisition use-cases. To be reasonably useful, the desire
            was for it to support 20Mbytes/sec of data or more. It does
            achieve this, but it is for further study to find higher
            speed methods.*
        -   *This is not such a bad idea, because in future the ADC
            could be swapped out to a (say) 10-bit ADC with no code
            change on the PRU.*
        -   **Once the data has been captured (2000 samples in this
            example), the command byte is acknowledged, so that the
            Linux hosted application can know that the PRU
            has completed. The PRU now sits and waits for a new
            instruction from the Linux hosted application.** -&gt; works
            for us - fixed depth = fixed \# of samples
    -   Buffer to be used : detailed at
        <http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/08/04/bbb--high-speed-data-acquisition-and-web-based-ui>
        -   ''These were extremely important for two reasons. One reason
            is that the pins to the BBB that I wished to use need to be
            isolated during power-up, because they are used for
            selecting the boot method. If there was any unusual level on
            the pins upon power-up then the BBB will not boot from
            the eMMC. So, a tri-state buffer is needed. The other reason
            is that there is a fair bit of capacitance and it is highly
            likely that the ADC may not be able to directly drive the
            pins at high speed. I actually came across this problem
            while trying to connect a camera to the BBB. I struggled for
            days without realising that the camera could not support
            the load. So, the buffers are likely to be essential for
            most designs using the pins that were selected. I used a
            74LVC244A device as a buffer. Note that the clock also needs
            a buffer, unless significant jitter is acceptable. No
            tri-state is required here, so I used a MC74VHC1GT50.

''

### Dec 3rd

+---------------------------------------------+------------------------------+
| -   New ADCs in mind                        | ![](turnerforago.png "turner |
|     -   ADS803E                             | forago.png"){width="500"}    |
|     -   LTC2315-12                          |                              |
| -   [Orange Pi Plus 2 : A nasty little      | -   <http://stackoverflow.co |
|     thing](http://www.orangepi.org/orangepi | m/questions/tagged/beaglebon |
| plus2/)                                     | eblack?newreg=6e30d12d1ba64b |
| -   BBB [as always coming mostly from       | 65ac46b7deee1f9fd5#>         |
|     element14](http://www.element14.com/com | -   <http://electronics.stac |
| munity/community/designcenter/single-board- | kexchange.com/questions/tagg |
| computers/next-gen_beaglebone//blog/2013/08 | ed/beaglebone-black?page=1&s |
| /04/bbb--high-speed-data-acquisition-and-we | ort=newest&pagesize=15>      |
| b-based-ui)                                 |                              |
|     -   Some limits - not exploiting all ?  |                              |
|         <http://exploringbeaglebone.com/cha |                              |
| pter13/#The_ADS7883_Single-Channel_12-bit_A |                              |
| DC_1MSps_max>                               |                              |
|     -   SPI speed with BBB :                |                              |
|         <http://fr.mathworks.com/help/suppo |                              |
| rtpkg/beagleboneio/ug/use-the-beaglebone-bl |                              |
| ack-spi-interface-to-connect-to-a-device.ht |                              |
| ml>                                         |                              |
|         (up to 32MHz) - which is            |                              |
| -   16 bits : *is it possible to set all 16 |                              |
|     pins on pru0 as inputs? I saw you       |                              |
|     mentioned something about disabling the |                              |
|     microSD functionality on the BB to get  |                              |
|     access to all 16 pins, but I wasn't     |                              |
|     exactly sure how.* -- heartofasquid     |                              |
|     -   I thought the PRUs had a 16bit      |                              |
|         parallel capture mode or are all    |                              |
|         the pins not available on the BBB?  |                              |
|         (need to consult the docs) section  |                              |
|         4.5.2.2.3.2 of the tech ref         |                              |
|         spruh73c.pdf One thought I had was  |                              |
|         to use both PRUs to capture         |                              |
|         alternate bytes/words but that was  |                              |
|         just a thought, again are all the   |                              |
|         pins available?                     |                              |
|     -   I'd made a mistake, it looks like   |                              |
|         all of PRU0's GPI pins may be       |                              |
|         available, if we are happy to lose  |                              |
|         the microSD (no big loss - there    |                              |
|         are other ways to get data in/out   |                              |
|         of the BBB). So, we can             |                              |
|         theoretically get high-res captures |                              |
|         up to about 15bits, if we need 1    |                              |
|         pin for the clock.                  |                              |
+---------------------------------------------+------------------------------+

### Dec 4th

-   [BBB and 5Msps 12bit : a SO
    question](https://electronics.stackexchange.com/questions/204317/what-is-the-best-setup-for-a-5msps-12bit-adc-to-beaglebone-black-setup)
-   Registered at element14.com =)

### Dec 5th

-   Graphing all elements @GaiteLyrique
-   5 to 100 DC
    -   <http://www.researchgate.net/post/Does_someone_know_an_simple_electronic_design_that_takes_small_PCB_area_producing_a_stable_100_DC_voltage_from_a_power_supply_of_5V2>
    -   <https://www.maximintegrated.com/en/app-notes/index.mvp/id/1751>

<!-- -->

-   Call/Chat Emmanuel - electronic board - 2 months is what he'd expect
-   Discussion S - review of scope / finetuning signals
    -   Necessity at 100V to separate HV to avoid interferences / noise
    -   Remark: using PRUs, we can go up to 50MHz (at least) from the
        ADC
-   Validation of parallel ADC
-   Mapping the Shield knowledge graph
-   Followup MIC

+------------------------------+---------------------------------------------+
| ![](git.png "git.png")       | ### Dec 6th                                 |
|                              |                                             |
|                              | -   Reflexions on documentation [ coming    |
|                              |     from this                               |
|                              |     presentation](:File:Wozniak-OHS2011.pdf |
|                              |  "wikilink")                                |
|                              |     on OSH                                  |
|                              | -   5Msps -&gt; Parallel -&gt; PRU up to 12 |
|                              |     bits -&gt; can go further than          |
|                              |     5Msps (SOA)                             |
|                              | -   Buffer has to come (no, not the buffer  |
|                              |     app - real world buffer)                |
|                              | -   Thinking as well on architecture        |
|                              |     -   Motor + transducer + top in the     |
|                              |         probe                               |
|                              |     -   Board + BBB (Node.js still..)       |
|                              |     -   Output (if necessary)               |
|                              |                                             |
|                              | ### Dec 7th                                 |
|                              |                                             |
|                              | -   Busy business day                       |
|                              | -   Usual monday meeting                    |
|                              |     -   awesome progress on mech part.      |
|                              |         Seems robust, small, ...            |
|                              |     -   need to follow the power usage of   |
|                              |         POLULU \^\^                         |
|                              | -   What about a webcam video format?       |
|                              |     -   **WebRTC** -&gt; awesome stuff at   |
|                              |         <https://rtc.io/> for nodejs +      |
|                              |         webrtc                              |
+------------------------------+---------------------------------------------+

### Dec 8th

-   <http://www.theopensourceway.org/book/The_Open_Source_Way-How_to_tell_if_a_FLOSS_project_is_doomed_to_FAIL.html>
    : nice doc to failproof a FLOSS project.
-   FPGA team
    -   FPGA vs µC : discussion ongoing with F&V - seems going
        towards RP. Sane, pragmatic approach. If the RP is cracked, that
        could unlock many things.
    -   Simulations to come from MIC
-   Another supplier
    -   seeedstudio.com(reco by F&V)
    -   See also <http://pcbshopper.com/>
-   PCBA abroad :
    -   [myropcb](http://www.myropcb.com/services-capabilities/pcba-services/)
    -   [nortechsys](http://www.nortechsys.com/nortech-advantagepcba-protyping-short-run-production/)
    -   [SeeedStudio](https://www.seeedstudio.com/service/index.php?r=upcb)
        only north america
-   PCBA in france:
    -   [Quad Ind](http://fr.quad-ind.com/assemblage-pcb/)
    -   [PCB-Pool](https://www.pcb-pool.com/ppfr/info_pcb_assembling.html)
-   [Fun on gerber and silk
    screens](http://makezine.com/projects/make-36-boards/make-your-own-dmn-board-part-3-silkscreen-and-gerbers/)

### Dec 9th

-   Following some [design thinking
    classes](https://www.coursera.org/learn/design-thinking-innovation/home/welcome)
    for the sake of soft design & fun

### Dec 11th

-   Update the *Culture* repertory in our drive :p
-   [ Piezo
    suppliers](:Category:Transducer#Transducer_suppliers "wikilink") on
    their way
-   Mapping the DITSO resources - update
-   Apéro !

### Dec 12th

-   GP1A57HRJ00F // photo interrupter
-   Server for again 3 days...

### Dec 14th

-   Holocracy progress
-   Comments from S: problems with HV system

+---------------------------------------------+------------------------------+
| ### Dec 15th                                | ![](bas.jpg "bas.jpg")       |
|                                             |                              |
| -   First elements from A - [ first draft   |                              |
|     ](:File:151216_-_A.pdf "wikilink")      |                              |
|     (pdf file).                             |                              |
|                                             |                              |
| ### Dec 16th                                |                              |
|                                             |                              |
| -   Another feedback from S : small,        |                              |
|     interesting DC/DC power convertors      |                              |
|     from RECOM. Excellent idea.             |                              |
| -   Some great GIT cheatsheet -             |                              |
|     <https://gist.github.com/mplewis/a7563c |                              |
| 7cb589048a071b>                             |                              |
| -   The sysadmin apprentice :               |                              |
|     <http://www.commitstrip.com/fr/2015/11/ |                              |
| 18/the-sysadmins-apprentice/>               |                              |
+---------------------------------------------+------------------------------+

### Dec 19th

-   S has started, on it

### Dec 20th

-   Adafruit fun - display and printing ?
    -   Adafruit 1.8" Color TFT Shield w/microSD and Joystick:
        <https://www.adafruit.com/products/802>
    -   WIFI feather : <https://www.adafruit.com/products/2821>
    -   touchscreen : <https://www.adafruit.com/products/1651>
-   Thermal printing : <https://www.adafruit.com/products/2753> but no
    level of grays

### Dec 22nd

-   Progress A / S
-   Caractérisation du piezo :
    -   <http://www.biosono.com/PrmtLgd/PrmtLgd.php?id=TrnsRlc>
    -   <http://www.brl.uiuc.edu/Downloads/bigelow/APPENDIX%20C.PDF> ou
        en local sur : [:File:APPENDIX
        C.PDF](:File:APPENDIX_C.PDF "wikilink")
    -   <http://www.vtvt.ece.vt.edu/research/papers/08sas.pdf> ou en
        local sur : [:File:08sas.pdf](:File:08sas.pdf "wikilink")

### Dec 27th

-   Some PCB Assembly recommendation
    -   <https://groups.google.com/forum/#!topic/tcmaker/rXdZSrWvRTU>
    -   <https://forum.sparkfun.com/viewtopic.php?f=20&t=36339>
-   OSH Park, purple board, doesn't do assembly
-   <https://macrofab.com/> -- GO FROM PROTOTYPE TO MARKET FASTER THAN
    EVER BEFORE -- excellent review

### Dec 28th

-   Back from festive period ! But no slack:
    -   First iteration of A (though no buffers [:File:Top
        View.jpg](:File:Top_View.jpg "wikilink") ) -- buffers as
        74AC541MTC ?
    -   Schematics and BOMs from S
    -   Cacophony everywhere
-   <https://www.youtube.com/watch?v=aPVLyB0Yc6I> Eating bears
-   LCD at <http://www.espruino.com/PCD8544>
-   Autre display / TFT :
    <https://learn.adafruit.com/1-8-tft-display> .. et une micro SD
    intégrée =)
-   BBB headers : <https://www.adafruit.com/products/706> (Stacking
    Header Set for Beagle Bone Capes (2x23) @5\$)

### Dec 29th

#### News

-   vieux displays: <https://www.adafruit.com/categories/99>
-   <https://www.adafruit.com/product/358>
-   <https://www.adafruit.com/products/2478> : 240by 320 screen, touch,
    sd
    -   The display can be used in two modes: 8 bit or SPI. For the
        fisrt you'll need 12 lines total. Second mode requires only 5
        pins total but is slower than first.
    -   In addition, 4 pins are required for the touch screen (2
        digital, 2 analog)
    -   Tuto :
        <https://learn.adafruit.com/adafruit-2-4-color-tft-touchscreen-breakout>
-   <https://www.adafruit.com/products/1480> : 320 by 240 screen, 4-wire
    SPI to communicate and has its own pixel-addressable frame buffer

**Seems like the BBB SPI communication rate are around 0.1s to draw the
image over SPI.. may be a tad slaw to only display an image**

#### Bots

-   Onboarding bot for Slack at
    <https://18f.gsa.gov/2015/12/15/how-bot-named-dolores-landingham-transformed-18fs-onboarding/>
    (in ruby)

### Dec 30th

-   Did automatic backup for the wiki, for the migration - yeahhh
-   Smartassthoughts
    -   *The absence of deal-breaking flaws is more important than the
        presence of any extras.* You don’t need anything special
        to succeed. You just need to do the essentials properly.
    -   Power is like being a lady… if you have to tell people you are,
        you aren’t. -- MT
-   FTS
-   Don't forget spider jerusalem's example - bards, journalists, and a
    merry cacophonic 2016

### Jan 6th

-   Trial on PCBCart
-   Render of the Murgen 1.0 board

![](Murgen Cape 1.0.png "Murgen Cape 1.0.png"){width="800"}

### Jan 8th

-   Small adjustments from the questions raised by PCBCart

### Jan 11th

-   Completed the S project -- CLOSED ;)
-   The A project is ongoing

### Jan 12th

-   Luc back in France

### Jan 15th

-   Boards:
    -   Confirmation that Seeedstudio does not ship out of north america
    -   Getting other options and quotes from Advanced Circuits,
        Macrofab (awesome interface), PCB Pool.
-   Need for a filter to get be sure , there's a low frequency component
    that remains: to remove- and to center around 0V ?

![](Screenshot_2016-01-15-12-08-13.png "fig:Screenshot_2016-01-15-12-08-13.png"){width="600"}
Let's cut it to 500kHz ?

-   For headers, we have
    -   12 input pins on P8 for PRU1 and 1 input pin for PRU1 on P9,
        these have been assigned for 12bitADC+Clock and the rest,
    -   SPI for DAC,
    -   Buffer enable and motor control have been assigned to PRU0.
-   For the controls in prototyping:
    -   SW1 controls the gain range for TGC
    -   SW2 controls the input range of the ADC,
-   Updating the blog as well, integration of disqus

### Jan 16th

-   disqus working
-   creating something on makake.. but seems bugged at the moment
-   list of components on the blog
-   discussions with edgeflex (thanks flylabs!) and macrofab (fun, and
    willing to test a 4 layer project in beta - only working in 2 layers
    so far)
-   work with S to integrate a high pass filter (1MHz+) following the
    echo on Jerome's hand
-   Follow up with Charles
    -   working on the RP with a student
    -   exploring collaborations

### Jan 18/19th

-   Call with Edgeflex
-   Breakout boards for SMDs :
    -   <https://www.adafruit.com/products/1210> /
        <https://www.adafruit.com/products/1206> / ...
    -   <https://www.adafruit.com/products/1281> to test
-   Followup with Macrofab
-   Producing the XYRS from Altium
-   Starting mini board - board \#2 -- what name (if not murgen, Tobo ?)
-   Order for a ThermalPiPrinter :)

### Jan 19th

-   Slight tweak of the budgetting for engineering a probe :) we have
    this
    [GDoc](https://docs.google.com/spreadsheets/d/1HbeRCOVrJFWL29VbagtKip8LvDqiuHKvDMe9bzmxfmM)

![](dt160120.gif "dt160120.gif")

### Jan 20th

-   What about having a µC ( PIC24FJ128GC010 ?) right after the analog
    part - could be an additional board/cape stacked below (so with
    microcontrolleur and alimentation)
    -   it would stream data like a wifi camera
    -   receives the ping from the motor controleur
-   should we be ordering SMD stuff (flux, fer à souder, soufflerie?) -
    seems an idea
-   Création des modules !

### Jan 21st

-   Changed WP template to something more readable
-   Post on HN .. even went 2nd :)

![](HN6-2nd post.png "HN6-2nd post.png"){width="300"}

-   Awesome work from Farad

![](Screenshot_2016-01-21-23-50-13.png "Screenshot_2016-01-21-23-50-13.png"){width="600"}

### Jan 22nd

-   Updated the [GitHub
    Readme.md](https://github.com/echopen/hardware/tree/master/electronics/murgen%201.0%20beta)
    (still lacking a pic, damned!)
-   Outputs from the HN post
    -   3700 visitors in less than 20 hours
    -   Interesting comments at
        <https://news.ycombinator.com/item?id=10944617>
    -   Interesting contacts (anfractuosity - leptitg )
    -   Interesting page :
        <https://www.anfractuosity.com/projects/hardware-development-links/>
-   TODO : get something on reddit ?
-   <http://finda.photo/#v2> TOF en CC0

+---------------------------------------------+------------------------------+
| ### Jan 23th                                | ![](tobo-5.png "tobo-5.png") |
|                                             |                              |
| -   Murgen on                               |                              |
|     <http://radar.oreilly.com/2016/01/four- |                              |
| short-links-22-january-2016.html>           |                              |
| -   Prez done here : [:File:160115 -        |                              |
|     murgen\_prez.pdf](:File:160115_-_murgen |                              |
| _prez.pdf "wikilink")                       |                              |
| -   Awesome boost on github and the wiki    |                              |
| -   adding some to the documentation        |                              |
|     -   1.  TODO : need to get to read more |                              |
|             the                             |                              |
|             [TAPR](http://www.tapr.org/ohl. |                              |
| html)                                       |                              |
|             and the full license            |                              |
|             <http://www.tapr.org/TAPR_Open_ |                              |
| Hardware_License_v1.0.txt>                  |                              |
|     -   1.  TODO : add CONTRIB.TXT and      |                              |
|             CHANGES.TXT                     |                              |
|                                             |                              |
| -   1.  TODO : failproof OSH                |                              |
|                                             |                              |
| ### Jan 24th                                |                              |
|                                             |                              |
| -   added datasheets                        |                              |
| -   1.  TODO : think about a USB/BT/...     |                              |
|         output for the board                |                              |
| -   Output ? What format? USB - but I'd     |                              |
|     rather have wireless ?                  |                              |
|     -   Wi-Fi Direct promises               |                              |
|         device-to-device transfer speeds of |                              |
|         up to 250Mbps                       |                              |
|                                             |                              |
| ### Jan 25th                                |                              |
|                                             |                              |
| -   Tobo is born ;) as a goodie/bonus for   |                              |
|     murgen                                  |                              |
| -   Some resources (thanks Oliv' =) )       |                              |
|     -   <http://www.evilmadscientist.com/20 |                              |
| 11/improving-open-source-hardware-visual-di |                              |
| ffs/>                                       |                              |
|     -   <https://opendesignengine.net/> not |                              |
|         working at the moment               |                              |
| -   Repos work                              |                              |
|     -   Github hooks:                       |                              |
|         <https://github.com/icefox/git-hook |                              |
| s>                                          |                              |
|     -   what's <http://www.solderpad.com/>  |                              |
|         worth ?                             |                              |
| -   Reading :                               |                              |
|     <http://opensourceecology.org/wiki/Open |                              |
| _Design_Engine>                             |                              |
| -   FUN USB keyboard emulator :             |                              |
|     <http://www.instructables.com/id/USB-PC |                              |
| B-Business-Card/>                           |                              |
+---------------------------------------------+------------------------------+

### Jan 27th

-   GitHub signing a release :
    -   Howto :
        <https://wiki.debian.org/Creating%20signed%20GitHub%20releases>
    -   Creating a key
        <http://ekaia.org/blog/2009/05/10/creating-new-gpgkey/>
-   Hardware:
    -   PCBs have been ordered, 3 days to come.
    -   1st and 2nd boards on their way.

1.  TODO: sign a release as soon as some code is on the way

### Jan 29th

-   <http://semver.org/> for semantinc versionning of releases

### Feb 13th

-   Lots under way..
-   [Goblin](http://murgen.echopen.org/pcbs-have-reached/) being
    released
    -   A 2 layer PCB.. easier
    -   Less components, less expensive
    -   However, needs to be tested !

<!-- -->

-   **Required**: we need to sit with electronics experts to check how
    Murgen, Tobo, Goblin, and Mira can merge - for a modular board -
    ideally as easy as possible to use!
-   IDEA: capelec!
-   Need also to push Goblin's files on the repo. Those are made with
    Eagle, not Altium, so a bit less options, but still interesting to
    see how to work with those files =)

### Feb 15th

Was about time I got some serious litterature review :)

-   <http://sci-hub.io/10.1109/ULTSYM.2015.0517> for a full fledge
    Smartphone Probe =)
-   [Microcontroller USB interfacing with MATLAB GUI for low cost
    medical ultrasound
    scanners](http://www.sciencedirect.com/science/article/pii/S2215098615303220)

Some others

-   Integrating hardware and software for the development of
    microcontroller-based systems
-   IDEA: Design of a USB based multichannel, low cost data acquisition
    system using PIC microcontroller

### Feb 16th

-   Waiting for the board ;)
-   Awesome work : Development of a wide band front end echo sounder
    receiver circuit by Jatin Sharma ( definitely need to contact him)

### Feb 17th

-   Fun hardware:
    -   IDEA : Good stepper: 99\$ /
        <https://www.pololu.com/product/2294>
    -   There are cheaper steppers on Lextronics (+driver)
    -   Pololu - LP 6V Motor with 48 CPR Encoder for 25D mm Metal
        Gearmotors (No Gearbox) (https://www.pololu.com/product/2280 )
    -   <https://www.pololu.com/product/2213> for a small motor
-   3D models of RPi, BBB:
    -   BBB: <https://www.thingiverse.com/thing:920804>
    -   RPi: <http://www.thingiverse.com/thing:278113>

### Feb 18th

-   Interesting read at
    <http://wp.josh.com/2014/03/03/the-mystery-of-the-zombie-ram/> !!
-   Discussions on mechanics =)

### Feb 19th

-   IDEA : display : 128² OLED screen:
    <https://www.adafruit.com/products/1431>

### Feb 21st

-   Asking feedback from M. Cooke
-   <http://sci-hub.io/10.1109/ULTSYM.2013.0526> for *Smartphone-based
    Portable Ultrasound Imaging System : A Primary Result* .. can't
    manage to reach them.
-   ebay :
    -   Aloka ASU-66 --
        <http://www.ebay.fr/itm/Aloka-ASU-66-Ultrasound-Probe-/221690345989?hash=item339dc63a05:g:l~gAAOSwBLlU3n1H>
    -   Aloka ASU-32H-3.5 Mechanical Probe --
        <http://www.ebay.com/itm/Aloka-ASU-32H-3-5-Mechanical-Probe-/190660257677>
    -   ATL-ADR-5-5-MHz-7-mm-Ultrasound-Transducer-Probe-for-UM-4-7081
    -   [ATL Access 10PV](ATL_Access_10PV "wikilink") is a sector array
        ultrasound transducer probe. The ATL Access 10PV is a
        mult-frequency probe with a range of 5.0, 7.5 and 10.0 Mhz. --
        <http://www.ebay.com/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313.TR0.TRC0.H0.XATL+Access+10PV.TRS0&_nkw=ATL+Access+10PV&_sacat=0>
        \*\*AWESOME\*\*
    -   IDEA : mechanics design idea !
    -   Same for ATL Access B10
    -   All \*\*ATL Access\*\* aaahhhh
        -   ATL-Access-C-3-0-MHZ-12-7mm-dia-Ultrasound-Transducer-P-N-101-25909-72-3862
    -   GE Kertz Technik S-VNA5-8 Transducer

### Feb 22nd

-   IDEA : interfacing murgen with a FPGA ? Solution here :
    store.hackaday.com/products/xula2-lx9
-   IDEA: doing a probe emulator? Signal generation upon a pulse
    transmitted : a physical emulator for the probe head =)

### Feb 23rd

-   Passphrase.io seems interesting =)

### Feb 24th

-   What can we do with wifi / ESP8266 //
    <http://makezine.com/2015/04/01/esp8266-5-microcontroller-wi-fi-now-arduino-compatible/>
    ?
-   <http://darksearch.io/> is fun ?
-   No stuff - <https://sivers.org/gifts> in favor of it =)
-   Some news from Amit

### Feb 25th

-   Boards reached: issue with the 5V and GND - shortage

### Feb 26th

-   Further tests. Shortage still exists.
    -   Short is not on the PCB. Appears after solder.
-   Found that the RECOM component was designed to be upside down --
    need to resolder it. Luckily it was a via component.
    -   This would not be the source of the short anyhow.
    -   EF recommends that we burn 10A on the 5V plane to see which
        component would burn.. hmm i'm quite shy to do this :p
-   Documenting the issue on github.
-   Sending back boards to EF.

### Feb 28th

-   Starting the interim report.

### Feb 29th

-   Found the source of the short, ADL5511, 5V and GND inverted...
    -   TODO : amend the altium files to correct the ADL5511 and the
        RECOM tracks
-   TODO : sampling freq to be documented

### Mar 1st

-   Sending back the boards

### Mar 3rd

-   Receiving new, corrected boards
-   SO qusetions to be tapped into?
    -   <http://stackoverflow.com/questions/35681099/beaglebone-black-control-gpio-with-pru>
    -   <http://stackoverflow.com/questions/35747954/beaglebone-move-data-from-pru-to-ddr-ram>
-   Newscastle published something new on their mechanical probe,
    awesome!!
    <http://www.ncl.ac.uk/eee/research/groups/coms2ip/ultrasound-imaging.htm>

### March 4th

-   Testing the board on the morning

### Sunday, Mar 6th

-   Posts about the day hacking at
    -   <https://hackaday.io/project/9281-murgen/log/33275-getting-the-first-echoes>
    -   <https://github.com/kelu124/murgen-dev-kit/blob/master/Session_1.md>

### Mar 7th

-   HackerNews : <https://news.ycombinator.com/item?id=11232144>
    -   <https://github.com/abhishek-kakkar/BeagleLogic/wiki>
    -   <http://theembeddedkitchen.net/beaglelogic-building-a-logic-analyzer-with-the-prus-part-1/449>
    -   <http://dangerousprototypes.com/docs/Logic_Pirate>
    -   <http://dangerousprototypes.com/docs/Logic_Shrimp_logic_analyzer>
-   Matos
    -   Inverseur : CD74HC4049E
    -   Caps 1.27mm
        -   M50-1900005
        -   M50-2020005

### Mar 8th

-   GSCholar pour HV7360 (to solve the issues) :
    10.1109/ULTSYM.2015.0140
-   HV7361 : Sharma
-   TODO
    -   Pulser: intégrer un schéma sur le readme de murgen
    -   VPE est a 5V sur notre board - 3.3 en typical. Logique à
        remonter?
    -   Add a resistance in parallel of the transducer?
-   Damn!! The alimentation voltage was low... because it takes 6.5V to
    12V! Will need to put 9V in through the thermal printer alimentation

### Mar 11th

-   Session 2 : Non-controlled pulsing, inverters, better echoes

### Marc 14th

-   Starting to get echoes

### Mar 15th

-   Session 3 : Getting controlled pulsing, but width not controlled

### March 18th

-   Sending his board to prof Charles

### 19 March 2016

-   Session 4 & 4b
    -   Testing the board with the transducer
    -   Testing with the BitScope

### March 20th

-   Getting the image!

![](image_grey_proto.png "image_grey_proto.png")

-   -   Assembling everything
    -   Coding in python
    -   Thanks bitscope

<!-- -->

-   Gallery:

<File:SC_0226.JPG> <File:SC_0227.JPG> <File:image_grey_proto.png>
<File:SC_0154.JPG>

### March 21st

-   Doc
    -   Documenting on <https://hackaday.io/project/9281-murgen> --
        visit, by all means, that's cute and nice!
    -   Same documentation on the github repo
-   Modular design in on with Benoit ! Let's check with Sofian
-   TODO:using SPI on the board
    -   plugging a SPI
    -   pluging the pulseroff in the buffer part?
-   TODO:logo of murgen in vector

### March 22st

-   PENDINGTODO
    -   print and distribute the interim report
    -   Organizing elections for the association
        -   Define responsibilities of all
        -   Review of les status de l'association
        -   Review of the reglement intérieur
    -   Definir who has access to the twitter account
    -   Wiki delivery
    -   Documentation
    -   BM's gerbers, altiums et al
    -   Costing of mira
    -   License issue on the wiki
    -   Budget update - what do we have?
    -   Project forecast - where do we go?
    -   Restructuration du wiki
    -   Page de veille a mettre sur le wiki
    -   Creer une page competition
    -   Traiter les "objectifs" de la fondation fabre et les finir
    -   Gérer les cotisations, faire un appel à cotisation
    -   publier les soutenances de F&V?

<!-- -->

-   Some SO questions:
    -   <http://stackoverflow.com/questions/35939058/beaglebone-without-dac-from-digital-to-analog-converter>
    -   <http://stackoverflow.com/questions/35910431/getting-beaglebone-prus-to-work-using-pasm>
    -   <http://electronics.stackexchange.com/questions/222661/connecting-large-number-of-i2c-slaves-using-i2c-multiplexers-and-buffers>

### March 23rd

-   A challenge page was created: [Challenge: the module
    approach‎](Challenge:_the_module_approach‎ "wikilink")
    -   working on modules =)
        -   [:File:listofmodules.png](:File:listofmodules.png "wikilink")
    -   thinking of the motherboard (contribution of benoit)
        -   [:File:motherboard.png](:File:motherboard.png "wikilink")
    -   Enveloppe detection :
        <http://echopen.org/index.php?title=Analog_Parts_%28Farad%29#Envelope_detector>

### March 24th

-   AOP (high speed 420MHz) THS3001 (Amit)
-   TODO:
    -   MFab - plan
-   Presentations tonight!
-   OUIDIDIT ! First presentation of echopen's working prototype
    -   <https://storify.com/ForTheFuture/firstech>
    -   <http://www.makery.info/2016/03/29/echopen-lance-une-sonde-dechographie-open-source/>

### March 27th

-   Getting good echoes with the TGC maxed!

### March 28th

-   Playing with bitscope -&gt; issue from the noise -&gt; usb plugin
    got !

### March 29th

-   order for the usb denoiser
-   <http://www.st.com/web/en/catalog/mmc/FM141/SC1169/SS1576?sc=stm32f3>
    : Getting 5Msps =)
-   Farnel price bitscopes
    -   <http://uk.farnell.com/bitscope/bs05u/oscilloscope-logic-analyzer-2/dp/2432906>:
        59£ (73€) (HT?)
    -   <http://uk.farnell.com/bitscope/bs05p/oscilloscope-adaptor-2ch-20mhz/dp/2455593>
        : 89£

### March 31st

-   Doing some new fantoms
-   Receiving the AFORP's guys :
    <https://twitter.com/OFresnoye/status/715519438037073920> and
    updating their page [AFORP](AFORP "wikilink")

### April 1st

-   Generating pulses with RPi :
    <http://codeandlife.com/2012/07/03/benchmarking-raspberry-pi-gpio-speed/>
    -- up to 22MHz
-   Sofian's back ;)

### April 3rd

-   Cleaning the acquired images

### April 4th

-   4T scan conversion algo OK and working

### April 5th

-   TODO: creer les liens sur le software/readme -&gt;
    [Software (murgen-dev-kit)](Software_(murgen-dev-kit) "wikilink")
    vers les fichiers sources

### April 7th

-   trying some docs at
    <https://github.com/kelu124/murgen-dev-kit/blob/master/hardware/doc/murgen-dev-kit.markdown>
-   starting with the modules.. should start a [Worklog - the module
    approach](Worklog_-_the_module_approach "wikilink") page based on
    the [Challenge: the module
    approach](Challenge:_the_module_approach "wikilink") page... coming
    soon?

### April 8th

Nice reading =)

-   Basecamp outlines their goals -- which they say have always been the
    same -- on their website:
    -   Have fun
    -   Do exceptional work
    -   Build the best product in the business
    -   Experiment
    -   Pay attention to the details
    -   Treat people right
    -   Tell the truth
    -   Have a positive impact on the world around us
    -   Give back
    -   Keep learning.
-   "We’re also big believers in business 101. We don’t spend more than
    we earn, we don’t waste money on things that don’t matter, we don’t
    give away everything for free and hope we’ll figure it out before we
    run out of cash. We’re in business to stay in business, and we have
    15 profitable years in a row to back it up."

### April 9th

Some reads on PRUs:

-   <https://hackaday.com/2014/06/22/an-introduction-to-the-beaglebone-pru/>
-   <https://www.embeddedrelated.com/showarticle/603.php>
-   <https://www.embeddedrelated.com/showarticle/586.php>
-   <https://github.com/beagleboard/am335x_pru_package>

### April 10th

-   Sofian is delayed :/
-   Lines are defined !

### April 11th

Choice of a uC: "le boulot des microcontrollers, ce qui me gêne sur
l'espruino c'est le manque de sortie wifi - si on veut sortir des
données en wireless." Deux choix se profilent

-   WICED : STM32F205RG 120MHz ARM Cortex M3 MCU : 17 timers et 3 ×
    12-bit, 0.5 μs ADCs with up to 24 channels and up to 6 MSPS in
    triple interleaved mode, 8- to 14-bit parallel camera interface (48
    Mbyte/s max.)
-   Le WifiMCU : EMW3165 : M4: STM32F411CE @100MHz, DSP+FPU, 1×12-bit,
    2.4 MSPS A/D converter -- Ce qui me fait peur est un WifiMCU de base
    en LUA, a voir comment repasser sur du plus bas niveau. L'avantage
    par contre c'est qu'il est dispo chez hackspark, et coute 18€ au
    lieu des 35\$ du WICED =)

Remarques : Avec le M3 tu perds les instructions DSP et un FPU optionnel
(cf <https://en.wikipedia.org/wiki/ARM_Cortex-M>). Par contre je ne sais
pas si c'est correctement exploité, ni si on en a vraiment besoin.

Il y a aussi le Module Particle "Photon"
<http://www.lextronic.fr/P37394-module-particle-photon.html> (M3 120 MHz
et wifi) ou l'Arietta
<http://www.lextronic.fr/P32050-module-microcontrole-arietta-g25.html>

-   Apparament module fermé

### April 12th

-   WifiMCU ordered

c'est vrai que le WifiMCU est plutôt tentant aussi. Faudrait passer un
peu de temps à faire un mini comparatif de ces petites bêtes, voir les
benchmarker. On peut se faire une petite compétence autour des
STM32F4xxx (et leurs 800 pages de docs) avant de passer au FPGA?

Raspi Oscilloscope
------------------

### Source

-   [Source](https://digibird1.wordpress.com/raspberry-pi-as-an-oscilloscope-10-msps/)
-   [GitHub](https://github.com/digibird1/RPiScope)
-   MapPi issue 24 -
    ![](The-MagPi-issue-24-en.pdf "fig:The-MagPi-issue-24-en.pdf")
-   Some other reads (gallery below)

### Gallery

<File:p620.png> <File:p621.png> <File:p622.png> <File:p623.png>
<File:p624.png> <File:p625.png> <File:p626.png>

### BOM

-   I’m using a CA3306 ADC from Intersil. This is a 6-bit 15 MSPS ADC
    with a parallel read out.
-   Buffer : 74HC4050
-   RPi 1
-   2 SD Cards
-   Nappe + TBone ?
-   Repo mis à jour :
    <https://github.com/echopen/hardware/tree/master/electronics/murgen>

Resources
---------

-   <http://passwordsgenerator.net/sha256-hash-generator/>

<Category:WorkLog>
