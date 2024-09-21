from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 启动浏览器（需要相应的浏览器驱动）
driver = webdriver.Chrome()

# 打开一个空的 HTML 表单页面
driver.get("data:text/html,<html><body><form id='myForm' action='http://www.baidu.com' method='post'><input type='hidden' name='key1' value='value1'><input type='hidden' name='key2' value='value2'></form><script>document.getElementById('myForm').submit();</script></body></html>")

