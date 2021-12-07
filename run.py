from venv.common.send_message_base import send_massage

if __name__ == '__main__':
    """
    page：一共查找多少页的候选人
    job： 先看发布的岗位列表，0为第一个，1为第二个依次类推
    cookie：登录时，在寻找推荐人页面F12从页面中复制过来
    """
    page=15
    job=2
    cookie="_bl_uid=mpk02qjakXbv8q64gkzh28nsUaas; lastCity=101020100; wd_guid=c6cd0aaf-c31e-4a29-a29e-617437ef88c2; historyState=state; wt2=Du2Hp5txFNwHtt7WisSruodeJs1RwxJufziezV2ZJe8z8Bmsx4grFxMqx6yISnZ71Rfw_XwfnWaJcnmum-3hD7A~~; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1637633069,1637890923,1638150748,1638236825; __f=f90fbd19e7124d136246dd0ca2e4f888; __g=-; __l=l=%2Fwww.zhipin.com%2Fweb%2Fboss%2Findex&r=&g=&s=3&friend_source=0; __c=1638755484; __a=28283146.1625141292.1638704903.1638755484.2239.126.9.2239; acw_tc=0bdd34b216387590858468932e019e2792ed3995800fe0245ef7e3a3b4430d; zp_token=V1Q9MlE-X12VlgXdNqxxodIC2y6TLQxg%7E%7E"
    for i in range (page):
        send_massage(cookie,job,page=i+1)
