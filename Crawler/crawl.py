import Model.MainModel
import requests
import time
from bs4 import BeautifulSoup
from Crawler.crawlrule import *

model = Model.MainModel.MainModel.getInstance()
defurl = 'http://odds.500.com/'


def creatWebHeard():
    # 构造请求报头
    webheaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'}
    return webheaders


def getDatas(url):
    header = creatWebHeard()
    req = requests.get(url, headers=header)
    encoding = req.apparent_encoding
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
    encode_content = req.content.decode(encoding, 'replace')
    return encode_content


class Crawler():

    def __init__(self):
        # self.ruleFun = {'odds500': ruleBy500, 'list': self.getMatchList}
        pass

    def runCrawler(self, t):
        model.view['main'].outPutText(
            model.datamodel['info']['start'], True)
        model.startTime = time.time()
        if model.crawlLock:
            model.view['main'].outPutText(model.datamodel['info']['start'], True)
            return
        model.crawlLock = True
        d = getDatas(defurl)
        soup = BeautifulSoup(d, 'html5lib')
        obj = self.ruleFun[t](soup)
        model.getData[t]=obj
        return obj

    def getAllodds(self):
        pass

