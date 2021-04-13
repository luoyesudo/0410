# coding = utf-8
# Author: 没有不同
# Date: 2021/4/2 17:52
# Year： 2021
import websocket
url='ws://echo.websocket.org/'
websocket.enableTrace(True)
ws=websocket.create_connection(url=url,header=["User-Agent: MyProgram", "x-custom: header"])
ws.send('000')
print(ws.recv())
