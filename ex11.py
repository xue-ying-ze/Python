import tkinter as tk
import tkinter.messagebox # 需要导入弹窗的包
window = tk.Tk()
window.title('my window')
window.geometry('200x200')
"""tk.Label(window, text='1').pack(side='top')#上
tk.Label(window, text='1').pack(side='bottom')#下
tk.Label(window, text='1').pack(side='left')#左
tk.Label(window, text='1').pack(side='right')#右
"""

"""for i in range(4):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)
"""
tk.Label(window, text=1).place(x=20, y=50, anchor='nw')

window.mainloop()
