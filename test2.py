import tkinter.messagebox
import tkinter as tk

window = tk.Tk()
window.title('menu')
window.geometry('400x400')


def hit():
    # box系列
    # tk.messagebox.showinfo(title='hi',message='so this is a msgbox')
    # tk.messagebox.showwarning(title='warning', message='so this is a warningbox')
    # tk.messagebox.showerror(title='hi', message='No! the program is about to crash!')

    # ask系列
    tk.messagebox.askquestion(title='hi', message='Are you sure to cancel it?') #返回'yes'或'no'
    # tk.messagebox.askyesno(title='hi', message='Are you sure to cancel it?')  #返回True或者False
    # tk.messagebox.askquestion(title='hi', message='Are you sure to cancel it?')  #



b = tk.Button(window, text='there will be a msgbox', command=hit).pack()

tk.mainloop()
