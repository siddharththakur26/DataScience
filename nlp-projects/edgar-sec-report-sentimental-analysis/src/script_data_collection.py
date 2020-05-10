import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from bs4 import BeautifulSoup
import requests

# READ EXCEL FILE FOR THE URL LINKS #
df = pd.read_excel("cik_list.xlsx")
# print(df.columns)

# CREATED A LIST OF URLs #

prefix_url = "https://www.sec.gov/Archives/"
url_links = []
for i in df.index:
    # print(df['SECFNAME'][i])
    sufix_url = df["SECFNAME"][i]
    url = prefix_url + sufix_url
    url_links.append(url)
# print(url_links)

# EXTRACTING THE DATA FROM 152 EDGAR ARCHIVE FILES #

counter = 1
for url in url_links:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.text)
    file2write = open("sec_file_{}.txt".format(counter), "w+", encoding="UTF-8")
    counter += 1
    file2write.write(soup.text)
    file2write.close()

