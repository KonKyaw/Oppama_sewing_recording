import threading
from tkinter import*
root = Tk()

def real_loop():
    while True:
        with superman_lock:
            if not superman:
                return
       print("It's doing something")
def loop():
    global superman
    global superman_lock
    superman=False
    superman_lock = threading.Lock()
    thread = threading.Thread(target=real_loop, daemon=True)
def endloop():
    global superman
    with superman_lock:
        superman=True

btn_1 = Button(root, text="stop", command=endloop)
btn_1.pack()
btn_2 = Button(root, text="start", command=loop)
btn_2.pack()