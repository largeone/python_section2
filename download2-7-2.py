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

url = "http://finance.naver.com/sise/"
res = req.urlopen(url).read().decode('cp949')

soup = BeautifulSoup(res, "html.parser")

top10 = soup.select("#popularItemList > li > a")

print('네이버 주식 인기검색 종목 10위')
for i, e in enumerate(top10, 1):
    print('순위 : {}. 이름 : {}'.format(i, e.string))
