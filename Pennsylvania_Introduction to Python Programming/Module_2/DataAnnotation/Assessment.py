import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"


def extractUrlData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find_all('tr', class_='c4')
    dataArr = []
    skip_count = 0
    for row in table:
        cells = row.find_all(['td'])
        for cell in cells:
            if cell.text.strip():
                if skip_count < 3:
                    skip_count += 1
                else:
                    dataArr.append(cell.text.strip())
                print(dataArr)
    print("123123123")
    resultArr = []
    for i in range(len(dataArr), 3):
        if i + 2 < len(dataArr):
            group_data = [dataArr[i], dataArr[i+1], dataArr[i+2]]
            resultArr.append(group_data)
    print(resultArr)
    return resultArr


extractUrlData(url)
    


