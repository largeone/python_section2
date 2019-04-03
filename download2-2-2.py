import sys
import io
import urllib.request as dw


sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

imgUrl = "http://post.phinf.naver.net/20150815_145/pepsiman517_143961030555702Wvp_JPEG/mug_obj_143961030555936553.jpg"
htmlURL = "http://google.com"

savePath1 = "./test1.jpg"
savePath2 = "./index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1,'wb') # w : write, r :read, a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")
