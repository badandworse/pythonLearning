#server.py

from wsgiref .simple_server import make_server
#导入我们自己编写的application 函数
from hello import application

httpd=make_server('',8000,application)
print('Serving HTTP on port 8000...')
#开始监听HTTP请求
httpd.serve_forever()