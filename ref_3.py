#https://python-forum.io/thread-34864.html
import tkinter as tk
 
class Counter():
    '''Periodically print counter value to stdout'''
    def __init__(self, parent, end, start=0, increment=1, interval=1000):
        self.parent = parent
        self.start_value = start
        self.end_value = end
        self.increment = -increment if (end - start) * increment < 0 else increment
        self.interval = interval
        self.value = start
        self.running = False
 
    def start(self):
        '''Start counter'''
        self.value = self.start_value
        self.running = True
        self.doit()
 
    def stop(self):
        '''Stop counter'''
        self.running = False
 
    def doit(self):
        '''Called periodically to incrementer counter and print value'''
        if self.running:
            print('Counter value =', self.value)
            self.value += self.increment
            self.running = (self.end_value - self.value) * self.increment > 0
            if self.running:
                self.parent.after(self.interval, self.doit)
 
root = tk.Tk()
root.title("Loop Terminate")
counter = Counter(root, 0, 10)
 
# Function button_stop
def button_stop():
    counter.stop()
 
# Function button_start
def button_start():
    counter.start()
 
# Button START
button_start =  tk.Button(root, text = "START", padx=53, pady=20, command=button_start)
button_start.grid(columnspan=1, row=1,column=0)
 
# Button STOP
button_stop =  tk.Button(root, text = "STOP", padx=44, pady=20, command=button_stop)
button_stop.grid(row=2,column=0)
 
root.mainloop()