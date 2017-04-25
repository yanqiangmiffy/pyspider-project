

```python
#爬取360图片
#分析好网站之后，发现规律，每次下拉出现30张图片
import requests
import urllib.request

class Pic360():
    def __init__(self):
        self.url="http://image.so.com/zj?ch=beauty&sn={}&listtype=new&temp=1"
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
        self.img_urls=[]
        self.offset=30
    def get_list(self):
        try:
            #爬取十页（相当于下拉十次）
            for i in range(10):
                print('下拉第'+str(i+1)+'次')
                res = requests.get(self.url.format(self.offset))
                data = res.json()
                #print(data['list'])
                items = data['list']
                for item in items:
                    print(item['qhimg_url'])
                    self.img_urls.append(item['qhimg_url'])
                self.offset+=30
            return self.img_urls
        except Exception as e:
            print(e,"获取图片urls失败")
    def download_img(self,img_srcs):
        for src in img_srcs:
            img_name=src.split('/')[-1]
            file_path="G://360pic/"
            urllib.request.urlretrieve(src, filename=file_path+img_name)
        print("下载图片结束")

xizai=Pic360()
img_srcs=xizai.get_list()
xizai.download_img(img_srcs=img_srcs)
```
