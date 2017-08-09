# Next Steps..

## Status today

 Since the end of November, where I knew nothing about electronics, I managed to learn about the following points:

* Electronics : back to the basics
* Datasheets: learning to read and understand those
* Fabs: getting to know the ecosystem, touch base with some, work an excellent agreement
* Transducers: an ongoing process.. but I do know a bit more about those.
* Documentation: getting to know more about the process of documenting open-source hardware... and getting the first automation tools on.
* A worklog: starting with the [first session with the board](/worklog/Session_1.md). Not too much a bad idea of having written it, it still has a lot of information.

## Community engaged

The results in terms of community were quite good. We managed to onboard on several media (stats as of 23/4/16):

* [HackerNews](https://news.ycombinator.com/item?id=10944617): made it to the first page for a couple of hours, 122 points, 43 comments
* [Hackaday.io](https://hackaday.io/project/9281-murgen): where the project is posted - 3.6k views, 97 followers, 25 likes so far, plus an [article](http://hackaday.com/2016/04/12/a-developers-kit-for-medical-ultrasound/).
* An [article on GeekTimes](https://geektimes.ru/post/274478/), a russian hackernews or so it seems, 11.6k views and 50 stars, with 68 comments.
* A murgen board acquired by Vanderbilt's Charles' lab.

## Leftovers

I'm now left with the following stuff to work with:
* An empty shell of a ultrasound scanner probe
* An arduino nano
* A ESP8266
* Two thermal printers
* A Raspberry 2
* Two BeagleBone Black
* A servo
* Some rapid logic invertors
* A 3.3/5V level shifter

What can I do with those?

## ToDo

We only have now to play with the following items on the next phase:

1. Playing with the design and fab the modules: 3 to go in CMS (HV/TGC/MD, enveloppe detection, SPI ADC) and 2 in stripboard mode (alim, based on the breadboard 3.3V and 5V, as well as the controler, maybe an arduino nano at first) - and start the github repo / [echOmods](https://hackaday.io/project/10899-echomods) hackaday pages as well. Work on this with Sofian and Vlad. See also the [echOmods repo](https://github.com/kelu124/echomods/).
2. Playing with an electronic emulator of the transducer - as well as an electronic model. Work on this with a partner/supplier.
3. Play with a ultrasound durable fantom. Work on this with **staticdet5** (comment on HAD). Started a [project with Virginie and Static on HAD.io](https://hackaday.io/project/11478-open-source-ultrasound-phantoms).
4. Play with the BeagleBone PRUs. Work on this with Vanderbilt.
5. Playing with some intelligent uC of FPGA. uC has my preference at first for ease of use. WifiMCU seems fun (has a 8$ STM32F411CE - 100MHz, 2.4Msps ADC, FPU, DSP instructions and WiFi to stream!) or the [Feather Wiced](https://www.adafruit.com/product/3056) (arduino IDE compatible, based on a 34$ STM32F205 ARM Cortex M3 processor running at 120MHz. Project codename would be [Croaker](https://github.com/kelu124/echomods/croaker), not created yet. Who's volunteering?

# Some resources to move further

## Bibliography

### STM32 ?
* http://www.st.com/web/en/resource/technical/document/application_note/DM00050879.pdf : How to improve ADC accuracy when using STM32F2xx and
STM32F4xx microcontrollers
* http://www.micromouseonline.com/2009/05/26/simple-adc-use-on-the-stm32/

### Working with the PRUS:
* *For low-speed comms, conventional I2C or similar protocols can be used, and there is no need to use a PRU. For high-speed comms the PRU may be extremely useful because it can service the hardware with no interruptions due to Linux context switching, and no overhead is experienced by the main ARM processor. Here are some examples that should be feasible; basically quite a few possibilities, such as interfacing to a fast ADC (e.g. analog capture)*
* http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/05/22/bbb--working-with-the-pru-icssprussv2
* https://theembeddedkitchen.net/beaglelogic-building-a-logic-analyzer-with-the-prus-part-1/449 *BBB is a 100MHz logic analyzer on a BeagleBoneBlack* : Demo over the http://beaglelogic.github.io/webapp/
* http://r.git.net/beagleboard/2013-10/msg00204.html : can the PRU be used to interface the Beaglebone to external ADC? I need to capture 500 micro-seconds of data at a 5 MHz rate? -> It depends on the interface to the ADC. There is a parallel capture interface that will easily run that fast, and you may be able to use the bit-shift interface to do serial or something like SPI if the PRU's capability lines up with what your ADC wants to see.
* http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/08/04/bbb--high-speed-data-acquisition-and-web-based-ui : In its current state, it grabs analog data from an ADC, and dumps it into memory on the BBB, ready to be displayed or further processed. It could be used for gathering analog information from sensors, CCDs or other data acquisition use-cases. To be reasonably useful, **the desire was for it to support 20Mbytes/sec of data or more**. It does achieve this, but it is for further study to find higher speed methods.  Once the data has been captured (2000 samples in this example), the command byte is acknowledged, so that the Linux hosted application can know that the PRU has completed. The PRU now sits and waits for a new instruction from the Linux hosted application. **-> works for us - fixed depth = fixed # of samples**
* http://exploringbeaglebone.com/chapter13/#The_ADS7883_Single-Channel_12-bit_ADC_1MSps_max
* 5Msps -> Parallel -> PRU up to 12 bits -> can go further than 5Msps (SOA) 

* https://hackaday.com/2014/06/22/an-introduction-to-the-beaglebone-pru/
* https://www.embeddedrelated.com/showarticle/603.php
* https://www.embeddedrelated.com/showarticle/586.php
* https://github.com/beagleboard/am335x_pru_package


**http://stackoverflow.com/questions/35939058/beaglebone-without-dac-from-digital-to-analog-converter
**http://stackoverflow.com/questions/35910431/getting-beaglebone-prus-to-work-using-pasm


### WebRTC

* awesome stuff at https://rtc.io/ for nodejs + webrtc

### PCBs
* Another supplier : seeedstudio.com(reco by F&V), see also http://pcbshopper.com/

* PCBA abroad : myropcb, nortechsys. SeeedStudio does only north america in fab-mode

* PCBA in france: Quad Ind, and PCB-Pool

### Caracterization of the piezos:

Caractérisation du piezo :

* http://www.biosono.com/PrmtLgd/PrmtLgd.php?id=TrnsRlc
* http://www.brl.uiuc.edu/Downloads/bigelow/APPENDIX%20C.PDF ou en local sur : File:APPENDIX C.PDF
* http://www.vtvt.ece.vt.edu/research/papers/08sas.pdf ou en local sur : File:08sas.pdf



## Documentation tools and processes

Still a work in progress... but the key here is to move towards a maximum of automation. No other solution.

## Fun stuff

Using the Pi as an oscilloscope:
* [Is Pi powerful enough for an oscilloscope project?](http://raspberrypi.stackexchange.com/questions/4129/is-pi-powerful-enough-for-an-oscilloscope-project)
* [Raspberry Pi as an Oscilloscope @ 10 MSPS](https://digibird1.wordpress.com/raspberry-pi-as-an-oscilloscope-10-msps/)
 


