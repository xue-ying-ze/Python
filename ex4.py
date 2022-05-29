import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('200x200')
var1 = tk.StringVar()
l1 = tk.Label(window, bg='lightblue', width=20, text='empty')
l1.pack()


def print_selection():
    l1.config(text='you have selected ' + var1.get())


r1 = tk.Radiobutton(window, text='Option A', variable=var1, value='A', command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window, text='Option B', variable=var1, value='B', command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window, text='Option C', variable=var1, value='C', command=print_selection)
r3.pack()

window.mainloop()
