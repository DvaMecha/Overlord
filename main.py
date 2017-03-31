# coding=utf-8
from view.QtView import *
from PyQt5.QtWidgets import QApplication
import Crawler.CrawlSave as fileManager
from Crawler import crawl
import Model.MainModel as Model
import json
import requests
import sys

# 定义变量
eventModel = {}
websites = ()
model = Model.MainModel.getInstance()



def initApp():
    jsfile = 'datamodel.json'
    fp = open(jsfile, 'r')
    model.datamodel = json.load(fp)
    fp.close()
    model.crawler = crawl.Crawler()
    showHelp()


def initEvent():
    model.events = {
        'init': initApp,
        'runCrawl': runCrawl,
        'save': fileManager.saveData,
        'showHelp': showHelp,
        'getMatchs': getMatchList
    }
    return model.events


def runCrawl():
    main.outPutText('开始抓取', True)
    model.crawler.runCrawler('odds500')
    # model.getData['all'] = d
    # model.getData[t] = rule.analysisHtml(d, t)

def getMatchList():
    main.outPutText('开始获取比赛列表', True)
    model.crawler.runCrawler('list')

def showHelp():
    main.outPutText(
        '''
            Welcome!
        ''', True)


# 获得窗口对象


app = QApplication(sys.argv)
main = QtView(initEvent())
model.view['main'] = main
initApp()
app.exec_()
