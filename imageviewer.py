#
#               Python-Tkinter - ImageViewer v0.3
#
#   A Simple Python based GUI ImageViewer Application written
#   with Py-Tkinter.
#       This code performs following functions:
#           ->   Navigate Options:
#                   * Next Image
#                   * Previous Image
#           ->   Close Application
#           ->   Status Bar - Image Count.
#
#   Feel free to add more features to the code and create a PR
#   i'm working on adding more features on the next releases.
#
#                   Author : Ravi Kiran
#                   GitHub : iravikiran
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Import all the Libraries.
from tkinter import *
from PIL import ImageTk, Image
import os

# A container for TK.
root = Tk()

# Title of the Application.
root.title("Image Viewer")

# Loading application icon.
ico = PhotoImage(file='ico.png')
root.iconphoto(False, ico)																																																																																																																																																														

# Listing out all the images in 'images' path.
img_path = os.listdir('images')

# Empty list to capture all the images in above path.
image_list = []

# Iterate all the images in the path and append it into the list.
for img in img_path:
	image = os.getcwd() + "/images/" + img
	if os.path.exists(image):
		# Load the image with PhotoImage method
		img = ImageTk.PhotoImage(Image.open(image))
		# Append the loaded image. 
		image_list.append(img)

# Creating a new Label for image.
label = Label(image=image_list[0])
# Grid to display the image.
label.grid(row=0, column=0, columnspan=3)

# Stats bar to display the total images in the UI.
stats = Label(root, text="Showing 1 of {0} Images.".format(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
stats.grid(row=2, column=0, columnspan=3, sticky=W+E)


# Next Navigation function. 
def next(image_num):
	global label
	global button_next
	global button_prev

	# Clean up the order image to display. 
	label.grid_forget()
	label = Label(image=image_list[image_num-1])
	button_next = Button(root, text="Next >>", command=lambda: next(image_num+1), bg="#29ee55")
	button_prev = Button(root, text="<< Prev", command=lambda: prev(image_num-1), bg="#ffd30e")
	
	# Disable nav icon if len of image is equal to total image num.
	if image_num >= len(image_list):
		button_next = Button(root, text="Next >>", state=DISABLED, bg="#9ef0b0")

	# Stats label to display image count.
	stats = Label(root, text="Showing {0} of {1} Images.".format(image_num, len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	stats.grid(row=2, column=0, columnspan=3, sticky=W+E)

	# placing it on the grid to display.
	label.grid(row=0, column=0, columnspan=3)
	button_next.grid(row=1, column=2)
	button_prev.grid(row=1, column=0)


# Previous Navigation function. 
def prev(image_num):
	global label
	global button_next
	global button_prev

	# Clean up the order image to display. 
	label.grid_forget()
	label = Label(image=image_list[image_num-1])
	button_next = Button(root, text="Next >>", command=lambda: next(image_num+1), bg="#29ee55")
	button_prev = Button(root, text="<< Prev", command=lambda: prev(image_num-1), bg="#ffd30e")

	# Disable nav icon if len of image is equal to 1, disables the image icon.
	if image_num == 1:
		button_prev = Button(root, text="<< Prev", state=DISABLED, bg="#f7e9a7")

	# Stats label to display image count.
	stats = Label(root, text="Showing {0} of {1} Images.".format(image_num, len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	stats.grid(row=2, column=0, columnspan=3, sticky=W+E)

	# placing it on the grid to display.
	label.grid(row=0, column=0, columnspan=3)
	button_next.grid(row=1, column=2)
	button_prev.grid(row=1, column=0)

# Button declaration, and the command for each event. 
button_next = Button(root, text="Next >>", command=lambda: next(2), bg="#29ee55")
button_close = Button(root, text="Close", command=root.quit, bg="#f5673d")
button_prev = Button(root, text="<< Prev", command=prev, state=DISABLED, bg="#f7e9a7")

# Placing all the buttons on to the grids with rows & Colums. 
button_next.grid(row=1, column=2, padx=10, pady=10)
button_close.grid(row=1, column=1, padx=10, pady=10)
button_prev.grid(row=1, column=0, padx=10, pady=10)

# Loop GUI. 
root.mainloop()