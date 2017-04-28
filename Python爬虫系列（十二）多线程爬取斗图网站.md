

```python
import requests
import threading#多线程处理与控制
from bs4 import BeautifulSoup
from lxml import etree#解析网页，比自带的html.parser速度更快

#打开网页，获取源码
#网站禁止爬虫
#添加headers 模拟浏览器
#添加user_agent
def get_html(url):
    #url='https://www.doutula.com/article/list/?page=1'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    request=requests.get(url=url,headers=headers)
    response=request.text
    return response
#从主页获取斗图的每一个url，获取源码
def get_img_html(html):
    soup=BeautifulSoup(html,'lxml')#创建一个对象
    all_a=soup.find_all('a',class_='list-group-item')
    for link in all_a:
        img_html=get_html(link['href'])
        img_html+=img_html
    return img_html
        
#获取每个图片src地址
def get_img(html):
    soup=etree.HTML(html)#初始化打印源码，自动修正html源码
    # //代表选择盒子内容，[]代表过滤的条件 @选定属性盒子
    items=soup.xpath('//div[@class="artile_des"]')#解析网页方法
    for item in items:
        imgurl_list=item.xpath('table/tbody/tr/td/a/img/@onerror')
        start_save_img(imgurl_list)

#下载图片
def save_img(img_url):
    #global x
    #x+=1
    img_url=img_url.split('=')[-1][1:-2].replace('jp','jpg')
    print(u'正在下载'+'http:'+img_url)
    img_content=requests.get('http:'+img_url).content
    with open('G:\doutu\%s.jpg' % img_url.split('/')[-1],'wb') as f:#wb写的模式
        f.write(img_content)

#多线程
def start_save_img(imgurl_list):
    for i in imgurl_list:
        th=threading.Thread(target=save_img,args=(i,))
        th.start()#启动线程



#多页
def main():
    start_url='https://www.doutula.com/article/list/?page={}'
    for i in range(1,8):
        start_html=get_html(start_url.format(i))#获取外页url
        html=get_img_html(start_html)#获取内页url里面的源码
        get_img(html)
# if __name__=='__main__':
#     main()
main()
print("爬取结束")
#save_img()
# a=get_html(1)
# get_img_html(a)

```

    正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616598_vriFjP.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616599_xNjLzl.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616599_OYVxIi.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616600_BVpnQK.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616600_VyLFsW.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616601_vTmyeH.jpg正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616602_NBXtda.jpg
    
    正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616602_sFmQKt.jpg正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616602_PYTwgA.jpg正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616598_vriFjP.jpg
    
    正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616599_xNjLzl.jpg正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616599_OYVxIi.jpg正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616600_BVpnQK.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616600_VyLFsW.jpg
    
    
    正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616601_vTmyeH.jpg
    
    正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616602_NBXtda.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616602_PYTwgA.jpg正在下载http://img.doutula.com/production/uploads/image/2017/04/19/20170419616602_sFmQKt.jpg
    
    正在下载http://img.doutula.com/production/uploads/image/2017/04/14/20170414179590_WwYETk.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/14/20170414179591_pQNeuh.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/14/20170414179592_elrEkf.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/14/20170414179593_OoKena.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/14/20170414179590_WwYETk.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/14/20170414179591_pQNeuh.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/14/20170414179592_elrEkf.jpg正在下载http://img.doutula.com/production/uploads/image/2017/04/14/20170414179593_OoKena.jpg
    
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744261_zaKFUe.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744262_KpOhcq.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744262_ZatjsF.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744263_zRlIbo.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744264_FTWcvN.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744265_xyqdZE.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744265_rGBMCh.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744266_JuXbTN.jpg正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744261_zaKFUe.jpg
    
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744262_KpOhcq.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744262_ZatjsF.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744263_zRlIbo.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744264_FTWcvN.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744265_xyqdZE.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744265_rGBMCh.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/09/20170409744266_JuXbTN.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/04/20170404308601_CgHvpO.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/04/20170404308601_jhRfJH.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/04/20170404308602_tJFUOW.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/04/20170404308603_fLOgJp.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/04/20170404308603_wdhvSb.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/04/20170404308604_jbDPcG.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/04/20170404308601_CgHvpO.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/04/20170404308601_jhRfJH.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/04/20170404308602_tJFUOW.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/04/20170404308603_fLOgJp.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/04/20170404308603_wdhvSb.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/04/04/20170404308604_jbDPcG.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885698_pvFAJa.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885698_diCkpE.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885698_PnmEba.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885699_wiPQuj.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885699_uclZtU.jpg正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885700_kcDOCu.jpg
    
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885701_AaCLpW.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885702_sMPjAi.jpg正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885702_nhBDtH.jpg
    
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885698_pvFAJa.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885698_diCkpE.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885699_uclZtU.jpg正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885699_wiPQuj.jpg正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885698_PnmEba.jpg
    
    
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885700_kcDOCu.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885701_AaCLpW.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885702_sMPjAi.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/30/20170330885702_nhBDtH.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519140_KVdJoR.jpg正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519151_GwHMdV.jpg
    
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519151_OMwYbc.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519151_DAzsUj.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519151_SlpnAt.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519152_RFiUJt.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519152_fZxyea.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519152_qvIbFi.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519153_HsMcpi.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519140_KVdJoR.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519151_GwHMdV.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519151_OMwYbc.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519151_DAzsUj.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519151_SlpnAt.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519152_RFiUJt.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519152_fZxyea.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519152_qvIbFi.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/26/20170326519153_HsMcpi.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053791_KJbkrW.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053791_gMWhNc.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053792_gjdLIP.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053792_wbVSRP.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053792_MBNLKX.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053793_xzcVsl.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053793_zisFCN.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053793_IFPskz.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053793_BihjVt.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053791_KJbkrW.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053791_gMWhNc.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053792_gjdLIP.jpg正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053792_MBNLKX.jpg正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053792_wbVSRP.jpg
    
    
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053793_xzcVsl.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053793_zisFCN.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053793_IFPskz.jpg
    正在下载http://img.doutula.com/production/uploads/image/2017/03/21/20170321053793_BihjVt.jpg
    爬取结束
    
