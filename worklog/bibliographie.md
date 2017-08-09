# Our setup

For details, read the bibliography below =)

## Recap and history

|Partie |                                                                                                                              Solutions considérées                                                                                                                            |                 Solutions Choisies                |                    Evolutions considérées?           |
|:---------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------:|:------------------------------:|
|       Transducer      | FURUNO 520-5PSD (Shatin Sharma Thesis) GP2000 (Philippe Levesque) DGH6000 (iPhone Thesis)                                                                                                                                                                                    |                        Recycled                        |             100€ SM            |
|           HV          | HV2901  (10.1109/ULTSYM.2015.0517) MAX1771 (Shatin Sharma Thesis)                                                                                                                                                                                                           |                        R05-100B                        |            R05-100B            |
|       Beamformer      | LM96570  (doi:10.3390/jimaging1010193)                                                                                                                                                                                                                                     |                       Pas besoin                       |           Pas besoin           |
|         Pulser        | MAX14808  (10.1109/ULTSYM.2015.0517) MD1213 mosfet driver + TC6320  (Shatin Sharma Thesis) MD1210 + TC2320 (Philippe Levesque - he doesn't recommend) MAX14808  (10.1109/ULTSYM.2014.0399)  MAX4940 over LM96550 (iPhone Thesis) HV7360 (Recommended)                           |                         HV7360                         |               ???              |
|       Protection      | MD0100 (Shatin Sharma Thesis) TX810 (iPhone Thesis)                                                                                                                                                                                                                         |                         MD0100                         |            MD0105 ?            |
|          TGC          | AFE 5808 IC  (doi:10.3390/jimaging1010193) AD9272 (doi:10.1016/j.jestch.2016.01.008) AFE5S0S (10.1109/ULTSYM.2015.0517) LM96511 (iPhone Thesis) AFE5801 (iPhone Thesis) AD605 (Shatin Sharma Thesis) AD8332 (Philippe Levesque)                                                  | AD8331  controlled over Analog Gain or SPI DAC MAX5383 |             AD8331             |
|  Enveloppe detection  | RC (echOpen)                                                                                                                                                                                                                                                               |                         ADL5511                        |       A tester en modules      |
|          ADC          | LTC2245  (Shatin Sharma Thesis) AFE5808 (10.1109/ULTSYM.2014.0399) ADC10040 (Philippe Levesque) AD9236  (Recommended) STM32F334R8 (Recommended, 12bits, 5Msps)                                                                                                                 |              AD9220 + Buffer (74AC541MTC)               | LTC2314-14 pour son aspect SPI |
|   Signal Processing   | Xilinx Kintex-7 FPGA (doi:10.3390/jimaging1010193) Xilinx FPGAs (doi:10.1016/j.jestch.2016.01.008) Spartan6, Xilinx (10.1109/ULTSYM.2015.0517) Spartan 6 LX150 (10.1109/ULTSYM.2014.0399) XC3S1500L-FG320, FPGA Xilinx  (Philippe Levesque) Altera Cyclone III (iPhone Thesis)  |                        BitScope                        |                                |
|        Display        | Raspberry Pi 2 (doi:10.3390/jimaging1010193)                                                                                                                                                                                                                               |                     Linux Computer                     |                                |
|          Cout         | NA                                                                                                                                                                                                                                                                        |                          470 €                         |              250 €             |

## Parts, ICs selection (and critical specs)
 
### HV7360:  High Speed, ±100V 2.5A, Two or Three Level Ultrasound Pulser
* High density integration AC coupled pulser
* 0 to ±100V output voltage
* ±2.5A source and sink minimum pulse current
* Up to 35MHz operating frequency
* 2.0ns matched delay times
* 2.5, 3.3 or 5.0V CMOS logic interface
* Low power consumption and very simple to use

HV7360 is a high voltage, high-speed, pulse generator with built-in, fast return to zero damping FETs. This high voltage and high-speed integrated circuit is designed for portable medical ultrasound image devices, but can also can be used for NDT and test equipment applications.

The HV7360 consists of a controller logic interface circuit, level translators, AC coupled MOSFET gate drivers and high voltage and high current P-channel and N-channel MOSFETs as the output stage. The peak output currents of each channel are guaranteed to be over ±2.5A with up to ±100V of pulse swing. The AC coupling topology for the gate drivers not only saves two floating voltage supplies, it also makes the PCB layout easier.
### Protection: MD0100 Datasheet - HV Protection T/R Switch
* Up to ±100V input voltage protection
* Low on resistance - 15O typical
* Fast switching speed
* Effectively, a simple two terminal device
* No external supplies needed

MD0100 is a high voltage, two terminal, bi-directional, current-limiting protection device. The two terminals are interchangeable. It is designed to protect a low noise receiver from the high voltage transmit pulses in ultrasound applications and is commonly referred to as a T/R (transmit and receive) switch. The MD0100 can be considered as a normally closed switch with a typical switching resistance of 15O that allows small signals to pass.

Once the voltage drop across the two terminals exceeds a nominal value of ±2.0V, the device will start to turn off. In the off state, the MD0100 can withstand up to ±100V across its terminals.

A small amount of current, typical of 200µA, is allowed to flow through.
 
### TGC : AD8331 (Single VGA with Ultralow Noise Preamplifier and Programmable RIN)
* Ultralow noise preamplifier
* 3 dB bandwidth: 120 MHz
* Low power: 125 mW/channel
* Wide gain range with programmable postamp (-4.5 dB to +43.5 dB in LO gain mode, 7.5 dB to 55.5 dB in HI gain mode) – we can use this with the corresponding on-board jumper
* Low output-referred noise: 48 nV/vHz typical
* Active input impedance matching
* Optimized for 10-bit/12-bit ADCs : perfect for us
* Selectable output clamping level
* Single 5 V supply operation : ideal for a 5V board supply!

The AD8331 is a single channel, ultralow noise, linear-in-dB, variable gain amplifier (VGA). Optimized for ultrasound systems, it is usable as a low noise variable gain element at frequencies up to 120 MHz.

Included is an ultralow noise preamplifier (LNA), an X-AMP® VGA with 48 dB of gain range, and a selectable gain postamplifier with adjustable output limiting. The LNA gain is 19 dB with a single-ended input and differential outputs. Using a single resistor, the LNA input impedance can be adjusted to match a signal source without compromising noise performance.

The 48 dB gain range of the VGA makes these devices suitable for a variety of applications. Excellent bandwidth uniformity is maintained across the entire range. The gain control interface provides precise linear-in-dB scaling of 50 dB/V for control voltages between 40 mV and 1 V. Factory trim ensures excellent part-to-part and channel-to-channel gain matching. Differential signal paths result in superb second- and third-order distortion performance and low crosstalk.

### TGC  Control : SPI DAC : MAX5383
Controls the TGC
* 8-Bit Resolution in a Miniature 6-Pin SOT23 Package
* Less than 1µA Shutdown Mode
* Low-Glitch Power-On Reset to Zero DAC Output
* 3-Wire SPI/QSPI/MICROWIRE-Compatible Interface : perfect for a SPI interface
* Low 230µA (max) Supply Current

The MAX5383 low-cost, 8-bit digital-to-analog converters (DACs) in miniature 6-pin SOT23 packages have a simple 3-wire, SPI™/QSPI™/MICROWIRE™-compatible serial interface that operates up to 10MHz. The MAX5383 has an internal +2V reference and operates from a +2.7V to +3.6V supply.

The MAX5383 require an extremely low supply current of only 150µA (typ) and provide a buffered voltage output. These devices power up at zero code and remain there until a new code is written to the DAC registers. This provides additional safety for applications that drive valves or other transducers that need to be off on power-up. The MAX5383 include a 1µA, low-power shutdown mode that features software-selectable output loads of 1kO, 100kO, or 1MO to ground.

### Analog envelop detection: ADL5511 - DC to 6 GHz ENVELOPE AND TruPwr™ RMS Detector
* Envelope tracking RF detector with output proportional to input voltage
* No balun or external tuning required
* Input power dynamic range of 47 dB
* Input frequency range from dc to 6 GHz
* 130 MHz envelope bandwidth
* Envelope delay: 2 ns
* Single-supply operation: 4.75 V to 5.25 V

The ADL5511 is an RF envelope and TruPwr™ rms detector. The envelope output voltage is presented as a voltage that is proportional to the envelope of the input signal. The rms output voltage is independent of the peak-to-average ratio of the input signal.
The rms output is a linear-in-V/V voltage with a conversion gain of 1.9 V/V rms at 900 MHz. The envelope output has a conversion gain of 1.46 V/V at 900 MHz and is referenced to an internal 1.1 V reference voltage, which is available on the EREF pin.
The ADL5511 can operate from dc to 6 GHz on signals with envelope bandwidths up to 130 MHz.

### ADC : AD9220 - Complete 12-Bit, 10.0 MSPS Monolithic A/D Converter
* Monolithic 12-Bit A/D Converter Product Family
* Flexible Sampling Rates: 1.5 MSPS, 3.0 MSPS, and 10 MSPS
* Single +5 V Supply
* Out-of-Range Indicator
* 28-SOIC and 28-SSOP

The AD9221/AD9223/AD9220 combine a low cost, high speed single-CMOS process and a novel architecture to achieve the resolution and speed of existing hybrid and monolithic implementations at a fraction of the power consumption and cost. Each device is a complete, monolithic ADC with an on-chip, high performance, low noise sample-and-hold amplifier and programmable voltage reference. An external reference can also be chosen to suit the dc accuracy and temperature drift requirements of the application. The devices use a multistage differential pipelined architecture with digital output error correction logic to provide 12-bit accuracy at the specified data rates and to guarantee no missing codes over the full operating temperature range.

The input of the AD9221/AD9223/AD9220 is highly flexible, allowing for easy interfacing to imaging, communications, medical, and data-acquisition systems. A truly differential input structure allows for both single-ended and differential input sample-interfaces of varying input spans. The sample-and-hold (SHA) amplifier is equally suited for both multiplexed systems that switch full-scale voltage levels in successive channels as well as sampling single-channel inputs at frequencies up to and beyond the Nyquist rate. Also, the AD9221/AD9223/AD9220 is well suited for communication systems employing IF Down Conversion since the SHA in the differential input mode can achieve excellent dynamic performance far beyond its specified Nyquist frequency2.

A single clock input is used to control all internal conversion The digital output data is presented in straight binary format. An out-of-range (OTR) signal indicates an flow condition which can be used with the most significant bit to determine low or high overflow.
 
### Buffers: 74AC541MTC
* Signal isolation is of high value for measurements at this precision (12bit)

The 74AC541 and 74ACT541 are octal buffer/line drivers designed to be employed as memory and address drivers, clock drivers and bus oriented transmitter/ receivers.
 

# Inspiration from other articles

##  FPGA-Based Portable Ultrasound Scanning System with Automatic Kidney Detection

### Article information
* **Keywords:** learning, fpga, raspberry
* **Uses:** Automatic kidney detection
* **Who:** raji@iith.ac.in (x)
* **Date:** 04/12/2015
* **DOI:** : doi:10.3390/jimaging1010193

### Overall information
*  **Notes:** Awesome work for image segmentation using a Raspberry Pi 2.
*  **Image data**: 22 fps at 480 x 640

### Electronics
* **HV**:  
* **Pulser**:  
* **Beamformer**: LM96570
* **Transducer**:  64-element
* **Protection**:  
* **TGC**:  AFE 5808 IC
* **ADC**:  14bit, 40 MHz
* **DAC**:  
* **Processing**:   Xilinx Kintex-7 FPGA
* **Transfer**:  RS-232 
* **Image processing**:  Raspberry Pi ARM


##  Low Complex, Programmable FPGA based 8-Channel Ultrasound Transmitter for Medical Imaging Researches

### Article information
* **Keywords:**  FPGA, AFE,
* **Uses:**  Prototype
* **Who:**  ee12m1014, raji, sureshpulig@iith.ac.in (x)
* **Date:**  2014
* **DOI:** :  978-1-4799-6644-8/14/$31.00 ©2014 IEEE

### Overall information
*  **Notes:**
*  **Image data**:

### Electronics
* **HV**:  
* **Pulser**:  
* **Beamformer**: LM96570 (single high speed 4-wire serial interface for transmission parameters)
* **Transducer**:  
* **Protection**:  
* **TGC**:  AFE 5809
* **ADC**:  
* **DAC**:  
* **Processing**:  Spartan 3E FPGA
* **Transfer**:  
* **Image processing**:  A Graphical User Interface (GUI) has been developed with National Instruments LabVIEW 2012 in the Microsoft Windows platform. Spartan

##  Microcontroller USB interfacing with MATLAB GUI for low cost medical ultrasound scanners


### Article information
* **Keywords:** microcontroller, matlab
* **Uses:** academics, research 
* **Who:** Jean Rossario Raj - bmz108120@cbme.iitd.ac.in (x)
* **Date:** Accepted 12 January 2016
* **DOI:** : doi:10.1016/j.jestch.2016.01.008


### Overall information
*  **Notes:** This is an open access article under the CC BY-NC-ND license
*  **Image data**:

### Electronics
* **HV**:  
* **Pulser**:  
* **Beamformer**:  
* **Transducer**:  
* **Protection**:  
* **TGC**:  AD9272
* **ADC**:  
* **DAC**:  
* **Processing**:  Xilinx FPGAs
* **Transfer**:  C8051F340
* **Image processing**:  

## Smartphone-based Portable Ultrasound Imaging System : A Primary Result 

### Article information
* **Keywords:**   
* **Uses:**  
* **Who:**    Kyu Cheol Kim
* **Date:**  2013
* **DOI:**   10.1109/ULTSYM.2013.0526

### Overall information
*  **Notes:** Nothing was electronics, all smartphone.  The ultrasound B-mode image reconstructed from the Android smartphone where an 850×800 image is reconstructed and displayed. The total execution time to perform core functional blocks for 128-scanline, 512-sample data is about 520 milliseconds. 
*  **Image data**:   128x512

### Electronics
* **HV**:  
* **Pulser**:  
* **Beamformer**:  
* **Transducer**:   V10, Samsung Medison, Seoul, Korea
* **Protection**:  
* **TGC**:  
* **ADC**:  
* **DAC**:  
* **Processing**:  
* **Transfer**:   
* **Image processing**:  GPU in Samsung’s Galaxy Note II smartphone


##  Smartphone-based  Portable  Ultrasound  Imaging    System: Prototype Implementation and Evaluation 

### Article information
* **Keywords:** smartphone, hardware, software
* **Uses:** Smartphone
* **Who:** Sewoong Ahn
* **Date:** 2015
* **DOI:** : 10.1109/ULTSYM.2015.0517

### Overall information
*  **Notes:** : probe de 180 x 55 x 35mm, 180g
*  **Image data**: 58 fps

### Electronics
* **HV**:  HV2901 (70V-peak voltage)
* **Pulser**:  MAX14808 two 8-channel pulsers
* **Beamformer**: 
* **Transducer**:  128element transducer 16-channel probe system
* **Protection**:  
* **TGC**:  two 8-channel analog front-end chip (AFE5S0S, Texas Instruments, TX, USA) which include low noise amplifiers (LNA) and analog-to-digital converters (ADC).
* **ADC**:  40MHz
* **DAC**:  
* **Processing**:   Spartan6, Xilinx Inc.
* **Transfer**:  USB30l4-BZX -- USB 3.0
* **Image processing**:  Galaxy S5 LTE-A, Samsung., Korea


##  PC-Based Modular Digital US Imaging System


### Article information
* **Keywords:**  
* **Uses:**  
* **Who:** Amr M. Hendy - ahendy@ibetech.com
* **Date:**  
* **DOI:**  

### Overall information
*  **Notes:** Working mostly with Hilbert transforms
*  **Image data**:

### Electronics
* **HV**:  
* **Pulser**:  
* **Beamformer**: LM96570
* **Transducer**:  
* **Protection**:   
* **TGC**:   
* **ADC**:  
* **DAC**:  
* **Processing**:  Virtex-5 FPGA
* **Transfer**:   8-lane PCIe interface	
* **Image processing**:  Pentium 3.0 GHz Core 2 Quad PC with 8 GB memory

## Development of a wide band front end echo sounder receiver circuit

### Article information
* **Keywords:**   
* **Uses:**  Maritime
* **Who:**   Jatin Sharma
* **Date:**   August 2015
* **DOI:**  Department of Physics, University of Oslo

### Overall information
*  **Notes:**
*  **Image data**:  

### Electronics
* **HV**:  MAX1771 
* **Pulser**:  MD1213 mosfet driver (The other similar options were MD1210 and MD1211. But MD1213 was the preferred choice because Bipolar output voltage of 5V can also be achieved with this chip if desired.) + TC6320 mosfet pair
* **Beamformer**:  
* **Transducer**:  FURUNO 520-5PSD  (200kHz) 
* **Protection**:  MD0100. Switch MD0101 is also a good option as it has integrated clamp diodes and therefore no need of external diodes but it is useful when there are more number of channels in the system. Similarly, if voltages greater than §100V are used for transmission, then the switchMD0105 can be used. This switch can be used for protection against voltages up to §130V .
* **TGC**:  Amplifier AD605 is used in this project. AD605 is a low noise, differential-input, dual-channel, linear-in-dB Variable Gain Amplifier. It fulfills the desired characteristics of gain, noise, supply voltage etc. It comprises of two variable gain amplifiers which can be connected in series to get higher gain ranges, up to 96dB and it uses a common gain voltage(VGN) for both the amplifiers to control the variable gain.
* **ADC**:  LTC2245 is a 14-bit, 10Msps ADC. It needs a single 3V Supply making it compatible with the rest of the components.
* **DAC**:  
* **Processing**:  
* **Transfer**:   
* **Image processing**:  

##  A New Smart Probe System for a Tablet PC-based Point-of-Care Ultrasound Imaging System Feasibility Study


### Article information
* **Keywords:**  POCUS, feasibility, tablet
* **Uses:**  POCUS
* **Who:**  Yeongnam Lee
* **Date:** 
* **DOI:** 10.1109/ULTSYM.2014.0399

### Overall information
*  **Notes:** small probe : 73 g, 150 mm x 40 mm x 10 mm, 7W
*  **Image data**: 22 Hz of frame rate  

### Electronics
* **HV**:  
* **Pulser**:  MAX14808 (two 8-channel pulsers with transmit/receive switch)
* **Beamformer**:  
* **Transducer**:  7.5MHz - 16-channel
* **Protection**:  
* **TGC**:  
* **ADC**:  AFE5808 : two analog-to-digital converters 40 MHz
* **DAC**:  
* **Processing**: Spartan 6 LX150 
* **Transfer**:  USB3
* **Image processing**: ATIV Smart PC, Samsung
 


##  Very Fast Scanning Probe for Ophthalmic Use



### Article information
* **Keywords:** ophthalmic
* **Uses:** ophthalmic
* **Who:**  Carotenuto - r.carotenuto@ing.unirc.it
* **Date:**  
* **DOI:** 

### Overall information
*  **Notes:**
*  **Image data**: 256 lines at 25fps

### Electronics
* **HV**:  
* **Pulser**:  
* **Beamformer**: by µC : Scenix SX by Parallax,
* **Transducer**:  PVDF, single, 35MHz
* **Protection**:  
* **TGC**:  
* **ADC**:  
* **DAC**:  
* **Processing**:  
* **Transfer**:  Scenix SX by Parallax
* **Image processing**:  



##  ARCHITECTURE D’UN PROCESSEUR DÉDIÉ AUX TRAITEMENTS DE SIGNAUX ULTRASONIQUES EN TEMPS RÉEL 



### Article information
* **Keywords:** FPGA, mecanique
* **Uses:**  Prototype
* **Who:**  Philippe Levesque
* **Date:**  2011
* **DOI:** 

### Overall information
*  **Notes:**
*  **Image data**: 25 fps 320x240 pixels

### Electronics
* **HV**:  
* **Pulser**:  MD1210 et TC2320
* **Beamformer**: 
* **Transducer**: GP2000 5 MHz, Interson 
* **Protection**:  
* **TGC**:  AD8332
* **ADC**:  ADC10040 - 10 bits, 10Msps
* **DAC**:  10 Msps
* **Processing**: XC3S1500L-FG320, Xilinx  
* **Transfer**:  
* **Image processing**:  


##  A Low Cost Open Source High Frame-Rate High-Frequency Imaging System

### Article information
* **Keywords:** bimorph, OpenHiFUS, ohptalmic
* **Uses:**  ophtalmic
* **Who:** J.A. Brown - j.brown@dal.ca
* **Date:** 
* **DOI:**  

### Overall information
*  **Notes:**
*  **Image data**:

### Electronics
* **HV**:  
* **Pulser**:  
* **Beamformer**: 
* **Transducer**: Daxsonics 45MHz + Arduino Nano 
* **Protection**:  
* **TGC**:  
* **ADC**:  500 MHz 12 bit PCIe digitizer
* **DAC**:  
* **Processing**:  Xilinx, Virtex V,
* **Transfer**:  
* **Image processing**:  


##  iPHONE ULTRASOUND

### Article information
* **Keywords:**  iPHONE, jack
* **Uses:**  
* **Who:**  Jonathan Adam, Adam Keen, Dean Santarinala
* **Date:**  
* **DOI:** Final Report for ECE 445, Senior Design, Spring 2012

### Overall information
*  **Notes:** AFE5801 
*  **Image data**:

### Electronics
* **HV**:  
* **Pulser**:  MAX4940 over LM96550. Our original design employed Texas Instrument’s LM96550 ultrasound transmit pulser. After several failed attempts to achieve correct operation, however, we used Maxim IC’s MAX4940 high-voltage digital pulser instead. The MAX4940’s design includes four channels, as well as positive and negative high-voltage supplies up to +220V and -220V, respectively. Since our application is a one-dimensional scan, only one channel was utilized.
* **Beamformer**:  
* **Transducer**:  DGH 6000 Scanmate A transducer (10.0 MHz). It focuses an acoustic beam at 23.0 mm nominal and has a circular patient contact area 0.275” in diameter.
* **Protection**:  TX810 or LM96530
* **TGC**:  AFE5801, LM96511 more complicated. The AFE5801 includes an 8-channel variable-gain amplifier (VGA) and an 8-channel, 12bit, high-speed analog-to-digital converter (ADC) based on a switched capacitor design.
* **ADC**:  
* **DAC**:  
* **Processing**:  Altera Cyclone III. The Altera Cyclone III is a powerful Field-Programmable Gate Array (FPGA) featuring 10,320 Logic Elements. Its 144 pins are divided into three sections below by function, and the communication protocol with the iPhone is discussed.
* **Transfer**:  
* **Image processing**:  iPhone


##  A Low-Cost B-Mode USB Ultrasound Probe


### Article information
* **Keywords:**  mechanical
* **Uses:**  
* **Who:**  WILLIAM D. RICHARD - wdr@zandrtech.com
* **Date:**  
* **DOI:**  

### Overall information
*  **Notes:**
*  **Image data**: 256x512

### Electronics
* **HV**:  
* **Pulser**:  
* **Beamformer**:  
* **Transducer**:   12.5 MHz ophthalmic probe.
* **Protection**:  
* **TGC**:  
* **ADC**:  
* **DAC**:  
* **Processing**:  Complex Programmable Logic Device (CPLD)
* **Transfer**:  CY7C68014A - a com plete USB 2.0 in ter face, 4 KB of Static RAM (SRAM) for buffering high-speed USB data and an 8051 microprocessor with 16 KB of code/data SRAM all integrated into a single chip. This IC runs embedded 8051 code stored in the I2C Bus Serial PROM (SPROM) or that has been down loaded from the host via a process called ‘ReNumeration.’
* **Image processing**:  



Other 
===

### Links

 * [Murgen  on hackaday](http://hackaday.io/project/9281-murgen) for some news
 * [sci-hub.io](http://sci_hub.io/) for syntax highlighting in output code blocks


# Template


## Name of the article


### Article information
* **Keywords:**   
* **Uses:**  
* **Who:**   
* **Date:**  
* **DOI:**  

### Overall information
*  **Notes:**
*  **Image data**:  

### Electronics
* **HV**:  
* **Pulser**:  
* **Beamformer**:  
* **Transducer**:  
* **Protection**:  
* **TGC**:  
* **ADC**:  
* **DAC**:  
* **Processing**:  
* **Transfer**:   
* **Image processing**:  
