import os
import tkinter
from tkinter import ttk
from tkinter import Label, Tk, LabelFrame, Entry, Button, StringVar
from tkinter.filedialog import askopenfilename, askdirectory
import utils

class Window:

    def __init__(self):
        # attr初始化
        self.root = Tk()
        self.init_window_frame = LabelFrame(self.root, text="")
        self.init_window_frame.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.7)

        # 数据变量
        self.header_t = StringVar()                                 # Header_T
        self.header_user_agent = StringVar()                        # Header_User_Agent

        # 组件
        self.start_button = None
        self.progress_bar = None        # 进度条

        # 设置根窗口属性
        self.root.title("羊了个羊治愈器")
        self.root.geometry("550x350")
        self.root.attributes("-alpha", 1)

        self.create_page()

    """
        界面功能初始化
    """
    def create_page(self):
        Label(self.root).grid(row=0, stick='W', pady=10)

        # 第一行输入 - header_t的值
        Label(self.init_window_frame).grid(row=1, column=0, padx=30)
        Label(self.init_window_frame, text="header_t的值").grid(row=1, column=1, stick='W', pady=10)
        self.header_t_entry = Entry(
            self.init_window_frame,
            textvariable=self.header_t,
            width=20,
        )
        self.header_t_entry.grid(row=1, column=2, stick='E')

        # 第二行输入 - header_user_agent的值
        Label(self.init_window_frame).grid(row=2, column=0, padx=30)
        Label(self.init_window_frame, text="header_user_agent").grid(row=2, column=1, stick='W', pady=10)
        self.header_user_agent_entry = Entry(
            self.init_window_frame,
            textvariable=self.header_user_agent,
            width=20,
        )
        self.header_user_agent_entry.grid(row=2, column=2, stick='E')

        # 空白
        Label(self.init_window_frame).grid(row=5, stick='W')

        # 按钮
        self.start_button = Button(
            self.init_window_frame,
            text="开始",
            width=10
        )

        self.start_button.grid(row=6, column=1, columnspan=3)

        def button_event(event):
            self.progress_bar['maximum'] = 100
            self.progress_bar['value'] = 0

            header_t = self.header_t_entry.get()
            header_user_agent = self.header_user_agent_entry.get()
            
            if header_t is None or len(header_t) == 0 or header_user_agent is None or len(header_user_agent) == 0:
                self.notify("参数不能为空", 2)
                return
            success, time = utils.game_over(header_t, header_user_agent)
            if not success:
                self.notify("请求失败,请检查head_t和head_user_agent的值是否正确", 2)
                return
            self.progress_bar['value'] = 100
            self.notify("【羊了个羊闯关结束 (完成耗时:{} s)】".format(time), 3)


        self.start_button.bind("<Button-1>", button_event)


        self.label = Label(self.init_window_frame, text="")
        self.label.grid(row=8, column=1, columnspan=3)


        # 空白
        Label(self.init_window_frame).grid(row=8, stick='W')

        # 进度条
        self.progress_bar = ttk.Progressbar(
            self.init_window_frame,
            length=320,
            mode='determinate',
            orient=tkinter.HORIZONTAL,
        )
        self.progress_bar['maximum'] = 100
        self.progress_bar['value'] = 0
        self.progress_bar.grid(row=9, column=1, columnspan=3)

    def notify(self, msg, state=1):
        self.label['text'] = msg
        if state == 1: # 默认文本
            self.label['fg'] = "black"
        elif state == 2: # 警告
            self.label['fg'] = "red"
        elif state == 3: # 成功
            self.label['fg'] = "green"
        else:
            self.label['fg'] = "black"

    def run(self):
        self.init_window_frame.mainloop()