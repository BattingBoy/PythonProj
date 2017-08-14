import urllib.request
import lxml.etree
import mysql_con

def read_html(html):
    page = lxml.etree.HTML(html)
    tags = page.xpath("//tr")
    for tag in tags:
        tds = tag.xpath("./td")
        temp = tag.xpath(".//em")
        if temp:
            con = mysql_con.mysql_con()
            data = [tds[0].text, tds[1].text, temp[0].text, temp[1].text, temp[2].text, temp[3].text, temp[4].text, temp[5].text, temp[6].text]
            data_dto = mysql_con.data_dto(data)
            con.insert(data_dto)
            print(tds[0].text, end=" ")
            print(tds[1].text, end=" ")
            for children in temp:
                print(children.text, end=" ")
            print()

if __name__ == "__main__":

    for i in range(2, 108):
        url = "http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp?pageNum=" + str(i)
        proxy_handler = urllib.request.ProxyHandler({'http': '10.17.171.11:8080'})
        opener = urllib.request.build_opener(proxy_handler)
        resp = opener.open(url)
        html = resp.read()
        read_html(html)


