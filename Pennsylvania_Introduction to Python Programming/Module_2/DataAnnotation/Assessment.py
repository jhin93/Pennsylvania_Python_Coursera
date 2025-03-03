import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"


def extractUrlData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    spanData = soup.select('table span')
    tagData =  spanData[3:]
    print("======================== tagData ========================", tagData)
    
    return tagData



extractUrlData(url)
    


