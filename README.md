itunes-collage
==============

I had to create a flyer for the [Seattle Coderdojo](http://www.seattlecoderdojo.com) and wanted a backdrop of the most popular apps.

It's a pretty straightforward process. You can skip 1 & 2 as I've included sample data in the repo:

1. (Optional) Download [Charles](http://www.charlesproxy.com/)

2. (Optional) Open up iTunes and use Charles to record while you open up the most popular apps. Make sure to scroll to the bottom of the list so that all the images load.

3. Export the session as a .csv. I called mine the cryptic ```itunes_images.csv```

4. Run the Python script ```scrape_images.py``` to download the images

5. Run the Python script ```merge_images.py``` (in the images directory) to create the collage

Here's what the final image looks like:

![Image](https://github.com/lindsayrgwatt/itunes-collage/blob/master/images/collage.jpg?raw=true)
