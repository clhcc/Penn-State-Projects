# This program calculates the windchill in a GUI form.

# Author: Linhan Cai

import tkinter

class WindchillCalculatorGUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title = ('Windchill Calculator')

        # Create five frames to group widgets.
        self.frame1 = tkinter.Frame()
        self.frame2 = tkinter.Frame()
        self.frame3 = tkinter.Frame()
        self.frame4 = tkinter.Frame()
        self.frame5 = tkinter.Frame()

        # Create the widgets for the frame1.
        self.titleLabel = tkinter.Label(self.frame1, \
                    text='Windchill Calculator',
                    bg = 'yellow',
                    fg = 'red',
                    font = ('verdana', 12))
        
        # Pack the frame1's widgets.
        self.titleLabel.pack()

        # Create the widgets for the frame2.
        self.prompt_label1 = tkinter.Label(self.frame2, \
                    text='Enter the temperature in degrees Fahrenheit:')
        self.temp_entry = tkinter.Entry(self.frame2, \
                                        width=10)
        # Pack the frame2's widgets.
        self.prompt_label1.pack(side='left')
        self.temp_entry.pack(side='left')
    
        # Create the widgets for frame3.
        self.prompt_label2 = tkinter.Label(self.frame3, \
                    text='Enter the wind speed in mph:')
        self.speed_entry = tkinter.Entry(self.frame3, \
                                        width=10)
        # Pack the frame3's widgets.
        self.prompt_label2.pack(side='left')
        self.speed_entry.pack(side='left')

        # Create the button widgets for frame4.
        self.calc_button = tkinter.Button(self.frame4, \
                                     text='Calculate Windchill', \
                                     command=self.calculate_windchill)

        # Pack the button.
        self.calc_button.pack(side='left')

         # Create the widgets for frame5.
        self.descr_label1 = tkinter.Label(self.frame5, \
                                 text='The windchill temperature is:')
        self.descr_label2 = tkinter.Label(self.frame5, \
                                 text='degrees fahrenheit.')

        # We need a StringVar object to associate with
        # an output label. Use the object's set method
        # to store a string of blank characters.
        self.value = tkinter.StringVar()

        # Create a label and associate it with the
        # StringVar object. Any value stored in the
        # StringVar object will automatically be displayed
        # in the label.
        self.windchill_label = tkinter.Label(self.frame5, \
                                    textvariable=self.value)

        # Pack the frame5's widgets.
        self.descr_label1.pack(side='left')
        self.windchill_label.pack(side='left')
        self.descr_label2.pack(side='left')

        # Pack the frames.
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The convert method is a callback function for
    # the Calculate button.
    
    def calculate_windchill(self):
        # Get the value entered by the user into the
        # temp_entry widget.
        temp = float(self.temp_entry.get())

        # speed_entry widget.
        speed = float(self.speed_entry.get())

        # Calculate the windchill.
        windchill = 35.74 + 0.6215 * temp - 35.75 * speed**0.16 + 0.4275 * temp * speed**0.16

        # Calculate the windchill to a string and store it
        # in the StringVar object. This will automatically
        # update the windchill_label widget.
        self.value.set(format(windchill, '.1f'))

# Create an instance of the KiloConverterGUI class.
wind_cal = WindchillCalculatorGUI()
