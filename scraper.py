import requests
from bs4 import BeautifulSoup
import csv



date = input("Enter Date following this format MM/DD/YYYY : ")


page = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}")
matches_infos = []


def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    championships = soup.find_all("div", {"class": "matchCard"})
    championships_number = len(championships)
    
    for i in range(championships_number):
        championship_name = championships[i].contents[1].find("h2").text.strip()
        matches = championships[i].find_all("div", {"class": "liItem"})
        
        matches_number = len(matches)
        # print(matches_number)
        
        
        # print(championship_name)
        
        
        for j in range(matches_number):
            teamA = matches[j].find('div', {'class': 'teamsData'}).find('div', {'class': 'teamA'}).text.strip()
            # print(teamA)
            teamB = matches[j].find('div', {'class': 'teamsData'}).find('div', {'class': 'teamB'}).text.strip()
            
            score = matches[j].find('div', {'class': 'teamsData'}).find('div', {'class': 'MResult'}).find_all("span",{'class': 'score'})
            scoreA = score[0].text.strip()
            scoreB = score[1].text.strip()
            
            time = matches[j].find('div', {'class': 'teamsData'}).find('div', {'class': 'MResult'}).find('span',{'class': 'time'}).text.strip()
            match_info = {
                "championship": championship_name,
                "teamA": teamA,
                "teamB": teamB,
                "scoreA": scoreA,
                "scoreB": scoreB,
                "time": time
            }
            matches_infos.append(match_info)
            # print(match_info)
            
    # print(matches_infos)
    with open('matches.csv', 'w', encoding='utf-8', newline='') as csv_file:
        fieldnames = ['championship', 'teamA', 'teamB', 'scoreA', 'scoreB', 'time']
        dict_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(matches_infos)
        
        print("Done")

            
    
            
        
    
    
        
main(page)    
