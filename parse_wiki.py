from bs4 import BeautifulSoup
import urllib
import urllib.request
import csv

soup=BeautifulSoup(urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_English_monarchs'))


for r in soup.select(".reference"):
	r.replace_with("")

table=[]
for a in soup.select(".wikitable td b a")[:-1]:
	name =a.text
	cell=a.find_parent("td")

	contents=cell.text.split("\n")

	try:
		date1 = contents[contents.index("-") - 1]
		date2 = contents[contents.index("-") + 1]
	except:
		date1 = contents[-3].replace("-","")
		date2 = contents[-2]
		print(contents)

	table.append([name.strip(),date1.strip(),date2.strip()])



with open("monarchs.csv","w",encoding="utf-8",newline="") as f:

	writer=csv.writer(f)
	writer.writerows(table)