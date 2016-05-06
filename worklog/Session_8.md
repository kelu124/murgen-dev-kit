# Session 8 - 3rd May 2016 - Comparing acquisition speeds

## Previous sessions

- [Session 1](/worklog/Session_1.md) : Powering the board, power use, first (bad) trigging and echoes (06 March 2016)
- [Session 2](/worklog/Session_2.md) : Non-controlled pulsing, inverters, better echoes (11 March 2016)
- [Session 3](/worklog/Session_3.md) : Getting controlled pulsing, but width not controlled (15 March 2016)
- [Session 4](/worklog/Session_4.md) : Width of the pulses is getting controlled =) (19 March 2016)
- [Session 4b](/worklog/Session_4b.md) : Simple data visualisation with BitScope (19 March 2016)
- [Session 5](/worklog/Session_5.md) : moving the transducer to get the first image (20 March 2016)
- [Session 6](/worklog/Session_6.md) : ***Getting a clinically usable image*** (28 March 2016)
- [Session 7](/worklog/Session_7.md) : Getting cleaner images - code improvements  (3 April 2016)
- [Session 8](/worklog/Session_8.md) : Comparing acquisition speeds (3 May 2016)

## Comparing

|Sampling at 5Msps|Sampling at 2.5 Msps|Sampling at 1Msps|
|----|----|----|
|![5Msps](/worklog/Images/Session_8/2c10128b362d2e1652c1b97111ba0ae2.data-DEC1-SC-4T.normalized_zoom.png)|![2.5Msps](/worklog/Images/Session_8/2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T.normalized_zoom.png)|![1Msps](/worklog/Images/Session_8/2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T.normalized_zoom.png)|
| 1 mm is 6.67px | 1mm is 3.33 px| 1mm is 1.33px|

## Step 2

|Type of Sampling|Sampling at 5Msps|Sampling at 2.5 Msps|Sampling at 1Msps|
|---|----|----|----|
|Average|![5Msps](/worklog/Images/Session_8/source_files/normalized/2c10128b362d2e1652c1b97111ba0ae2.data-DEC1-SC-4T.normalized_zoom.png)|![2.5Msps](/worklog/Images/Session_8/source_files/normalized/2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-averaged.normalized_zoom.png)|![1Msps](/worklog/Images/Session_8/source_files/normalized/2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-averaged.normalized_zoom.png)|
|Max|![5Msps](/worklog/Images/Session_8/source_files/normalized/2c10128b362d2e1652c1b97111ba0ae2.data-DEC1-SC-4T.normalized_zoom.png)|![2.5Msps](/worklog/Images/Session_8/source_files/normalized/2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-max.normalized_zoom.png)|![1Msps](/worklog/Images/Session_8/source_files/normalized/2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-max.normalized_zoom.png)|
|Random|![5Msps](/worklog/Images/Session_8/source_files/normalized/2c10128b362d2e1652c1b97111ba0ae2.data-DEC1-SC-4T.normalized_zoom.png)|![2.5Msps](/worklog/Images/Session_8/source_files/normalized/2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-rand.normalized_zoom.png)|![1Msps](/worklog/Images/Session_8/source_files/normalized/2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-rand.normalized_zoom.png)|

## Comparing before Scan conversion

Comparing on the images before scan conversion

![5Msps](/worklog/Images/Session_8/source_files/2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-comparing-raw.png)

Files are at :
* [Averaged](/worklog/Images/Session_8/source_files/2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-averaged.png)
* [Maxed](/worklog/Images/Session_8/source_files/2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-max.png)
* [Rand](/worklog/Images/Session_8/source_files/2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-rand.png)


## Comments

Using the _2c10128b362d2e1652c1b97111ba0ae2.data_ image (in the [examples](/software/examples/) repo).

May look different on different screens.


