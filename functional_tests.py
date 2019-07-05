from selenium import webdriver

print("IMPORTOU SELENIUM WEBDRIVER")

browser = webdriver.Firefox()

browser.get("http://localhost:8000")

assert 'Django' in browser.title

browser.close()