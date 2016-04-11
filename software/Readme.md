# Software Readme

## Contents of the folder 

### Some files

* All example files are compressed and thumbs created in [the example folder](/software/examples/Readme.md)
* For the convention in files format, [the data files specs are in](/software/examples/Specs.md)

### Some software

* AcquireImage.py acquires the images, stores them in pairs of log files
* CreateImage.py creates the .data file from the log files
* CreateSC.py creates the .png files (Scan Conversion) using a nearest neighbour algorithm, from the .data files
* CreateSC-4T.py creates the .png files (Scan Conversion) using the 4 nearest neighbours to determine the pixel value, from the .data files
* TrinketProCode is the code for the Arduino Trinket Pro.
* BatchImage is a shell script to automate the creation of images properly

### Some files
* The examples.tar.bz2 contains quite a lot of raw images, to be processed by CreateImage.py . There should be around 200Mo of raw images packed in this 4Mo archive.
* The [examples](/software/examples/) repository, and its [Readme](/software/examples/Readme.md),  contains some raw images, along with a table, and the [Specs](/software/examples/Specs.md)) for the data format.

# Installing BitScope

## Setting up bitscope tools for Ubuntu, using BS05 (Bitscope Micro)	

1. Installation : install all deb/ .deb files (dpkg -i install_files/*.deb), starting with bitscope-link.
2. Follow the https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=122636 instructions

```
 $ sudo unzip python-bindings-2.0-DC01L.zip -d /usr/share/doc/bitscope-library/examples/python/
 $ cd /usr/share/doc/bitscope-library/examples/python/
 $ cd /usr/share/doc/bitscope-library/examples/python/python-bindings-2.0-DC01L/
 $ sudo python setup-bitlib.py install
```
Compilation fails? To do that we discover that we should do this:
```
 $ sudo BASECFLAGS="" OPT="" CFLAGS="-O3" python setup-bitlib.py install
```
This should work and you should see:
```
 $ python test-bitlib.py 
 Starting: Attempting to open one device...
  Library: 2.0 FE26B (Python DC01L)
     Link: USB:/dev/ttyUSB0
 BitScope: BS000501 (YK26VX18)
 Channels: 10 (2 analog + 8 logic)
    Modes: FAST DUAL MIXED LOGIC STREAM
  Capture: 12288 @ 40000000Hz = 0.000307s (LOGIC)
   Offset: +2.917V to -6.217V
      POD:  9.20V  5.20V  3.50V  1.10V
  Data(5): 1.725000, 1.725000, 1.760937, 1.760937, 1.725000
 Finished: Library closed, resources released.
```

