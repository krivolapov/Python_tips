from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Calculator")

def calk(key):
    global memory
    if key == "=":
        strl = "-+0123456789.*/"
        if calc_entry.get()[0] not in strl:
            calc_entry.insert(END, "Not a number!")
            messagebox.showerror("Error, It's not a number")

btn_list = [
    "7", "8", "9","+","-",
    "4","5","6","*","/",
    "1","2","3","-/+","=",
    "0",".","C","",""
]

r = 1
c = 0

for i in btn_list:
    rel = ""
    ttk.Button(root, text = i, command = cmd).grid(row = r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

root.mainloop()
