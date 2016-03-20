'''report.py -- BitLib 2.0 Capture Device Report Generator (Python)'''

from bitlib import *
import datetime
import time

MY_DEVICE = 0 # one open device only
MY_CHANNEL_TRIG = 0 # channel to trig on (chan A)
MY_CHANNEL = 1 # channel to capture and display (0 for Chan A, 1 for Chan B)
MY_PROBE_FILE = "" # default probe file if unspecified
MY_MODE = BL_MODE_FAST # preferred trace mode
MY_RATE = 20000000 # default sample rate we'll use for capture.
MY_SIZE = 8400 # number of samples we'll capture (3 periods to test -- 300us+120us * 20MHz)
MY_SIZE_TRIG = 1 # number of samples we'll capture (3 periods to test -- 300us * 20MHz * 3)
TRUE = 1

MODES = ("FAST","DUAL","MIXED","LOGIC","STREAM")
SOURCES = ("POD","BNC","X10","X20","X50","ALT","GND")



def main(argv=None):
    #
    # Open the first device found (only)
    #
    print "\nStarting: Attempting to open one device..."
    if BL_Open(MY_PROBE_FILE,1):
        #
        # Open succeeded (report versions).
        #
        print " Library: %s (%s)" % (
            BL_Version(BL_VERSION_LIBRARY),
            BL_Version(BL_VERSION_BINDING))
        #
        # Select this device (optional, it's already selected).
        #
        BL_Select(BL_SELECT_DEVICE,MY_DEVICE)
        #
        # Report the link, device and channel information.
        #
        print "    Link: %s" % BL_Name(0)
        print "BitScope: %s (%s)" % (BL_Version(BL_VERSION_DEVICE),BL_ID())
        print "Channels: %d (%d analog + %d logic)" % (
            BL_Count(BL_COUNT_ANALOG)+BL_Count(BL_COUNT_LOGIC),
            BL_Count(BL_COUNT_ANALOG),BL_Count(BL_COUNT_LOGIC))
        #
        # Determine which modes the device supports.
        #
        print "   Modes:" + "".join(["%s" % (
            (" " + MODES[i]) if i == BL_Mode(i) else "") for i in range(len(MODES))])
        #
        # Report canonic capture specification in LOGIC (if supported) or FAST mode (otherwise.
        # BL_Mode(BL_MODE_LOGIC) == BL_MODE_LOGIC or 
        BL_Mode(BL_MODE_FAST)
        print " Capture: %d @ %.0fHz = %fs (%s)" % (
            BL_Size(),BL_Rate(),
            BL_Time(),MODES[BL_Mode()])
        #
        # Report the maximum offset range (if the device supports offsets).
        #
        BL_Range(BL_Count(BL_COUNT_RANGE));
        if BL_Offset(-1000) != BL_Offset(1000):
            print "  Offset: %+.4gV to %+.4gV" % (
                BL_Offset(1000), BL_Offset(-1000))
        #
        # Report the input source provided by the device and their respective ranges.
        #
        for i in range(len(SOURCES)):
            if i == BL_Select(2,i):
                print "     %s: " % SOURCES[i] + " ".join(["%5.2fV" % BL_Range(n) for n in range(BL_Count(3)-1,-1,-1)])
        #
        # Set up to capture MY_SIZE samples at MY_RATE from CH-A via the POD input using the highest range.
        #
        BL_Mode(MY_MODE) # prefered trace mode
        BL_Intro(BL_ZERO); # optional, default BL_ZERO
        BL_Delay(BL_ZERO); # optional, default BL_ZERO
        BL_Rate(MY_RATE); # optional, default BL_MAX_RATE
        BL_Size(MY_SIZE); # optional default BL_MAX_SIZE
        BL_Select(BL_SELECT_CHANNEL,MY_CHANNEL); # choose the channel
        BL_Trigger(BL_ZERO,BL_TRIG_RISE); # optional when untriggered */
        BL_Select(BL_SELECT_SOURCE,BL_SOURCE_POD); # use the POD input */
        BL_Range(BL_Count(BL_COUNT_RANGE)); # maximum range
        BL_Offset(BL_ZERO); # optional, default 0

        BL_Enable(TRUE); # at least one channel must be initialised
        #
        # Perform an (untriggered) trace (this is the actual data capture).
        #
        BL_Trace()
        #
        # Acquire (i.e. upload) the captured data (which may be less than MY_SIZE!).
        #
        DATA = BL_Acquire()
	
        #print " Data(%d): " % MY_SIZE + ", ".join(["%f" % DATA[n] for n in range(len(DATA))])
        #print "Complete: trace and acquisition complete. Dump the log...\n"
        #print "%s" % BL_Log()

	
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d-%H%M%S')
	st = "/home/luc/"+st + "_bitscope-DATA.log"
	targetFile = open(st, 'w')

	##On cree le fichier de debug
	for x in range(len(DATA)):
		targetFile.write(str(DATA[x])+"\n")
	targetFile.close();
        #
        # Close the library to release resources (we're done).
        #
        print "Finished: close the library to release resources."
        BL_Close()
    else:
        print "  FAILED: device not found (check your probe file)."

if __name__ == "__main__":
    import sys
    sys.exit(main())
