'''基于python的局域网内UDP通讯'''
from tkinter import *
from tkinter import simpledialog, ttk

import threading

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()



    def create_server(self):
        import socket

        # UDP服务器
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 绑定端口:
        s.bind(('192.168.1.2', 9999))

        print('Bind UDP on 9999...')
        while True:
            # 接收数据:
            # data, addr = s.recvfrom(1024)
            self.text.insert(END, s.recv(1024).decode('utf-8') + '\n')

            # print('Received from %s:%s.' % addr, s.recv(1024).decode('utf-8'))
            # print(s.recv(1024).decode('utf-8'))

            # s.sendto(b'Hello, %s!' % data, addr)



    def initWidgets(self):
        # 一个文字label，假装是软件名称
        self.label = Label(self.master, text='microcom')
        self.label['bg'] = 'white'
        self.label.pack()


        # 一个目标容器======================================>>
        self.fr = Frame(self.master)
        self.fr.pack()
        # 一个Lable
        self.la = Label(self.fr, text='目标：')
        self.la.pack(side = LEFT)
        # 一个选择通讯对象框
        self.cb_content = StringVar()
        self.cb = ttk.Combobox(self.fr, textvariable = self.cb_content)
        self.cb['values'] = ('192.168.1.2:9999', '192.168.1.3:9999', '192.168.1.4:9999', '192.168.1.5:9999', '192.168.1.6:9999')
        self.cb.pack(side = LEFT)
        # 容器结尾<<==================================================

        # 一个输入容器======================================>>
        self.fr2 = Frame(self.master)
        self.fr2.pack()
        # 一个Lable
        self.la = Label(self.fr2, text='目标：')
        self.la.pack(side = LEFT)
        # 输入框
        self.inp = StringVar()
        e = Entry(self.fr2, textvariable = self.inp)
        e.pack(side = LEFT)
        # 容器结尾<<==================================================



        # 一个ttk按钮
        bn = ttk.Button(self.master,text='发送', command=self.launch)
        bn.pack()

        # 一个接收信息的text
        self.text = Text(self.master,  )
        self.text.pack()
        # 创建text央视mine
        self.text.tag_configure('mine', justify = RIGHT)


    def launch(self):
        """按钮点击进行发送"""

        # 获取发送目的地
        list = self.cb_content.get().split(':' )

        # 获取发送的字符串并清空输入框
        str = self.inp.get()
        self.inp.set('')

        # 同步本地text
        self.text.insert(END, '>>>我发的：' + str + '\n', 'mine')

        # 发送数据
        data = str.encode()
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(data, (list[0], int(list[1])))
        # s.sendto(data, ('127.0.0.1', 9999))
        # s.close()

        # for data in [b'Michael', b'Tracy', b'Sarah']:
        #     # 发送数据:
        #     s.sendto(data, ('127.0.0.1', 9999))
        #     # 接收数据:
        #     print(s.recv(1024).decode('utf-8'))



root = Tk()
root.title('第五个窗口')
a = App(root)
# 这里要分两个线程，一个线程开启server服务，一个线程打开ui界面
t1 = threading.Thread(target = a.create_server)
t1.start()
root.mainloop()


