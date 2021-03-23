import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('200x200')
var1 = tk.StringVar()
l1 = tk.Label(window, bg='lightblue', width=20, text='empty')
l1.pack()


def print_selection(v):
    l1.config(text='you have selected ' + v)


s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()
window.mainloop()
