from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import json
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# url = "http://finance.daum.net"
# res = req.urlopen(url).read()
# soup = BeautifulSoup(res, "html.parser")
#
# # print('soup', soup.prettify())
#
# top = soup.select("ul#")

ua = UserAgent()

headers = {
    'User-Agent': ua.ie,
    'referer': 'https://finance.daum.net'
}

url = "https://finance.daum.net/api/search/ranks?limit=10"

res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')

# print('res', res)

rank_json = json.loads(res)['data']

print('중간 확인: ', rank_json, '\n')

for elm in rank_json:
    # print(type(elm))
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'], elm['tradePrice'], elm['name']))
