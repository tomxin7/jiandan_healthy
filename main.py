import tkinter as tk
from tkinter import *
import time
import tkinter.messagebox
import _thread


global rest
global rest_flag
rest_flag = 10000000

def message(threadName, delay):
    global rest_flag
    tk.messagebox.showinfo(title='休息提醒', message='你已经工作了' + str(rest_flag) + "分钟啦，快起来走走吧~~")
    rest_flag = rest_flag + 10


class StopWatch(Frame):
    '''实现一个秒表部件'''
    msec=50
    def __init__(self,parent=None,**kw):
        Frame.__init__(self,parent,kw)
        self._start = 0.0
        self._elapsedtime =0.0
        self._running = False
        self.timestr = StringVar()
        self.makeWidgets()
    def makeWidgets(self):
        '''制作时间标签'''
        l = Entry(self,textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X,expand=NO,pady=2,padx=2)
    def _update(self):
        '''用逝去的时间更新标签'''
        self._elapsedtime=time.time() - self._start
        self._setTime(self._elapsedtime)
        self.timer = self.after(self.msec,self._update)
    def _setTime(self,elap):
        '''将时间格式改为分：秒：百分秒'''
        minutes = int(elap/60)
        global rest
        global rest_flag
        if int(elap) == rest_flag*60:
            _thread.start_new_thread(message, ("Thread-1", 2, ))
            time.sleep(1)
        seconds = int(elap-minutes*60.0)
        hour = int(minutes/60)
        self.timestr.set('%02d:%02d:%02d'%(hour,minutes,seconds))
    def Start(self):
        result = tk.StringVar()
        result.set("工作中")
        entry_result = tk.Label(window, textvariable=result, fg="blue")
        entry_result.place(x=310, y=50)
        '''开始秒表'''
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = True
    def Stop(self):
        global rest
        global rest_flag
        rest_flag=rest
        result = tk.StringVar()
        result.set("休息中")
        entry_result = tk.Label(window, textvariable=result, fg="red")
        entry_result.place(x=310, y=50)
        '''停止秒表'''
        if self._running:
            self.after_cancel(self.timer)
            self._elapsedtime = 0.0
            self._setTime(self._elapsedtime)
            self._running = False
    def Reset(self):
        '''重设秒表'''
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)
        self._running = False


window = tk.Tk()
window.title('简单健康小助手')
# window.geometry('400x250')
sw = window.winfo_screenwidth()
#得到屏幕宽度
sh = window.winfo_screenheight()
#得到屏幕高度
ww = 400
wh = 250
#窗口宽高为100
x = (sw-ww) / 2
y = (sh-wh) / 3
window.geometry("%dx%d+%d+%d" %(ww,wh,x,y))

# user information
tk.Label(window, text='工作时间: ').place(x=50, y= 50)
tk.Label(window, text='提醒时间（分钟）: ').place(x=50, y= 90)
# tk.Label(window, text='to_user: ').place(x=50, y= 130)
# tk.Label(window, text='HTML: ').place(x=50, y= 170)






def open_txt(path):
    file_object = open(path)
    txt_str=""
    try:
        for line in file_object:
            txt_str= txt_str +str(line)
    finally:
        file_object.close()
    return txt_str

def write_txt(path,content):
    with open(path, "w",encoding="utf-8") as f:
        f.write(content)

def set_rest():
    result = tk.StringVar()
    result.set("已开启")
    entry_result = tk.Label(window, textvariable=result,fg = "blue")
    entry_result.place(x=310, y=90)
    rest = var_usr_pwd.get()
    global rest_flag
    rest_flag = int(rest)
    write_txt("config.txt",rest)


# var_usr_name = tk.StringVar()
# entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
# entry_usr_name.place(x=160, y=50)
try:
    global rest
    rest = int(open_txt("config.txt"))
except Exception as e:
    rest = 60
    write_txt("config.txt","60")


var_usr_pwd = tk.StringVar()
var_usr_pwd.set(rest)
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd)
entry_usr_pwd.place(x=160, y=90)
# var_usr_user = tk.StringVar()
# entry_usr_user = tk.Entry(window, textvariable=var_usr_user)
# entry_usr_user.place(x=160, y=130)

# var_usr_text = tk.StringVar()
# var_usr_text = tk.Text(width=150,height=45,fg="Silver") #输入框，输入时显示*
# var_usr_text.place(x=160, y=170)

def start():
    result = tk.StringVar()
    result.set("已开启")
    entry_result = tk.Label(window, textvariable=result,fg = "red")
    entry_result.place(x=310, y=90)



sw = StopWatch()
sw.place(x=160, y=50)
# Button(window, text='开始工作', command=sw.Start).place(x=100, y=150)
# Button(window, text='重置时间', command=resw.Start).place(x=200, y=150)
Button(window, text='开始工作', command=sw.Start).place(x=50, y=150)
Button(window, text='起来走走', command=sw.Stop).place(x=150, y=150)
Button(window, text='开启提醒', command=set_rest).place(x=250, y=150)

# login and sign up button
# btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
# btn_sign_up.place(x=450, y=500)





window.mainloop()
