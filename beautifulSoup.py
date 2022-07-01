from bs4 import BeautifulSoup
import requests


class Suman:
    url1 = "https://www.zenclass.in/class"
    data = requests.get(url1)
    soup = BeautifulSoup(data.content, 'lxml')


    def lefthand(self):
            list = []

            for data in self.soup.findAll('div', class_='session-container'):
                list_lefthand = data.find('div', class_='preread-head')
                list.append(list_lefthand.text)

            print(list)
            print("-------------------------------------------------------------------")




s = Suman()

s.lefthand()
