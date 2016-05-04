#python CreateSC-4T-5-max.py 2c10128b362d2e1652c1b97111ba0ae2.data
#python CreateSC-4T-5-rand.py 2c10128b362d2e1652c1b97111ba0ae2.data
#python CreateSC-4T-5-averaged.py 2c10128b362d2e1652c1b97111ba0ae2.data
#python CreateSC-4T-2-averaged.py 2c10128b362d2e1652c1b97111ba0ae2.data
#python CreateSC-4T-2-max.py 2c10128b362d2e1652c1b97111ba0ae2.data
#python CreateSC-4T-2-rand.py 2c10128b362d2e1652c1b97111ba0ae2.data

convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-max.png -resize "800x800!" -quality 100 2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-max.normalized.png
convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-rand.png -resize "800x800!" -quality 100 2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-rand.normalized.png
convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-averaged.png -resize "800x800!" -quality 100 2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-averaged.normalized.png

convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-max.png -resize "800x800!" -quality 100 2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-max.normalized.png
convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-rand.png -resize "800x800!" -quality 100 2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-rand.normalized.png
convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-averaged.png -resize "800x800!" -quality 100 2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-averaged.normalized.png

convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC1-SC-4T.png -resize "800x800!" -quality 100 2c10128b362d2e1652c1b97111ba0ae2.data-DEC1-SC-4T.normalized.png

convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-rand.normalized.png -gravity Center -extent 400x400 2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-rand.normalized_zoom.png
convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-max.normalized.png -gravity Center -extent 400x400 2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-max.normalized_zoom.png
convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-averaged.normalized.png -gravity Center -extent 400x400 2c10128b362d2e1652c1b97111ba0ae2.data-DEC2-SC-4T-averaged.normalized_zoom.png

convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-rand.normalized.png -gravity Center -extent 400x400 2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-rand.normalized_zoom.png
convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-max.normalized.png -gravity Center -extent 400x400 2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-max.normalized_zoom.png
convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-averaged.normalized.png -gravity Center -extent 400x400 2c10128b362d2e1652c1b97111ba0ae2.data-DEC5-SC-4T-averaged.normalized_zoom.png

convert 2c10128b362d2e1652c1b97111ba0ae2.data-DEC1-SC-4T.normalized.png -gravity Center -extent 400x400 2c10128b362d2e1652c1b97111ba0ae2.data-DEC1-SC-4T.normalized_zoom.png

mv *.normalized_zoom.png normalized/
rm *.normalized.png


