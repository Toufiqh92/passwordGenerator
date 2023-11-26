
import random
import string
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()

# Set the window size
root.geometry('600x400')

# Define the special characters for the password
special_letters = "!-/"
# Define the Password class
class Password:
    def __init__(self, length=12):
        self.length = length

    # Generate a random password
    def generate(self):
        characters = ''.join(random.choice(special_letters+ string.ascii_lowercase + special_letters+ string.ascii_uppercase + string.digits+ special_letters )for i in range(self.length))
        return characters
   
# Define the function to show the password
def showPass():
    # Create a Password object with a length of 12
    passw = Password()

    # Generate the password and display it
    passhow.config(text="Here is your Password: " + passw.generate())

# Create a frame for the interface
frm = ttk.Frame(root, padding=30)
frm.grid()

# Create a button to generate the password
ttk.Button(frm, text="Generate Password",command=showPass).grid(column=10, row=4)

# Create a label to display the password
passhow = ttk.Label(frm, text = "Here is your Password: ")
passhow.grid(column=10, row=2)
passhow.config(font=("Ariel", 20   ))

# Start the main event loop
root.mainloop()
#
