from selenium import webdriver


browser=webdriver.Chrome("chromedriver")
browser.get("https://reddit.com")


titles_text=[]

for i in range(3):
	titles=browser.find_elements_by_css_selector("a.title.outbound")
	titles_text += [t.text for t in titles]

	next = browser.find_element_by_css_selector(".next-button a")
	next.click()

print(titles_text)