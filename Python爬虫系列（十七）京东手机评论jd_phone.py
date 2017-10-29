import requests
from lxml import etree
import csv


#获取每页所有商品的urls和skuIds(商品id)
def get_products(url):
    res = requests.get(url)
    selector = etree.HTML(res.text)
    pro_urls = selector.xpath( '//div[@id="plist"]/ul/li[@class="gl-item"]/div[@class="gl-i-wrap j-sku-item"]/div[@class="p-name"]/a/@href')
    pro_ids=selector.xpath('//div[@id="plist"]/ul/li[@class="gl-item"]/div[@class="gl-i-wrap j-sku-item"]/@data-sku')
    return pro_urls,pro_ids
#获取商品价格
# https://p.3.cn/prices/mgets?callback=jQuery7360900&skuIds=J_4461494
def get_products_price(pro_ids):
    data_urls=['https://p.3.cn/prices/mgets?&type=1&area=1_72_2799_0&pdtk=&pduid=1498699809220234468699&pdpin=&pin=null&pdbp=0&skuIds=J_{}&ext=1100000'.format(pro_id) for pro_id in pro_ids]
    pro_prices=[]
    for data_url in data_urls:
        data=requests.get(data_url).json()
        pro_prices.append(data[0].get('p'))
    return pro_prices

#获取商品详细信息
def get_products_details(pro_urls):
    products=[]
    for pro_url in pro_urls:
        product={}#存放单个商品
        response=requests.get(' http:'+pro_url).text
        selector=etree.HTML(response)
        data=selector.xpath('//div[@class="p-parameter"]/ul[@class="parameter2 p-parameter-list"]/li/@title')
        try:
            product['pro_name'] = data[0]  # 手机名称
            product['pro_os'] = data[4]  # 手机系统
        except IndexError:
            print("数据不完整")

        products.append(product)
    return products

#保存商品信息
def save_data(products,prices):
    with open('data/products.csv','a+',encoding='utf-8',newline='') as file:
        writer=csv.writer(file)
        for product in zip(products,prices):
            product[0]['pro_price']=product[1]
            data=list(product[0].values())
            writer.writerow(data)
if __name__ == '__main__':
    urls=['https://list.jd.com/list.html?cat=9987,653,655&page={}'.format(i) for i in range(1,10)]
    i=0
    for url in urls:
        i+=1
        print('正在解析第{}页'.format(i))
        pro_urls,pro_ids=get_products(url)
        print("正在获取数据")
        products=get_products_details(pro_urls)#获取每页所有的手机信息
        prices=get_products_price(pro_ids)#获取每页所有手机的价格
        #将价格添加到对应的每个商品里
        print("正在保存数据")
        save_data(products,prices)
