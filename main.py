import os
import requests
import json
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

Cookie = 'pgv_pvid=7252343688; RK=tMY9jEwrWY; ptcz=37a7af04da154c3f93dc034b77a457a1dbbdc21ea5731a23ae4e7ea0cc3cca35; eas_sid=C1k6O1o7S0a2D0J558D3e6G4Q8; iip=0; ua_id=ZYz644s7dOa1QDJGAAAAAPBXkiFfhHcg8UIdHyPHyiY=; wxuin=17534489866815; mm_lang=zh_CN; _tc_unionid=01431ee5-eeb3-4b0e-bd06-902610ef3639; o_cookie=209103572; pac_uid=1_209103572; ptui_loginuin=2953234537; LW_uid=U1e6D2w1V3H4f774k5X9D990f8; LW_sid=g176r2819334w7t4b765v0I0u8; uin_cookie=o0209103572; ied_qq=o0209103572; noticeLoginFlag=1; ts_uid=6824232640; rewardsn=; wxtokenkey=777; uuid=ad43ab9b17ee8e7a1a7f4774602adad1; rand_info=CAESINhkXwvDxGcjm4wwL/jRrX8Zq80wiGyY/teYuHPh+W7u; slave_bizuin=3588953568; data_bizuin=3588953568; bizuin=3588953568; data_ticket=DKevNGym0d0V34PVY4W5Ul/2F/EG0CvfHQ7SFfE8DR8yl937NuzaJD4KXcghhfQ0; slave_sid=ejZXWkdkU0cwenBOUHJkRHRab2taR05xc1ZYU1NrSTRVWnVQZmlMMWhpUXpsN0NYQnhmYkFzdVBpSjhabmhmRHRJd1VPWXFUREk0VnNFRnpSU3g1cnlIR0RKTkxWV1N1SE9kVTJxNUJnVHNpeXp4ejhNWmpJNkpEanBkbkVoeWFSNmszZTZ4eEhlNjdwMlZn; slave_user=gh_7b63669e1290; xid=10f9c2fcd18c81b161bc51198dfbc05f'
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
headers = {
 "Cookie": Cookie,
 "User-Agent": 'Mozilla/5.0 (Linux; Android 10; YAL-AL00 Build/HUAWEIYAL-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.64 HuaweiBrowser/10.0.1.335 Mobile Safari/537.36'
  }

ID = '每日60s简报'
token = '645266520'
search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?action=search_biz&begin=0&count=5&query={}&token={}&lang=zh_CN&f=json&ajax=1'.format(ID,token)

doc = requests.get(search_url,headers=headers).text
jstext = json.loads(doc)
fakeid = jstext['list'][0]['fakeid']

data = {
  "token": token,
  "lang": "zh_CN",
  "f": "json",
  "ajax": "1",
  "action": "list_ex",
  "begin": 0,
  "count": "5",
  "query": "",
  "fakeid": fakeid,
  "type": "9",
  }
json_test = requests.get(url, headers=headers, params=data).text
json_test = json.loads(json_test)
page = json_test["app_msg_list"]
page = page[0]['link']
html = requests.get(page)
text_obj = BeautifulSoup(html.text,'lxml')
imgurl = text_obj.find('div',class_='share_media').find('img').get('src')
r = requests.get(imgurl)
img = Image.open(BytesIO(r.content))
path = os.path.split(os.path.realpath(__file__))[0]
with open(path+'/'+'news.jpg','wb') as f:
    f.write(r.content)
