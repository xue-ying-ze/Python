import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('200x200')
var1 = tk.IntVar()
var2 = tk.IntVar()
l1 = tk.Label(window, bg='lightblue', width=20, text='empty')
l1.grid(row=0)


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):   # 如果选中第一个选项，未选中第二个选项
        l1.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1): # 如果选中第二个选项，未选中第一个选项
        l1.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):  # 如果两个选项都未选中
        l1.config(text='I do not love either')
    else:
        l1.config(text='I love both')             # 如果两个选项都选中


c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=print_selection)
c1.grid(row=1, sticky=tk.W)
c2.grid(row=2, sticky=tk.W)
window.mainloop()
