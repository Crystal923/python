from bs4 import BeautifulSoup
import urllib.request
import os


# 下载图片
def img_download(path, img_url, name):
    import requests
    # print(img_url)
    r = requests.get(img_url)
    with open(path + name, 'wb') as f:
        f.write(r.content)


# 获取中铁一局网站图片
def get_crfeb():
    os.makedirs('./image/crfeb/', exist_ok=True)
    host = 'http://www.crfeb.com.cn'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    request = urllib.request.Request(host, headers=header)
    res = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(res, 'html.parser')
    a_list = soup.find_all('img')
    for item in a_list:
        img_url = item['src']
        url_list = img_url.split('/')
        name = url_list[len(url_list) - 1]
        img_download('./image/crfeb/', host + img_url, name)


# 获取奇步网站的图片
def get_qeebu():
    os.makedirs('./image/qeebu/', exist_ok=True)
    host = 'http://www.qeebu.com/'
    request = urllib.request.Request(host)
    res = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(res, 'html.parser')
    a_list = soup.find_all('img')
    for item in a_list:
        img_url = item['src']
        url_list = img_url.split('/')
        name = url_list[len(url_list) - 1]
        img_download('./image/qeebu/', host + img_url, name)


# 获取豆瓣热点内容图片数据，带有分页处理
def get_douban_photo():
    host = "https://www.douban.com/"
    request = urllib.request.Request(host)
    res = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(res, 'html.parser')
    # 首先在首页拿到了热点内容，以及进入每个热点内容的链接还有热点内容的名称
    href_list = soup.find('div', class_="albums").find_all('div', class_="pic")
    name_list = soup.find('div', class_='albums').find_all('a')
    # a标签有多个，在这里判断如果a标签中包含有图片信息  则从列表中删除
    for item in name_list:
        if len(item.find_all('img')) != 0:
            name_list.remove(item)
    # 这里共有四个热点内容，循环每个热点，获取详情中的图片
    for index, item in enumerate(href_list):
        print('每一项的页面地址：', item.find('a')['href'])
        photo_list = []
        # 详情中图片有分页，需要循环去除每页的内容，这里不知道到底分了多少页，所以循环条件设置为True,直到拿不到数据之后跳出循环
        while True:
            a_url = item.find('a')['href'] + '?start=' + str(len(photo_list))
            a_list = BeautifulSoup(urllib.request.urlopen(
                urllib.request.Request(a_url)).read(),
                                   'html.parser').find_all('div', class_='photo_wrap')
            photo_list = photo_list + a_list
            if len(a_list) == 0:
                break
        print(len(photo_list))
        # 下载每个热点的图片资源
        for photo in photo_list:
            img_url = photo.find('img')['src']
            url_list = img_url.split('/')
            name = url_list[len(url_list) - 1]
            os.makedirs('./image/douban/' + str(name_list[index].string) + '/', exist_ok=True)
            img_download('./image/douban/' + str(name_list[index].string) + '/', img_url, name)

# get_crfeb()
# get_qeebu()
get_douban_photo()
