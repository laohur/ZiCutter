# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, csv, time, random,re

since = time.time()
link0="https://bj.zu.anjuke.com/fangyuan/l1-p6/?kw=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&cw=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6"
link1="https://bj.zu.anjuke.com/fangyuan/l1-p"
link2="/?kw=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&cw=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6"
agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'

refer="https://bj.zu.anjuke.com/fangyuan/l1/?kw=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&cw=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6"
#取得所有详情页连接
links=[]  
for i in range(1,8):
    url=link1+str(i)+link2
    headers={'User-Agent':agent ,'referer':refer }
    html=requests.get(url,headers=headers)
    soup=BeautifulSoup(html.text,'lxml')
    items=[]
    items=soup.find_all('div',class_='zu-itemmod')
    for item in items:
        link=item.get('link')
        links.append(link)
        print(link)
    time.sleep(random.random()*3)
    refer=url

file = open("D:/data/items.csv","a+", newline='',encoding='utf_8_sig')    #创建文件  encoding='utf-8'
writer = csv.writer(file)       #写入对象  
fields=['link','类型','地铁','right-info','rent','pay','户型','面积','朝向','楼层','装修','类型','小区','地区','地名','床', '洗衣机', '空调', '阳台', '冰箱', '卫生间', '可做饭', '电视', '更多', '热水器', '衣柜', '暖气', '宽带', '沙发']
writer.writerow(fields) 

refer="https://bj.zu.anjuke.com/fangyuan/l1/?kw=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&cw=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6"
#详情页中每个字段存入行记录
for no in range(0,len(links)):
    url=links[no]
    headers={'User-Agent':agent ,'referer':refer }    
    html=requests.get(url,headers=headers)
    soup=BeautifulSoup(html.text,'lxml')
    fields=['']*15 #行记录,前14列固定
    fields[0]=url
    #添加类型1列 fields[1]
    if soup.find('li',class_="title-label-item rent"):   fields[1]= soup.find('li',class_="title-label-item rent").get_text()
    #添加地铁1列 fileds[2]
    if soup.find('li',class_="title-label-item subway"):   fields[2]= soup.find('li',class_="title-label-item subway").get_text()
    
    #添加时间1列 fields[3]
    if soup.find('div',class_="right-info"):   fields[3]= soup.find('div',class_="right-info").get_text()
    
    #添加租金2列 fields[4:5]
    if soup.find('ul',class_="house-info-zufang cf"): 
        rent=soup.find('ul',class_="house-info-zufang cf").find_all('span')
        for i in range(0,len(rent)):
            if i<2: fields[4+i]=rent[i].get_text()

    #添加房屋信息6列fileds[6:11] 户型 面积 朝向 楼层 装修 类型
    if soup.find_all('span', class_='info') :    
        house=soup.find_all('span', class_='info')
        for i in range(0,len(house)):
            if i<6: fields[6+i]=house[i].get_text() 
    
    #添加地址3列 fields[12:14] 添加小区、地区、地名
    if soup.find_all('a',attrs={"_soj":"propview"}): 
        address=soup.find_all('a',attrs={"_soj":"propview"})
        for i in range(0,len(address)):
            if i<3: fields[12+i]=address[i].get_text()
    
    #添加标签组
    if soup.find_all('div',class_='peitao-info'):
        tags=soup.find_all('div',class_='peitao-info')
        for tag in tags:
            if tag.find_parent('li',class_=re.compile("has")) :
                support=1
            else:
                support=0
            fields.append(support)
    writer.writerow(fields)
    print(fields)
    time.sleep(random.random()*3)
    refer=url

file.close()

print(time.time() - since)
print("s elapsed!")