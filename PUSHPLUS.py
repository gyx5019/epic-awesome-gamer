import requests
import os
token = os.environ['9fff214b3d7f4b879ce08477e788af5d']
title= 'Epic-FreeGamer'
content ='Epic-FreeGamer任务已执行'
url = 'http://www.pushplus.plus/send?token='+token+'&title='+title+'&content='+content
requests.get(url)
