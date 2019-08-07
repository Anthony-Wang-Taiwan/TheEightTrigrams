import requests
from bs4 import BeautifulSoup

for i in range(1, 2):
    url = "https://www.eee-learning.com/simple64/1"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')
    class_field_item_even_tag = soup.find('div', {'class': 'field-item even'})
    class_tr_tags = class_field_item_even_tag.select('tr')

    contant = ""
    # The first tag is a img.
    td_tags = class_tr_tags[0].find_all('td')
    contant = contant + td_tags[1].text + td_tags[2].text + '\n'

    for tag in class_tr_tags[1:]:
        td_tags = tag.find_all('td')
        contant = contant + td_tags[0].text + td_tags[1].text + '\n'
    
    with open(str(i)+".txt", 'w') as file:
        file.write(contant)
