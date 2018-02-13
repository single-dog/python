# -*- coding: utf-8 -*-  
import re
import urllib2

#下载爱给网的素材

# ------ 获取网页源代码的方法 ---
def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

# ------ getHtml()内输入任意帖子的URL ------
url = "http://www.aigei.com/view/72746.html?order=name&page="
maxPage = 15
saveDir = 'D:\\res\\boysgirls\\'


# ------ 获取帖子内所有图片地址的方法 ------
def getImg(html):
    # ------ 利用正则表达式匹配网页内容找到图片地址 ------
    print html
    reg = r"src='(.+?=)'"
    imgre = re.compile(reg);
    imglist = re.findall(imgre, html)
    return imglist

def down(imgList,page):
    imgName = 0
    for imgPath in imgList:
        # ------ 这里最好使用异常处理及多线程编程方式 ------
        try:
            pic_file = (urllib2.urlopen(imgPath)).read()
            f = open(saveDir+ str(page)+'-'+str(imgName)+".png", 'wb')
            f.write(pic_file)
            print(imgPath)
            f.close()
        except Exception as e:
            print(imgPath+e.message)
        imgName += 1
for page in xrange(1,maxPage):
    html = getHtml(url+str(page))
    # ------ 修改html对象内的字符编码为UTF-8 ------
    html = html.decode('UTF-8')
    urlList = getImg(html)
    down(urlList,page)

print("All Done!")