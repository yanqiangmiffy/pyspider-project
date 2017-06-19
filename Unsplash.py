from selenium import webdriver#实现自动下拉
from lxml import etree#定位元素（更加高效）
from urllib.parse import urlparse#解析图片的名称
import urllib.request#urlretrieve()下载保存图片
import re
import time


class Unsplash:
    #初始化构造函数
    def __init__(self):
        self.url='https://unsplash.com/'#请求地址
        self.save_path="G://unsplash/"#图片保存路径
        self.driver=webdriver.Chrome('G:/chromedriver/chromedriver.exe')
        #self.driver = webdriver.PhantomJS()
    #实现下拉动作，并返回网页源代码，times:下拉次数
    def do_scroll(self,times):
        #打开目标网址
        driver=self.driver
        driver.get(self.url)
        #模拟下拉操作
        for i in range(times):
            print('正在下拉'+str(i+1)+'次：')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print('等待'+str(i+1)+'次网页加载')
            time.sleep(40)
        #解析网页源码
        html=etree.HTML(driver.page_source)
        return html

    #下载图片保存到本地
    def save_img(self,src,img_name):
        urllib.request.urlretrieve(src, filename=self.save_path + img_name)

    def get_pic(self, html):

        #获取a标签的style内容
        all_uls = html.xpath('//a[@class="cV68d"]/@style')
        # 获取图片下载地址，
        for url in all_uls:
            #使用正则表达式获取想要的src地址
            src = re.findall(r'url\(\"(.*?)\"\)',url,re.S)[0]
            print(src)
            #使用urlparse解析地址，使用path的内容，去除不需要的参数
            fina_src=urlparse(' ' + src).path.strip()
            # 保存图片的名字
            img_name = fina_src.split('/')[-1]+'.jpg'
            print(fina_src,img_name)
            self.save_img(src,img_name)

    def main(self):
        #获取源码
        html=self.do_scroll(1)
        print("开始下载图片")
        self.get_pic(html)
img=Unsplash()
img.main()