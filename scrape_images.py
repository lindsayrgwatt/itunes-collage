import urllib
import os

session_history_path = "itunes_images.csv"
session_history = open(session_history_path, "r")

os.chdir('images')

counter = 0
for line in session_history:
	components = line.split(",")
	url = components[0]
	if "icon_100.png" in url:
		url = url.replace("icon_100.png", "icon_200.png")
		print url
		parts = url.split("/")
		name = str(counter) + "_" + parts[len(parts)-1]
		urllib.urlretrieve(url, name)
		counter += 1

