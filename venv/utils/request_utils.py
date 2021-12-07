from time import sleep

import jsonpath
import requests

from venv.utils.log_utils import logger

filepath = 'tmp/tmp.yaml'

class HttpRequests:
    '''把get和post封装成为一个类'''
    def __init__(self,method,url,headers = None,data = None,json = None, cookies=None):
        # logger.info("请求method值为：" + str(method) + "; 请求url为： " + str(url) + "; headers为： " + str(headers) + " ;data为： " + str(data)+ " ;json为： " + str(json))
        self.method = method
        self.url = url
        self.data = data
        self.json = json
        self.headers = headers
        self.cookies = cookies

    def request(self):
        sleep(1)
        res=None
        try:
            if self.method.upper() == 'GET':
                res = requests.get(url=self.url, headers=self.headers, params=self.data)
                # logger.info("返回 res的值为：" + str(res.text))
            elif self.method.upper() == 'POST':
                if self.data is not None and self.json is None:
                    res = requests.post(url=self.url, headers=self.headers, data=self.data,cookies=self.cookies)
                    # logger.info("返回 res的值为：" + str(res.text))
                elif self.json is not None and self.data is None:
                    res = requests.post(url=self.url, headers=self.headers, json=self.json)
                    # logger.info("返回 res的值为：" + str(res.text))
                else:
                    res = None
                    raise Exception("请求数据不和法！")
            else:
                res = None
                raise Exception("请求方法不和法！")
        except Exception as err:
            logger.info('获取res失败：\n{0}'.format(err))
        return res





