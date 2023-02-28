from tkinter import *
import os
import psutil

class Check():
    '''Periodically print counter value to stdout'''
    def __init__(self, parent, interval=900):
        self.parent = parent
        self.interval = interval
        self.n = 1
        self.running = False
 
    def start(self):
        '''Start running check'''
        self.running = True
        self.doit()
 
    def stop(self):
        '''Stop running check'''
        self.running = False
 
    def doit(self):
        '''Called periodically to incrementer counter and print value'''
        
        if self.running:
            #print('Checking values =', self.value)
            print('Checking values = ' + str(self.n))
            self.n += 1
            #text = psutil.sensors_fans()
            text= psutil.virtual_memory()
            # Display of the result !
            text_Field.delete(0.0, END)
            text_Field.insert(END, text)
          
            if self.running:
                self.parent.after(self.interval, self.doit)

# Function button_stop
def button_stop():
    check.stop()
 
# Function button_start
def button_start():
  
    global interval
    interval = int(spin_interval.get()) *1000    #get the interval value (millisec)
   
    global check
    check = Check(window, interval)
    check.start()

# Designing the GUI using Tkinter
  
window = Tk()

window.title("KK Test Program")
window.geometry("350x350")

ProgName = Label(window,font=('times', 15, 'bold'), text = "This is a test program",fg="red",)
ProgName.grid(row=1, column=1, columnspan=2, padx=40, pady=20)

# Here is where user defines the check interval (secs)

TypeChoice = Label(window, text = "\n Define check interval (secs) :")
TypeChoice.grid(row=2, column=1, columnspan=2, pady=0)

# We use a SpinBox to set a minimum value and a maximum value
spin_interval = Spinbox(window, from_=1, to=360)
spin_interval.grid(row=3, column=1, columnspan=2, pady=9)

# --> Here is where we display the log <--

text_Field = Text(window, height=6, width=20, wrap=WORD)
text_Field.grid(row=4, column=1, columnspan=2, padx=20)
text_Field.insert(END, "\n Generate log ! ")

# Button to run the function

generate_button = Button(window, text="Run", command=button_start)
generate_button.grid(row=5, column=1, padx=10)

# Stop background checking

Exit_button = Button(window, text="End", command=button_stop)
Exit_button.grid(row=5, column=2, pady=10)

#window.mainloop()
