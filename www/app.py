import logging; logging.basicConfig(level=logging.INFO)
import asyncio,json,os,time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(text='<h1>Awesome</h1>', content_type='text/html')

@asyncio.coroutine
def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    #app.router.add_get('/', index)
  
    srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',9100)
    logging.info('server started at http://127.0.0.1:9100 ...')
    return srv

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

