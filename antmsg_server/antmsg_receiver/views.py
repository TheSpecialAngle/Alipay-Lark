from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import alipay

alipay_PUBLIC_KEY_PATH = 'path/to/alipay_public_key.pem'
APP_PRIVATE_KEY_PATH = 'path/to/app_private_key.pem'
APP_ID = 'your_app_id'

@csrf_exempt
def alipay_notify(request):
    if request.method == 'POST':
        data = request.POST.dict()
        alipay_client = alipay(
            appid=APP_ID,
            app_notify_url=None,
            app_private_key_path=APP_PRIVATE_KEY_PATH,
            alipay_public_key_path=alipay_PUBLIC_KEY_PATH,
            sign_type="RSA2",
            debug=False,
        )
        sign = data.pop('sign', None)
        if alipay_client.verify(data, sign):
            # 验签通过，处理消息
            trade_status = data.get('trade_status')
            if trade_status == 'TRADE_SUCCESS':
                # 处理交易成功的情况
                return HttpResponse('success')
            else:
                # 处理其他情况
                return HttpResponse('fail')
        else:
            # 验签失败，返回错误响应
            return HttpResponse('fail')
    else:
        # 非POST请求，返回错误响应
        return HttpResponse('fail')