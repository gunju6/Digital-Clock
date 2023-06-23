# importing whole module
from tkinter import *
from tkinter.ttk import *
 
# importing strftime function to
# retrieve system's time
from time import strftime
 
# creating tkinter window
root = Tk()
root.title('Digital Clock')

 
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
 
lbl = Label(root, font=('Algerian', 50, 'bold'),
            background='pink',
            foreground='black')
 
lbl.pack(anchor='center')
time()
 
mainloop()