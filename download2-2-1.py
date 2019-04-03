import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

imgUrl = "https://tvetamovie.pstatic.net/libs/1222/1222208/7a32e417c676b0d0968c_20181212142727870.mp4-pBASE-v0-f70540-20181212143843797_1.mp4"
htmlURL = "http://google.com"

savePath1 = "./test1.mp4"
savePath2 = "./index.html"

dw.urlretrieve(imgUrl,savePath1)
dw.urlretrieve(htmlURL,savePath2)

print("다운로드 완료!")
