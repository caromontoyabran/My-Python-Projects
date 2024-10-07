import pytz # this is a library for time zone handling
from datetime import datetime #from datatime module, import the datetime class
from tkinter import *  # Importing everything from tkinter for GUI
import tkinter as tk  # Importing tkinter under the alias tk
from tkinter import ttk  # Importing ttk for modern "themed" widgets of tkinter


class RealTimeZoneConverter:
  def __init__(self):
    self.timezones = pytz.all_timezones # Getting the list of all available time zones

  def convert(self, from_timezone, to_timezone):
    # Getting the timezone info for both paramethers
    from_tz = pytz.timezone(from_timezone)
    to_tz = pytz.timezone(to_timezone)

    # Getting the current time in the "from_timezone" and converting it to "to_timezone"
    from_time = datetime.now(from_tz)
    to_time = from_time.astimezone(to_tz)

    return from_time.strftime("%H:%M"), to_time.strftime("%H:%M")
    
class App(tk.Tk): 
  # Initializing the tkinter window
  def __init__(self, converter):
    tk.Tk.__init__(self)
    self.title = "Time Zone Converter"
    self.timezone_converter = converter

    self.geometry("500x200")
    self.configure(bg="#FFE873")

    # Label - Welcome message for the user
    self.intro_label = Label(
      self,
      text="Welcome to Real Time Zone Converter",
      fg="red",
      relief=tk.RAISED,
      borderwidth=3
    )
    self.intro_label.config(font=("Courier",15, "bold"))
    self.intro_label.place(x=10, y=5)

    # Entry box - This will restrict input to numbers and text for time zones
    self.amount_field = Entry(
      self,
      bd=3,
      relief=tk.RIDGE,
      justify=tk.CENTER,
    )
    self.converted_amount_field_label = Label(
      self,
      text="",
      fg="black",
      bg="white",
      relief=tk.RIDGE,
      justify=tk.CENTER,
      width=25,
      borderwidth=3
        )
    
    # Dropdown menu for selecting the "from" time zone
    self.from_timezone_variable = StringVar(self)
    self.from_timezone_variable.set("UTC")  # Setting default value for 'from' time zone
    self.to_timezone_variable = StringVar(self)
    self.to_timezone_variable.set("US/Pacific")  # Setting default value for 'to' time zone

    font = ("Courier", 12, "bold")  # Setting font style for dropdown
    self.option_add("*TCombobox*Listbox.font", font)

    # Dropdown for selecting the "from" time zone
    self.from_timezone_dropdown = ttk.Combobox(
      self,
      textvariable=self.from_timezone_variable,
      values=list(self.timezone_converter.timezones),  # Populating dropdown with all time zones
      font=font,
      state="readonly",  # Making the dropdown read-only
      width=25,
      justify=tk.CENTER
        ) 
        
    # Dropdown for selecting the "to" time zone
    self.to_timezone_dropdown = ttk.Combobox(
      self,
      textvariable=self.to_timezone_variable,
      values=list(self.timezone_converter.timezones),  # Populating dropdown with all time zones
      font=font,
      state="readonly",  # Making the dropdown read-only
      width=25,
      justify=tk.CENTER
        )
    
    # Placing the dropdowns and entry fields in the window
    self.from_timezone_dropdown.place(x=30, y=50)
    self.to_timezone_dropdown.place(x=280, y=50)
    self.converted_amount_field_label.place(x=180, y=100)  

    # Convert button
    self.convert_button = Button(
      self,
      text="Convert",
      fg="black",
      command=self.perform  # When clicked, it will call the 'perform' method
        )
    self.convert_button.config(font=("Courier", 10, "bold"))  # Configuring the font style
    self.convert_button.place(x=220, y=150)  # Placing the button in the window

  def perform(self):
    # Retrieving the time zone values from the dropdowns
    from_tz = self.from_timezone_variable.get()
    to_tz = self.to_timezone_variable.get()

    # Calling the converter method and getting the converted times
    from_time, to_time = self.timezone_converter.convert(from_tz, to_tz)

    # Displaying the converted time in the label
    self.converted_amount_field_label.config(text=f"From: {from_time}\nTo: {to_time}")

if __name__ == "__main__":
  # Creating an instance of the converter
  converter = RealTimeZoneConverter()

  # Creating an instance of the app
  App(converter)  

  # Running the tkinter main loop
  mainloop()