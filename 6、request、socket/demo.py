"""request"""

# import requests


# def fetchData():
#     resp = requests.get("http://api.tianapi.com/meinv/?key=APIKey&num=10")
#     data = resp.json()
#     return data


# data = fetchData()
# print(data)

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


"""socket"""
# socket 作用
# 创建服务器：用 socket 模块创建一个监听的套接字，绑定到特定的 IP 地址和端口号，并监听客户端的连接请求。这样，客户端就可以连接到该服务器并进行通信。
# 创建客户端：用 socket 模块创建一个连接的套接字，然后连接到服务器的 IP 地址和端口号，发送和接收数据

# demo: socket_c_s.py
