import tkinter
import tkinter.messagebox
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps, loads
from threading import Thread, Event


class ClientConnectedHandler(Thread):

    def __init__(self, client):
        super().__init__()
        self._client = client

    def run(self):
        my_dict = {}
        my_dict["filename"] = "guido.jpg"
        # 通过dumps函数将字典处理成JSON字符串
        json_str = dumps(my_dict)
        # 发送JSON字符串
        self._client.send(json_str.encode("utf-8"))
        self._client.close()


class ServerThread(Thread):
    def __init__(self):
        # 将线程设置为守护线程，确保当主线程退出时，服务器线程不会阻碍进程关闭
        super().__init__(daemon=True)

    def run(self):
        server = socket()
        self.__server = server
        # 绑定IP地址和端口(区分不同的服务)
        server.bind(("192.168.2.243", 5566))
        # 开启监听 - 监听客户端连接到服务器
        # 512 是连接队列的大小，服务器处理现有连接时，能够等待的最大未处理连接数
        # 队列已满，客户端会收到服务器拒绝连接的错误
        server.listen(512)
        print("服务器启动开始监听...")
        try:
            while True:
                client, addr = server.accept()
                # 启动一个线程来处理客户端的请求
                ClientConnectedHandler(client).start()
        except OSError:
            print("服务器已关闭")

    def stop(self):
        return self.__server.close()


class ClientThread(Thread):
    def __init__(self):
        # 将线程设置为守护线程，确保当主线程退出时，服务器线程不会阻碍进程关闭
        super().__init__(daemon=True)

    def run(self):
        client = socket()
        self.__client = client
        client.connect(("192.168.2.243", 5566))
        in_data = bytes()
        # 由于不知道服务器发送的数据有多大每次接收 1024 字节
        data = client.recv(1024)
        while data:
            # 将收到的数据拼接起来
            in_data += data
            data = client.recv(1024)
        # 将JSON字符串转成字典对象
        my_dict = loads(in_data.decode("utf-8"))
        filename = my_dict["filename"]
        print(f"client receive filename: {filename}")

    def stop(self):
        return self.__client.close()


class SocketBuilder(object):
    def createGUI(self):
        # 创建顶层窗口
        top = tkinter.Tk()
        self.__top = top
        # 设置窗口大小
        top.geometry("500x200")
        # 设置窗口标题
        top.title("客户端/服务器")
        # 创建标签对象并添加到顶层窗口
        # label = tkinter.Label(top, text="Hello, world!", font="Arial -32", fg="red")
        # label.pack(expand=1)
        # 创建一个装按钮的容器
        panel = tkinter.Frame(top)
        # 创建按钮对象 指定添加到哪个容器中 通过 command 参数绑定事件回调函数
        createClientBtn = tkinter.Button(
            panel, text="创建客户端连接", command=self.__createClient
        )
        createClientBtn.pack(side="left")
        createServerBtn = tkinter.Button(
            panel, text="创建服务端连接", command=self.__createServer
        )
        createServerBtn.pack(side="right")
        extBtn = tkinter.Button(panel, text="退出", command=exit)
        extBtn.pack(side="right")
        panel.pack(side="bottom")
        # 开启主事件循环
        tkinter.mainloop()

    def __createClient(self):
        print("create client")
        clientThread = ClientThread()
        clientThread.start()
        self.__clientThread = clientThread

    def __createServer(self):
        print("create server")
        serverThread = ServerThread()
        serverThread.start()
        self.__serverThread = serverThread

    def exit(self):
        if tkinter.messagebox.askokcancel("温馨提示", "确定要退出吗?"):
            self.__client.close()
            if self.__serverThread:
                self.__serverThread.stop()
            if self.__clientThread:
                self.__clientThread.stop()
            self.__top.quit()


if __name__ == "__main__":
    socketBuilder = SocketBuilder()
    socketBuilder.createGUI()
