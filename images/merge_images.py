from PIL import Image
import os

# Have 186 icons of apps. Each is 200 x 200 px
# 
# Want to put them in a grid that will fit on an 8.5 x 11 paper
# Assume that 1/4 inch border so 8 x 10.5 working area
#
# Equations to solve:
# x * y = 186
# y * z = 10
# x * z = 8
#
# Yields: z = 0.67 for a grid of 15 x 12 if you use integers

# Create a blank image. Need to delete collage.jpg if it already exists
# collage = Image.open("collage.jpg")

# Store the names of the files into a long array
# Assumes that:
# a) this script is in the directory with the image files
# b) the image files are the first alphabetical files in the directory
images = [entry for entry in os.listdir(os.getcwd()) if '.png' in entry]

side_length = 200

num_horizontal = 12
num_vertical = 15

collage = Image.new("RGB", (side_length * num_horizontal, side_length * num_vertical))

counter_horizontal = 0
counter_vertical = 0
overall_counter = 0

while counter_horizontal < num_horizontal:
	counter_vertical = 0
	while counter_vertical < num_vertical:
		# Open the image
		image = Image.open(images[overall_counter])
		overall_counter += 1

		# Paste it into the correct location
		x = 0 + counter_horizontal * side_length
		y = 0 + counter_vertical * side_length

		collage.paste(image ,(x, y))

		counter_vertical += 1
		print overall_counter, counter_horizontal, counter_vertical, x, y

	counter_horizontal += 1


# Save the image
collage.save("collage.jpg", quality=95)