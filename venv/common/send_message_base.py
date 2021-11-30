from jsonpath import jsonpath

from venv.common.boss.query_job_list import job_list
from venv.common.boss.search_geeklist_api import geek_list
from venv.common.boss.send_message_api import send_message
from venv.utils.log_utils import logger


def send_massage(cookie, jobid):
    joblist=job_list(cookie)
    joblistid=joblist["zpData"]["onlineJobList"][jobid]["encryptId"]
    logger.info("获取到的jobid为" + str(joblistid))

    geeklist=geek_list(cookie,joblistid)
    # logger.info("获取到的候选人列表"+str(geeklist))

    geekinfomation = geeklist["zpData"]["geekList"]
    gooki=[]
    logger.info("获取到的候选人列表" + str(geekinfomation))
    # 筛选符合条件的候选人id
    for i in range (len(geekinfomation)):
        content=geekinfomation[i]["geekCard"]["geekWorks"]
        encryptGeekId = list(set(jsonpath(content, "$..responsibility")))
        if ("银行" or "信贷") in str(encryptGeekId):
            gid=geekinfomation[i]["encryptGeekId"]
            expectId=geekinfomation[i]["geekCard"]["expectId"]
            lid = geekinfomation[i]["geekCard"]["lid"]
            gooki.append([gid,expectId,lid])
            print(gooki)

        # else:
        #     ad = geekinfomation[i]["encryptGeekId"]
        #     logger.info("当前候选人不符合" +ad)


    for i in range(len(gooki)):
        gid=gooki[i][0]
        expid=gooki[i][1]
        lib=gooki[i][2]
        jid = joblistid
        msg=send_message(cookie=cookie,gid=gid,jid=jid,expid=expid,lib=lib)
        print(msg.json())





if __name__ == '__main__':
    send_massage("lastCity=101020100; _bl_uid=F1k6hsn10dhgk3g4Czd1asFvRC0n; wd_guid=efb658c5-6d96-45b7-bf87-a987a992977a; historyState=state; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1637840440; __zp_stoken__=53d1dGm93URwwRD8fLCxWGmhxL2Y9KWhsc0hXSCUOGl16ex0VLV5JBEsuJxItG3JdHnYHVTc1GAwgH2w8MxB8X29nAzY4cCR4cmQTcwE1FBwzEVlNN0VwFSNBaCExFisMXE81fS1OZwVtBT4%3D; acw_tc=0bdd34ce16379276253642965e019e560ed542bb9251cdcba700d1efb3c9ee; __zp_seo_uuid__=08d2e932-4058-4e57-8de5-0dc7f6e4b544; __g=-; wt2=Dfl7NiQTXuoa_gD8TBWe7w9ZUkZ-SR1U2a4oQyNMFNACU0a6hj9rWO8puaY7GmK_d2JYleEnlDhluyMPymrNlsQ~~; zp_token=V1Q9MlE-X12VlgXdNqyBQaISq47TvXxg%7E%7E; __l=r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DCvNSqSRzp3NpgeRbXOBX7H2H3LbTIB03m72mayQ3Inq26dxP3WadR-6r6u6zdR5Y%26wd%3D%26eqid%3De92ad60700004da70000000461a0cac6&l=%2Fwww.zhipin.com%2Fweb%2Fboss%2Findex&s=3&g=&friend_source=0&s=3&friend_source=0; __f=af5b2b0fa430f0701a2910ddf7c7cc5e; __c=1637927627; __a=28596633.1628260836.1637840440.1637927627.65.6.5.12",1)