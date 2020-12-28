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


from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

root.title("Image Viewer")

ico = PhotoImage(file='ico.png')
root.iconphoto(False, ico)																																																																																																																																																														

img_path = os.listdir('images')

image_list = []

for img in img_path:
	image = os.getcwd() + "/images/" + img
	if os.path.exists(image):
		img = ImageTk.PhotoImage(Image.open(image))
		image_list.append(img)

label = Label(image=image_list[0])
label.grid(row=0, column=0, columnspan=3)

stats = Label(root, text="Showing 1 of {0} Images.".format(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
stats.grid(row=2, column=0, columnspan=3, sticky=W+E)


def next(image_num):
	global label
	global button_next
	global button_prev

	label.grid_forget()
	label = Label(image=image_list[image_num-1])
	button_next = Button(root, text="Next >>", command=lambda: next(image_num+1), bg="#29ee55")
	button_prev = Button(root, text="<< Prev", command=lambda: prev(image_num-1), bg="#ffd30e")
	
	if image_num >= len(image_list):
		button_next = Button(root, text="Next >>", state=DISABLED, bg="#9ef0b0")

	stats = Label(root, text="Showing {0} of {1} Images.".format(image_num, len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	stats.grid(row=2, column=0, columnspan=3, sticky=W+E)


	label.grid(row=0, column=0, columnspan=3)
	button_next.grid(row=1, column=2)
	button_prev.grid(row=1, column=0)


def prev(image_num):
	global label
	global button_next
	global button_prev

	label.grid_forget()
	label = Label(image=image_list[image_num-1])
	button_next = Button(root, text="Next >>", command=lambda: next(image_num+1), bg="#29ee55")
	button_prev = Button(root, text="<< Prev", command=lambda: prev(image_num-1), bg="#ffd30e")

	if image_num == 1:
		button_prev = Button(root, text="<< Prev", state=DISABLED, bg="#f7e9a7")

	stats = Label(root, text="Showing {0} of {1} Images.".format(image_num, len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	stats.grid(row=2, column=0, columnspan=3, sticky=W+E)

	label.grid(row=0, column=0, columnspan=3)
	button_next.grid(row=1, column=2)
	button_prev.grid(row=1, column=0)


button_next = Button(root, text="Next >>", command=lambda: next(2), bg="#29ee55")
button_close = Button(root, text="Close", command=root.quit, bg="#f5673d")
button_prev = Button(root, text="<< Prev", command=prev, state=DISABLED, bg="#f7e9a7")

button_next.grid(row=1, column=2, padx=10, pady=10)
button_close.grid(row=1, column=1, padx=10, pady=10)
button_prev.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()