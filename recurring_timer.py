import time
import tkinter as tk
import threading
from win10toast import ToastNotifier


stop_flag = False
interval_time = 900
init_start=True

def timer_gui(name) -> None:
    def on_change(entry):
        global interval_time
        interval_time = int(entry.widget.get())
        print(entry.widget.get())
    root = tk.Tk()

    def clean_slate() -> None:
        global stop_flag
        stop_flag=True
        root.destroy()
    canvas1 = tk.Canvas(root, width=300, height=300)
    canvas1.pack()

    entry = tk.Entry(root)
    entry.bind("<Return>", on_change)

    button1 = tk.Button(root, text='Exit Application', command=clean_slate)

    widget = tk.Label(canvas1, text='Timer', fg='white', bg='black')
    widget.pack()

    canvas1.create_window(150, 125, window=entry)
    canvas1.create_window(150, 150, window=button1)
    canvas1.create_window(70, 125, window=widget)

    root.mainloop()


def core_logic(name) -> None:
    global stop_flag
    global interval_time
    toaster = ToastNotifier()
    def recursive_timer() -> None:
        global init_start
        if not stop_flag:
            current_time = time.strftime(" %H:%M:%S", time.localtime())
            if init_start:
                toaster.show_toast("Hai Ajay, Startup Protocol Initiated",f"Timer set to {interval_time} seconds")
                init_start=False
            else:
                toaster.show_toast( "Hai Ajay Please Take a Break",f"Time is {current_time}")
            threading.Timer(interval_time, recursive_timer).start()
        else:
            return None
    recursive_timer()


# gui_thread = threading.Thread(target=timer_gui, args=("timer_gui",))
# gui_thread.start()
# gui_thread.join()
core_logic_thread = threading.Thread(target=core_logic, args=("core_logic",))
core_logic_thread.start()
core_logic_thread.join()
