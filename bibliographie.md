# Our setup

For details, read the bibliography below =)

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

 * [echOpen](http://echopen.org) for the framework of the project
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
