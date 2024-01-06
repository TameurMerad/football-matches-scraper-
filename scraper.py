import requests
from bs4 import BeautifulSoup
import csv



date = input("Enter Date following this format MM/DD/YYYY : ")


page = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}")

def main(page):
    src = page.content
    # print(src)
    soup = BeautifulSoup(src, "lxml")
    # print(soup)
    championship = soup.find_all("div", {"class": "matchCard"})
    print(championship)
    
main(page)
