import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('200x200')
var1 = tk.StringVar()
l1 = tk.Label(window, bg='lightblue', width=4, textvariable=var1)
l1.pack()


"""def print_selection():
    #value = lb.get(lb.curselection())
    value = len(lb.curselection())
    var1.set(value)
"""

#b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1 = tk.Button(window, text='print selection', width=15, height=2)
b1.pack()

var2 = tk.StringVar()
text = [11, 22, 33, 44]
var2.set(text)
lb = tk.Listbox(window, listvariable=var2)
list_items = [1, 2, 3, 4]
for items in list_items:
    lb.insert('end', items)
lb.insert(2, 'sec')
lb.pack()


def onselect(evt):
    w = evt.widget
    value = w.get(w.curselection())
    var1.set(value)


lb.bind('<<ListboxSelect>>', onselect)

window.mainloop()
