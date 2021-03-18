# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('200x200')
var = tk.StringVar()
l_1 = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)
l_1.pack()
hit_flag = False

a = 10
def hit_callback():
    global hit_flag
    if hit_flag:
        var.set('')
        hit_flag = False
    else:
        var.set('you hit me')
        hit_flag = True


b = tk.Button(window, text='hit me', width=15, height=2, command=hit_callback)
b.pack()

window.mainloop()
