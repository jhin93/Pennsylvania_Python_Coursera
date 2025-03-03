import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

def extractUrlData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    spanData = soup.select('table span')
    tagData =  spanData[3:]
    
    # Extract the content from the tagData
    contentData = []
    for tag in tagData:
        contentData.append(tag.get_text())
    
    # Group the contentData into 3 items each
    groupingData = []
    for i in range(0, len(contentData), 3):
        eachGroup = [contentData[i], contentData[i+1], contentData[i+2]]
        groupingData.append(eachGroup)    

    return groupingData

rawData = extractUrlData(url)

# Set max y coordinate value
max_yCoordinate = 0
for group in rawData:
    max_yCoordinate = max(max_yCoordinate, int(group[2]))

# Set max x coordinate value
max_XCoordinate = 0
for group in rawData:
    max_XCoordinate = max(max_XCoordinate, int(group[0]))

# Set grid
grid = []
for y in range(max_yCoordinate + 1):
    row = []
    for x in range(max_XCoordinate + 1):
        row.append(' ') # making space inside of letters
    grid.append(row)

# Put shape into the grid
for group in rawData:
    x, shape, y = int(group[0]), group[1], int(group[2])
    grid[y][x] = shape

# Put the grid into the string and print it
for y in range(max_yCoordinate, -1, -1):
    blank = ""
    for x in range(len(grid[y])):
        blank += grid[y][x]
    print(blank)