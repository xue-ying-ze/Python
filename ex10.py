import tkinter as tk
import tkinter.messagebox # 需要导入弹窗的包
window = tk.Tk()
window.title('my window')
window.geometry('200x200')


def hit_me():
    #tk.messagebox.showinfo(title='Hi', message='f**k you')  # 提示信息对话窗
     tk.messagebox.showwarning(title='')  # 提出警告对话窗
    # tk.messagebox.showerror()  # 提出错误对话窗
    # tk.messagebox.askquestion()  # 询问选择对话窗
    # print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))
    # print(tk.messagebox.askquestion())#返回yes和no
    # print(tk.messagebox.askokcancel())#返回true和false
    # print(tk.messagebox.askyesno())#返回true和false
    # print(tk.messagebox.askretrycancel())#返回true和false


tk.Button(window, text='hit me', command=hit_me).pack()


window.mainloop()
