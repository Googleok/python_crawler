import time

from selenium import webdriver

wd = webdriver.Chrome('D:\cafe24\libs\chromedriver\chromedriver.exe')
wd.get('http://goobne.co.kr/store/search_store.jsp')

time.sleep(2)
html = wd.page_source
print(html)

wd.quit()
