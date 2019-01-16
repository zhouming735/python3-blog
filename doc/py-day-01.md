#python第一天，web运行hello world

##web搭建  
+ 新建app.py文件  
1.导入日志包，并设置日志输出级别INFO
~~~  
import logging; logging.basicConfig(level=logging.INFO)  
~~~  
2.导入必备库  
+ asyncio：Python 3.4版本引入的标准库，直接内置了对异步IO的支持  
+ json：Python标准库，涉及json相关操作方法  
+ os：Python标准库，包含几百个函数,常用路径操作、进程管理、环境参数等几类。os.path子库以path为入口，用于操作和处理文件路径
+ time：Python的时间库  
+ datetime：重新封装了time模块，提供更多接口，提供的类有：date,time,datetime,timedelta,tzinfo  
+ aiohttp：一个支持异步请求的库，利用它和asyncio配合我们可以非常方便地实现异步请求操作  

3.编写app.py内容   
~~~
import logging; logging.basicConfig(level=logging.INFO)
import asyncio,json,os,time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(text='<h1>Awesome</h1>', content_type='text/html')
@asyncio.coroutine
def init(loop):
    app=web.Application(loop=loop)
    app.router.add_get('/', index)
    srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',9100)
    logging.info('server started at http://127.0.0.1:9100 ...')
    return srv

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

~~~

##注意事项
web.Response() 响应方法中需要设置参数content_type='text/html'，否则浏览器不能按要求输出html内容  


