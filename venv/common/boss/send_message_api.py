from venv.utils.request_utils import HttpRequests


def  send_message(cookie,gid,jid,expid,lib,securityId):
    url="https://www.zhipin.com/wapi/zpboss/h5/chat/start"
    headers={

            "Host": "www.zhipin.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
            "cookie": cookie
    }
    data={
            "gid": gid,
            "suid": None,
            "jid": jid,
            "expectId": expid,
            "lid": lib,
            "from": None,
            "securityId": securityId
    }
    res=HttpRequests("post",url=url,headers=headers,data=data).request()
    return res
