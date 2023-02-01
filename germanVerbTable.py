import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from colorama import Fore, Back, Style

# Make a GET request to the website
istek = input("Enter a verb: ")
url = f"https://en.pons.com/verb-tables/german/{istek}"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
# Find all the tables with class "ft-single-table"
tables = soup.find_all("div", class_="ft-single-table")
# Loop through each table to extract the header and data
data = []
for table in tables:
    for row in table.find("tbody").find_all("tr"):
        columns = [col.text for col in row.find_all("td")]
        data.append(columns)

#txt
f = open("dieFolgen.txt", "w+")

datas = []
def Maker(istek):
    try:
        for i in range(6):
            if i == 0:
                col_names = ["Personel Pronomen", "Präsens"]
                karts = data[0:6]
            elif i == 1:
                col_names = ["Personel Pronomen", "Präteritum"]
                karts = data[6:12]
            elif i == 2:
                col_names = ["Personel Pronomen", "Perfekt"]
                karts = data[12:18]
            elif i == 3:
                col_names = ["Personel Pronomen", "Plusquamperfekt"]
                karts = data[18:24]
            elif i == 4:
                col_names = ["Personel Pronomen", "Futur I"]
                karts = data[24:30]
            elif i == 5:
                col_names = ["Personel Pronomen", "Futur II"]
                karts = data[30:36]

            a = len(karts[0])
            datas = []
            if(a == 2):
                for i in karts:
                    datas.append([i[0], i[1]])
            elif(a == 3):            
                for i in karts:
                    datas.append([i[0], i[1] + " " + i[2]])
            elif(a == 4):
                for i in karts:
                    datas.append([i[0], i[1] + " " + i[2] + " " + i[3]])
            
            f.write(tabulate(datas, headers=col_names, tablefmt="fancy_grid"))
            f.write("\n")
            print(tabulate(datas, headers=col_names, tablefmt="fancy_grid"))
    except:
        print(f"{istek} could not be found")

Maker(istek)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
url = f"https://context.reverso.net/translation/german-english/{istek}"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

tablesDE = soup.find_all("div", class_="src ltr")
tablesEN = soup.find_all("div", class_="trg ltr")

c = 0
for index in range(len(tablesDE)):
    if(c == 10):
        break
    textDE = tablesDE[index].find("span", class_="text").text
    textEN = tablesEN[index].find("span", class_="text").text
    textDEEM = tablesDE[index].find("em").text
    textENEM = tablesEN[index].find("em").text
    print(textDE + "\033[33m" + f"{textDEEM}" + "\033[0m", end="")
    f.write(textDE + "( "+ f"{textDEEM}" + " )" )
    print(textEN + "\033[33m" + f"{textENEM}" + "\033[0m")
    f.write(textEN + "( " + f"{textENEM}" + " )")
    f.write("\n")
    print()
    c += 1
