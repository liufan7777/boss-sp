# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # author   : 刘樊
# # contact  : fan.liu@weimob.com
# # file     : test_goods.py
# # time     : 2021/11/24 9:24 PM
# # desc     : C端查询商品列表

import json

from venv.utils.log_utils import logger
from venv.utils.request_utils import HttpRequests


def query_goodslist():
    url = "http://saas-mall.qa.internal.weimob.com/mall/navigation/goods/getGoodsList"
    header ={
        'Content-Type': 'application/json',
    }

    data={
    "appid": "wx423275d4b8cb769c",
    "basicInfo": {
        "isStoreId": False,
        "pid": None,
        "merchantId": 2000000016212,
        "bosId": 4000136704212,
        "vid": 6000220771212,
        "vidType": 2,
        "vidTypeName": "\u54c1\u724c",
        "vidTypes": [
            2
        ],
        "vidPath": "-6000220770212-6000220771212-",
        "vidDeleted": False,
        "activeStatus": True,
        "productId": 145,
        "productVersionId": "1438691413058424924",
        "productInstanceId": 4177212,
        "statusCode": "in_use",
        "vidName": "\u6211\u7684\u54c1\u724c",
        "productName": "\u5546\u57ce",
        "cid": 5100212
    },
    "extendInfo": {
        "source": 1,
        "refer": "ec-goods-list",
        "youshu": {
            "token": "tokenStr",
            "enable": True
        },
        "wxTemplateId": 321
    },
    "queryParameter": {
        "goodsClassifyId": 0,
        "goodsClassifyName": "\u5168\u90e8\u5546\u54c1",
        "search": "ZDH",
        "sortBySearch": 0,
        "searchType": 1,
        "sortByRule": 1,
        "propValueList": [],
        "minSalePrice": "",
        "maxSalePrice": ""
    },
    "pid": "3400",
    "storeId": "0",
    "orderBy": [
        {
            "field": "complex",
            "sort": "desc"
        }
    ],
    "pageNum": 1,
    "pageSize": 50,
    "level": 1,
    "scenePageCode": 5,
    "openid": "",
    "templateId": 1
}
    datas=json.dumps(data)
    res = HttpRequests("POST", url=url, headers=header, data=datas).request()
    logger.info("C端查询结果" + str(res))
    return res.json()
if __name__ == '__main__':
    query_goodslist()