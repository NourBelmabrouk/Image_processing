from faulthandler import disable
from fileinput import filename
from re import T
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from GeoTrans import *
from ImageFiltering import *
from lab1 import calculate_mean_deviation
from lab2 import histogram_equalization
from lab1 import cumulative_histogram
from lab1 import histogram
from lab3 import mean_filter
from lab1 import write_image_pgm
from lab3 import median_filter
from lab3 import add_noise
from lab1 import read_image_pgm
from lab4 import *
import config
import matplotlib.pyplot as plt
import numpy as np


type_image="pgm"
def loadImage():
    global filename
    filename = filedialog.askopenfilename()
    
    try:
        resultaffiche = read_image_pgm(filename)["matrix"]
        img = PIL.Image.fromarray(resultaffiche)
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
        canvas.image = tk_img		# Keep reference to PhotoImage so Python's garbage collector
                                # does not get rid of it making the image dissapear
        config.current_image = img
    except:
        img = PIL.Image.open(filename)
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
        canvas.image = tk_img		# Keep reference to PhotoImage so Python's garbage collector
                                # does not get rid of it making the image dissapear
        config.current_image = img
        global type_image
        type_image = "ppm"




root = Tk()
root.title("TP Traitement")

mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(row=0, column=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

canvas = Canvas(mainframe, width=800, height=600)
canvas.grid(row=0, column=0, rowspan=3)		# put in row 0 col 0 and span 2 rows
canvas.columnconfigure(0, weight=3)

buttons_frame = ttk.Frame(mainframe)
buttons_frame.grid(row=0, column=1, sticky=N)

load_image_button = ttk.Button(buttons_frame, text="Load Image...", command=loadImage)
load_image_button.grid(row=0, column=1, sticky=N+W+E, columnspan=2, pady=10)
#####################
# Save Section #
#####################

i=0
def SaveImage():
    global i
    i+=1
    resultafficheToSave = read_image_pgm(filename)
    write_image_pgm("images/images_results/result_image"+str(i)+".pgm",resultaffiche,resultafficheToSave["line"],resultafficheToSave["column"],resultafficheToSave["lvl_gray"])
    
save_image_button = ttk.Button(buttons_frame, text="save Image...", command=SaveImage)
save_image_button.grid(row=1, column=1, sticky=N+W+E, columnspan=2, pady=10)


#######################
# Add Noise #
#######################
def addNoise():
    global resultaffiche
    resultaffiche = add_noise(filename)
    img = PIL.Image.fromarray(resultaffiche)
    tk_img = ImageTk.PhotoImage(img)
    canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
    canvas.image = tk_img       # Reference for Python's GC
    config.current_image = img      # Keep reference of current image
load_image_button = ttk.Button(buttons_frame, text="Add Noise", command=addNoise)
load_image_button.grid(row=2, column=1, sticky=N+W+E, columnspan=2, pady=10)

#######################
# Median Filtre #
#######################
ttk.Label(buttons_frame, text="Filtering").grid(row=3, column=1, columnspan=2, pady=(0, 8))
ttk.Label(buttons_frame, text="Median").grid(row=4, column=1)
number_median = ttk.Entry(buttons_frame, width=5)
number_median.grid(row=5, column=1)

median_button_x = ttk.Button(buttons_frame, text="apply",
                               command=lambda: addMedianFiltre( int(number_median.get())))
median_button_x.grid(row=5, column=2, sticky=(W, E))
def addMedianFiltre(number=3):
    global resultaffiche
    resultaffiche = median_filter(filename, number)
    img = PIL.Image.fromarray(resultaffiche)
    tk_img = ImageTk.PhotoImage(img)
    canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
    canvas.image = tk_img       # Reference for Python's GC
    config.current_image = img      # Keep reference of current image

#######################
# Mean Filtre #
#######################
ttk.Label(buttons_frame, text="Mean").grid(row=6, column=1)
number_mean = ttk.Entry(buttons_frame, width=5)
number_mean.grid(row=7, column=1)

mean_button_x = ttk.Button(buttons_frame, text="apply",
                               command=lambda: addMeanFiltre( int(number_mean.get())))
mean_button_x.grid(row=7, column=2, sticky=(W, E))
def addMeanFiltre(number=3):
    global resultaffiche
    resultaffiche = mean_filter(filename, number)
    img = PIL.Image.fromarray(resultaffiche)
    tk_img = ImageTk.PhotoImage(img)
    canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
    canvas.image = tk_img       # Reference for Python's GC
    config.current_image = img      # Keep reference of current image

#####################
# Filtering Section #
#####################

ttk.Label(buttons_frame, text="Filtering").grid(row=18, column=1, columnspan=2, pady=(0, 8))

matrix_frame = ttk.Frame(buttons_frame)
matrix_frame.grid(row=19, column=1, columnspan=2)

#########
# ROW 1 #
#########

a11 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a11.grid(row=0, column=0, padx=4, pady=4)

a12 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a12.grid(row=0, column=1, padx=4, pady=4)

a13 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a13.grid(row=0, column=2, padx=4, pady=4)

#########
# ROW 2 #
#########

a21 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a21.grid(row=1, column=0, padx=4, pady=4)

a22 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a22.grid(row=1, column=1, padx=4, pady=4)

a23 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a23.grid(row=1, column=2, padx=4, pady=4)

#########
# ROW 3 #
#########

a31 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a31.grid(row=2, column=0, padx=4, pady=4)

a32 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a32.grid(row=2, column=1, padx=4, pady=4)

a33 = ttk.Entry(matrix_frame, width=3, justify=CENTER)
a33.grid(row=2, column=2, padx=4, pady=4)
if (type_image=="pgm"):
    filter_button = ttk.Button(buttons_frame, text="Filter",
                           command=lambda: filter(canvas, [ [float(a11.get()), float(a12.get()), float(a13.get())],
                                                            [float(a21.get()), float(a22.get()), float(a23.get())],
                                                            [float(a31.get()), float(a32.get()), float(a33.get())] ] ) )
else:
    filter_button = ttk.Button(buttons_frame, text="Filter",
                           command=lambda: filter(canvas, [ [float(a11.get()), float(a12.get()), float(a13.get())],
                                                            [float(a21.get()), float(a22.get()), float(a23.get())],
                                                            [float(a31.get()), float(a32.get()), float(a33.get())] ] ) )
filter_button.grid(row=20, column=1, columnspan=2, sticky=(W, E))
ttk.Label(buttons_frame, text="Filtering").grid(row=18, column=1, columnspan=2, pady=(0, 8))

#####################
# Histogram Section #
#####################
def affichehistorgram():
    resultaffichehistogram = read_image_pgm(filename)
    histogramresultat=histogram(resultaffichehistogram["matrix"],resultaffichehistogram["column"],resultaffichehistogram["line"],resultaffichehistogram["lvl_gray"])
    print(histogramresultat)
    plt.plot(histogramresultat)
    plt.show()
affiche_Histogram_button = ttk.Button(buttons_frame, text="histogram", command=affichehistorgram)
affiche_Histogram_button.grid(row=25, column=1, sticky=N+W+E, columnspan=2, pady=10)


#####################
# Cumulutive Histogram Section #
#####################
def affichecumulutivehistorgram():
    resultaffichecumulitvehistogram = read_image_pgm(filename)
    oldhistogramresultat=histogram(resultaffichecumulitvehistogram["matrix"],resultaffichecumulitvehistogram["column"],resultaffichecumulitvehistogram["line"],resultaffichecumulitvehistogram["lvl_gray"])
    cumultivehistogramresultat=cumulative_histogram(oldhistogramresultat)
    plt.plot(cumultivehistogramresultat)
    plt.show()
affiche_Cumultive_Histogram_button = ttk.Button(buttons_frame, text="Cumulitive histogram", command=affichecumulutivehistorgram)
affiche_Cumultive_Histogram_button.grid(row=27, column=1, sticky=N+W+E, columnspan=2, pady=4)

#####################
# Egalisation Histogram Section #
#####################
def afficheegalistaionhistorgram():
    egalistionhistogramresultat=histogram_equalization(filename)
    plt.plot(egalistionhistogramresultat)
    plt.show()
affiche_Egalisation_Histogram_button = ttk.Button(buttons_frame, text="Egalisation histogram", command=afficheegalistaionhistorgram)
affiche_Egalisation_Histogram_button.grid(row=28, column=1, sticky=N+W+E, columnspan=2, pady=4)


#####################
# MEAN, DEVIATION Section #
#####################
def afficheMeanDeviation():
    imagematrix = read_image_pgm(filename)["matrix"]
    mean,variance =calculate_mean_deviation(imagematrix)
    selection_mean= "Mean is: " + str(mean)
    label_mean.config(text=selection_mean)
    selection_deviation= "Deviation is: " + str(variance)
    label_deviation.config(text=selection_deviation)

label_mean=ttk.Label(buttons_frame, text="Mean is: ")
label_mean.grid(row=33, column=1, columnspan=2, pady=(0, 8))

label_deviation=ttk.Label(buttons_frame,text="Deviation is: ")
label_deviation.grid(row=35, column=1, columnspan=2, pady=(0, 8))   

mean_variance_button = ttk.Button(buttons_frame, text="MEAN DEVIATION", command=afficheMeanDeviation)
mean_variance_button.grid(row=37, column=1, sticky=N+W+E, columnspan=2, pady=4)


matrix_frame = ttk.Frame(buttons_frame)
matrix_frame.grid(row=19, column=1, columnspan=2)
root.mainloop()
