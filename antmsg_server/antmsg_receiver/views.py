from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json

def receive_antmsg(request):
    if request.method == 'POST':
        # 解析请求中的JSON格式的消息
        msg = json.loads(request.body)
        # 根据消息类型进行相应的处理
        if msg['type'] == 'text':
            # 处理文本消息
            content = msg['content']
            # TODO: 进行相应的处理
        elif msg['type'] == 'image':
            # 处理图片消息
            media_id = msg['media_id']
            # TODO: 进行相应的处理
        # 返回处理结果
        return HttpResponse('OK')
    else:
        return HttpResponse('Method Not Allowed')