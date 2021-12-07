from jsonpath import jsonpath

from venv.common.boss.query_job_list import job_list
from venv.common.boss.search_geeklist_api import geek_list
from venv.common.boss.send_message_api import send_message
from venv.utils.log_utils import logger


def send_massage(cookie, jobid,page):
    joblist=job_list(cookie)
    joblistid=joblist["zpData"]["onlineJobList"][jobid]["encryptId"]
    jobName=joblist["zpData"]["onlineJobList"][jobid]["jobName"]
    logger.info("准备筛选岗位：" + str(jobName)+"的候选人")
    geeklist=geek_list(cookie,joblistid,page)
    # logger.info("获取到的候选人列表"+str(geeklist))

    geekinfomation = geeklist["zpData"]["geekList"]
    gooki=[]
    geeknamelist=[]
    # logger.info("获取到的候选人列表" + str(geekinfomation))
    # 筛选符合条件的候选人id
    for i in range (len(geekinfomation)):
        content=geekinfomation[i]["geekCard"]["geekWorks"]
        encryptGeekId = list(set(jsonpath(content, "$..responsibility")))
        if ("银行" or "信贷") in str(encryptGeekId):
            gid=geekinfomation[i]["encryptGeekId"]
            securityId=geekinfomation[i]["geekCard"]["securityId"]
            geekName=geekinfomation[i]["geekCard"]["geekName"]
            expectId=geekinfomation[i]["geekCard"]["expectId"]
            lid = geekinfomation[i]["geekCard"]["lid"]
            geeknamelist.append(geekName)
            gooki.append([gid,expectId,lid,securityId,geekName])

        # else:
        #     ad = geekinfomation[i]["encryptGeekId"]
        #     logger.info("当前候选人不符合" +ad)
    if geeknamelist == []:
        logger.info("筛选第"+str(page)+"页候选人无符合")
    else:
        logger.info("筛选出第"+str(page)+"页符合的候选人"+str(geeknamelist))

    for i in range(len(gooki)):
        gid=gooki[i][0]
        expid=gooki[i][1]
        lib=gooki[i][2]
        securityId=gooki[i][3]
        geekName = gooki[i][4]
        jid = joblistid
        logger.info("正在给"+str(geekName)+"打招呼")
        msg=send_message(cookie=cookie,gid=gid,jid=jid,expid=expid,lib=lib,securityId=securityId)
        msg=msg.json()
        if msg["message"]=="Success":
            logger.info(str(geekName)+"发送成功")
        else:
            logger.info(str(geekName)+"发送失败")





# if __name__ == '__main__':
#     send_massage("_bl_uid=mpk02qjakXbv8q64gkzh28nsUaas; lastCity=101020100; wd_guid=c6cd0aaf-c31e-4a29-a29e-617437ef88c2; historyState=state; wt2=Du2Hp5txFNwHtt7WisSruodeJs1RwxJufziezV2ZJe8z8Bmsx4grFxMqx6yISnZ71Rfw_XwfnWaJcnmum-3hD7A~~; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1637633069,1637890923,1638150748,1638236825; __f=f90fbd19e7124d136246dd0ca2e4f888; __g=-; __l=l=%2Fwww.zhipin.com%2Fweb%2Fboss%2Findex&r=&g=&s=3&friend_source=0; __c=1638755484; __a=28283146.1625141292.1638704903.1638755484.2239.126.9.2239; acw_tc=0bdd34b216387590858468932e019e2792ed3995800fe0245ef7e3a3b4430d; zp_token=V1Q9MlE-X12VlgXdNqxxodIC2y6TLQxg%7E%7E",2,15)