import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('200x200')
tk.Label(window, text='on the window', bg='yellow').pack()

frm = tk.Frame(window)
frm.pack()
frm_l = tk.Frame(frm,)
frm_r = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')
tk.Label(frm_l, text='on the frm_l1').pack()##这个`label`长在`frm_l`上，显示为`on the frm_l1`
tk.Label(frm_l, text='on the frm_l2').pack()##这个`label`长在`frm_l`上，显示为`on the frm_l2`
tk.Label(frm_r, text='on the frm_r1').pack()##这个`label`长在`frm_r`上，显示为`on the frm_r1`
window.mainloop()
