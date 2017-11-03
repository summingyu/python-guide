import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://112.124.22.37:19001/lt/task.do")
bsObj = BeautifulSoup(html,'html5lib')
#主对比表格是当前页面的第一个表格
table = bsObj.findAll("table")[0]
rows = table.findAll("tr")


csvFile = open("./downloaded/Chapter5_2.csv",'wt',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
