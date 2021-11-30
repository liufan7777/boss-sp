from venv.utils.request_utils import HttpRequests


def  send_message(cookie,gid,jid,expid,lib):
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
            "securityId": "UgcuEknhZDPL8-K1Hd8OegwlaXXR9EMhlmR2ypO8RwWQLVXZPEetjqCjxBgQaGb7jpJFo90L5DM9RB_G4_bnV0KNX1lo78O8pAK5oYBWeQcKJEGKStkd53AlLYB_T9ihIt3Jz9ErrybU6z4bUty2TON0_Ckn6sEaW_hbDyn0-eprWo5sQmiJ3d_-T2isW7CLUItdD8ltEvCYtuvSDX9L9xde_2SAqa8PCjfgRvwrVj3mGtZqbAvi8i5j9Yvvc2MroZsSM-O-GsMK5kBAEDFQX2Cmzj8IklvrH3O1vTFFgTaj-ZgjR-S2-RlTc9T-EGdtCyk0Ssz5uadpFcsPxVOsSfM2VCUCCNRqptY1ZU-IjS2moHo1113IM1P30Q959iH1XUVRYOWR9RSlocO4L2lJLbkjia0wPYn5y1vj3Nr19xY0Jm6wIfwVmHwsgSeFsEgHKQSHUEI_IKDz9Cjnjj-SvYbkuBmIhTA-v5sKteOMvJO5qs1i0_Bm1ZPgb9lmJtb73cH6cw~~"
    }
    res=HttpRequests("post",url=url,headers=headers,data=data).request()
    return res
