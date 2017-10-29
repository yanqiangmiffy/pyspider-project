import requests
from lxml import etree
import csv
import time
#获取所有文章的url
def get_article_urls(i):
    headers = {
        'Host':'www.aiqing.com',
        'Referer':'http://www.aiqing.com/forum.php?mod=viewthread&tid=2019&extra=page%3D1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    root_url = 'http://www.aiqing.com/'
    article_urls = []
    url = 'http://www.aiqing.com/forum.php?mod=forumdisplay&fid=5&page={}'.format(i)
    response=requests.get(url,headers=headers)
    selector=etree.HTML(response.text)

    hrefs=selector.xpath('//table[@id="threadlisttableid"]/tbody/tr/td[@class="icn"]/a/@href')#获取每页的url地址
    for href in hrefs:
        article_urls.append(root_url+href)

    title_tds=selector.xpath('//table[@id="threadlisttableid"]/tbody[position()>1]/tr/th[@class="new"]')#获取每页文章的标题
    titles=title_tds[0].xpath('//a[@class="s xst"]/text()')

    time_tds=selector.xpath('//table[@id="threadlisttableid"]/tbody[position()>1]/tr/td[@class="by"]//span/text()')#获取文章发布时间
    return article_urls,titles,time_tds
def get_article_content(url):
    content=''
    headers = {
        'Host': 'www.aiqing.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    selector=etree.HTML(response.text)
    # content=''.join(selector.xpath('//div[@class="pcb"]//td[@class="t_f"]/text()')).strip()
    data=selector.xpath('//div[@class="pcb"]//td[@class="t_f"]')
    if len(data)>0:
        content=data[0].xpath('string(.)').strip()
    return content
if __name__ == '__main__':
    start_time=time.time()
    for i in range(44):#多页爬取
        article_urls,titles,times=get_article_urls(i+1)
        content=[]
        for url in article_urls:
            content.append(get_article_content(url))
        #保存数据
        with open('data/blog.csv','a+',encoding='utf-8',newline='') as file:
            writer=csv.writer(file)
            for data in list(zip(titles,article_urls,times,content)):
                print(list(data))
                writer.writerow(list(data))
        print('第{}页爬取完成'.format(i+1))
    end_time=time.time()
    print("一共用时:{}秒".format(end_time-start_time))