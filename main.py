from bs4 import BeautifulSoup
import requests

response = requests.get("https://rcdb.com/rhr.htm?m=1&l=59")
coasters = response.text


soup = BeautifulSoup(markup=coasters, features="html.parser")

table = soup.find_all('table')[1]

coasters = table.find_all('tr')
coaster_list = []
heights = []
for coaster in coasters[1:]:
    coaster_name = coaster.a
    coaster_list.append(coaster_name.getText())
    height = coaster.span
    heights.append(height.getText())


with open("coasters.txt", "w") as file:
    file.write("Top 10 tallest roller coasters:\n")
    for i in range(len(coaster_list)):
        file.write(f"{i+1}. {coaster_list[i]} at {heights[i]}ft tall.\n")