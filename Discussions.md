Discussions.md

Linked with Murgen 1.0 release

# Discussions

The bottleneck may lie in the data transfers...

## Data rates

## Data bus

- 151202: QuadSPI through a dedicated microcontroleur?
- 151201: At 5Msps, 12 bits, shall we use SPI or parallel? 
- 151201: SPI is managed through hardware... parallel, not. Has to be managed from soft. Can be an issue for real time, and to avoid loosing samples.
- 151130: Rather be going onto SPI : QuadSPI? Is that managed by the RPi? Common amongst ADCs ?
- 151207: For high speed data acquisition: about 120Mbits/sec: No SPI port will support such speed…. Only the  Quad version… we can use USB 2.0 HS for such huge movement.  A FPGA or FPGA/RISC MPU combination can be the best  solution. Later, once on RPI, the data can be handled. But for so  perfect measurement of times, and value, only a DSP it’s not enough.  

## Signal detection

- 151129: LTC5507ES6 to filter ? A rajouter!

## ADC and DAC

- 151130: Better ADC at LTC2315-12
- AD7356 (ual, 12-bit, high speed, low power, successive  approximation ADC that operates from a single 2.5 V power  supply and features throughput rates up to 5 MSPS.  
- DAC: a simple DAC i2c 


## Different setups

- 151202: A DSP may be sufficient for our needs: is that the case? 
- 151203: Proposed setup
 - Using a a Main controller - STM32F407 + USB High speed PHY ?? 
 - Analog frontend :  1/4 of AD8264 as LNA and VGA + AD9236 ADC. TGC  can be controlled by internal STM32 DAC - that's max 100-point TGC  calibration curve.  The ADC then could be connected to DCMI interface of  STM32.
 - Transmitter: could be HV Pulser and the TR switch - microchip HV7360 + MD0100,  STHV 748 
- 151209: In  looking at the issue, I think that DSP can be implemented. Of  course,  that comes with the sourcing and a bit of programming, but it  should  work and provide some flexibility. 
- 151112: 
 - it'd be interesting to keep a 100M s/s sampling rate.  
 - wouldn't recommend MD1210 and TC2320 from supertex for the pulse  part. Those have a recovery time that is quite long, and can get easily  damaged - not to mention that they may be obsolete.  
 - Wouldn't recommend two VGAs ... difficult to control, with a high risk of saturation. 


# All-in-one chips (YDO)

## 151201 : Electronics

### AFE (Analog front end)

#### Rationale 

It appears that compoonent MAX2082 from  Maxim's could be a great choice because it integrates everything in one chip (Analog Front End, Pulser, TCG (ou AVG pour eux), T/R Switch, ADC, Filtrage) - maybe better exists ?
Note : Pre-existing chips are 8-channels.
#### Resources
- MAX2082 - Maxim  (Pulser +/- 105 V), TCG (ou VGA) , ADC 50 MSPS and filtering (63$ a piece starting at 1000 units)
https://www.maximintegrated.com/en/products/analog/data-converters/analog-front-end-ics/MAX2082.html
- Several Maxim's Analog Front end  : https://para.maximintegrated.com/en/results.mvp?fam=us_afe
- Pulser - 90 V (16$ a piece starting at 1000 units) : http://www.st.com/web/en/news/n3553d
- A  Texas Instrument Dev Kit : http://www.ti.com/tool/tx-sdk-v1
- Several other Ultrasound Analog Front end (all are 8 channels):  
 - http://www.analog.com/media/en/news-marketing-collateral/product-highlight/AD927x-AD967x-Octal-Ultrasound-AFE-Product-Family.pdf
http://www.analog.com/en/products/landing-pages/001/integrated-afe-contains-8-ultrasound-rcv-channels.html
 - http://www.analog.com/en/products/analog-to-digital-converters/ad-converters/ad9675.html
 - http://www.digikey.com/web%20export/supplier%20content/TI_296/mkt/health/afe5809.pdf?redirected=1
 - http://www.ti.com/product/afe5801
- Ultrasound Receiver module (32 channel) (maybe not so cheap) : http://www.cephasonics.com/product/ultrasound-receiver-modules-csm913233

### Need of a FPGA ?

According to articles and reading, it seems like it will be delicate to proceed without a FPGA for data processing. All "Reference Design" sheets I've read do have a FPGA, or a DSP.... because signals to be processeed are IMHO too fast for a µC.

### Microcontroler

- Microchip - a µC PIC24FJ128GC010 - ADC, 12 bit, 10 MSPS : http://www.microchip.com/wwwproducts/Devices.aspx?product=PIC24FJ128GC010
- and its dev board at 100$: http://www.microchip.com/Developmenttools/ProductDetails.aspx?PartNO=DM240015
- ST ant its ADC 12 bit 5 MSPS  µC STM32F334R8: http://www.st.com/web/en/catalog/mmc/FM141/SC1169/SS1576/LN1531/PF258875#
- with its dev board at 10 € : http://fr.farnell.com/stmicroelectronics/nucleo-f334r8/carte-dev-32-bits-stm32f334r8/dp/2424210
- Analog Device has a reference list µC  : 
http://www.analog.com/en/products/processors-dsp/analog-microcontrollers/8052-core-products.html
- At analog device, the best seems to be ADSP-CM40XF with a 16 bit ADC at 2,3 MSPS: http://www.analog.com/en/products/processors-dsp/cm4xx-mixed-signal-control-processors/adsp-cm403f.html#product-overview  and its 2 dev boards:
 - http://fr.farnell.com/analog-devices/adzs-cm408f-ezlite/kit-d-eval-ez-kit-lite-adsp-cm408f/dp/2367988?CMP=GRHS-1000059
 - http://fr.farnell.com/analog-devices/adzs-cm403f-ezlite/kit-d-eval-ez-kit-lite-adsp-cm403f/dp/2367987?CMP=GRHS-1000059
- I also found some MCU with an internal ADC and a good rate wich seems interesting : http://www.analog.com/en/products/processors-dsp/analog-microcontrollers/8052-core-products.html and http://www.microchip.com/Developmenttools/ProductDetails.aspx?PartNO=DM240015

# Forks

## Constraints

- 151124: The tech milestone was on Nov 24th '15 -  and we need to have something by mid Feb' 16.

## YDO ideas

- 151125: I'm pretty sure that it's impossible that a microcontroler, raspberry or beaglebone can process this data at a speed above 5Msps.  Most of ADCs have a SPI interface, with a 12-bit ADC at 5Msps we'd need a SPI at more than 60Mbps - not everything can do ! In such a case, a DSP or a FPGA is a must-have.

## LJO/FKA cape

- 151124: let's play with the BBB PRU's and develop a analog+ADC cape.

# Bibliography

## FPGA-related bibliography
- Structuring a whole ultrasound system on a board: an excellent thesis from P. Levesques (Kyvox),  File:2011 PhilippeLevesque.pdf. 
- A first corresponding article: File:Real-Time Hand-Held Ultrasound Medical-Imaging Device Based on a New Digital Quadrature Demodulation Processor.pdf
- the second corresponding article: File:Novel Low-Power Ultrasound Digital Preprocessing Architecture for Wireless Display.pdf
- Hardware-Software Partitioning of Digital Signal Processing in Ultrasound Medical Devices a Case Study : File:Hardware-Software Partitioning of US probes.pdf
 - File:A Single FPGA-Based Portable Ultrasound Imaging System for Point-of-Care Applications.pdf
 - File:Low-Cost, High-Speed Back-End Processing System for High-Frequency Ultrasound B-Mode Imaging.pdf
- Extremely interesting too,  iPHONE ULTRASOUND By Jonathan Adam, Adam Keen, Dean Santarinala  and File:project2_presentation.pdf their presentation
## Key general articles (base of inspiration for our dear Emile)
- A single monoelement, low-cost ophtalmic probe using a piezo motor : File:Carotenuto ophtalmic prob.pdf : an excellent article. 
- A single monoelement, low-cost USB probe using a CPLD + microcontroller File:Richard low cost probe.pdf, including a great diagram block of the USB probe 
- Saijo USB work : Development of an ultra-portable echo device connected to USB port : Resource: File:2004 Development of an ultra-portable echo device connected to USB port.pdf
- A Software-Based Ultrasound System for Medical Diagnosis by Samir Ram Thadani File:1997 These MIT Thadani.pdf : an excellent introduction the overall design of a US probe design dating back from 1997. 
- Data processing and transfer in echography : File:Design of an Open-Architecture Ultrasound Acquisition System for Real-Time Processing and Control.pdf
- Transducer parameters: File:A focussed transducer-scatterer model for ultrasonic reference st.pdf

## Other

- Projet étudiant, réalisation d'un échographe de poche pour Iphone (très intéressant et très instructif...) : https://courses.engr.illinois.edu/ece445/getfile.asp?id=5167
- White paper de Xilinx : portable ultrasound system : http://www.xilinx.com/support/documentation/white_papers/wp378-Xilinx-in-Portable-Ultrasound.pdf
- Quelques Notes d'applications intéressantes de chez Maxim's :
https://www.maximintegrated.com/en/app-notes/index.mvp/id/5765
 https://www.maximintegrated.com/en/app-notes/index.mvp/id/5553
- Note d'application de chez ST sur "Ultrasound Imaging" :
 - http://www.st.com/web/en/catalog/apps/SE410/AS430/AC404
 - http://www.st.com/web/en/catalog/apps/SE410/AS430/AC404#
- Pulser TI avec Applcation Note d'une solution complète avec des composants TI :
 - http://www.ti.com.cn/cn/lit/ds/symlink/lm96550.pdf
