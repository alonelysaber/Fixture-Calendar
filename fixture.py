from bs4 import BeautifulSoup
import requests
import os

os.system('color')

    
def realmadrid():
    url = "https://www.espn.in/football/team/fixtures/_/id/86/real-madrid"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "lxml") 
    
    team1 = soup.select('div.local')[0].text 
    team2 = soup.select('div.away')[0].text
    date = soup.select('div.matchTeams')[0].text
    time = soup.select('td.Table__TD')[4].text
    comp = soup.select('td.Table__TD')[5].text
    placement = soup.select('ul.list')[0].text
    
    date_time_comp = ' on ' + date + ' at ' + time + ' in the ' + comp
    
    main_team = "Real Madrid"

    bolded_main_team = "\033[1m" + main_team + "\033[0m"
    
    if team1 == main_team:
        print('• ' + bolded_main_team + ' vs ' + team2 + date_time_comp)
    else:
        print('• ' + bolded_main_team + ' vs ' + team1 + date_time_comp)
        
    print('  ' + 'Real Madrid are ' + placement)
        
    

def manu():
    url = "https://www.espn.in/football/team/fixtures/_/id/360/manchester-united"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "lxml") 
    
    team1 = soup.select('div.local')[0].text 
    team2 = soup.select('div.away')[0].text
    date = soup.select('div.matchTeams')[0].text
    time = soup.select('td.Table__TD')[4].text
    comp = soup.select('td.Table__TD')[5].text
    placement = soup.select('ul.list')[0].text
    date_time_comp = ' on ' + date + ' at ' + time + ' in the ' + comp
    
    main_team = "Manchester United"

    bolded_main_team = "\033[1m" + main_team + "\033[0m"
    
    if team1 == main_team:
        print('• ' + bolded_main_team + ' vs ' + team2 + date_time_comp)
    else:
        print('• ' + bolded_main_team + ' vs ' + team1 + date_time_comp)
        
    print('  ' + 'Manchester United are ' + placement)
        
def liverpool():
    url = "https://www.espn.in/football/team/fixtures/_/id/364/liverpool"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "lxml") 
    
    team1 = soup.select('div.local')[0].text 
    team2 = soup.select('div.away')[0].text
    date = soup.select('div.matchTeams')[0].text
    time = soup.select('td.Table__TD')[4].text
    comp = soup.select('td.Table__TD')[5].text
    placement = soup.select('ul.list')[0].text

    
    date_time_comp = ' on ' + date + ' at ' + time + ' in the ' + comp
    main_team = 'Liverpool'

    bolded_main_team = "\033[1m" + main_team + "\033[0m"

    if team1 == main_team:
         print('• ' + bolded_main_team + ' vs ' + team2 + date_time_comp)
    else:
        print('• ' + bolded_main_team + ' vs ' + team1 + date_time_comp)
        
    print('  ' + 'Liverpool are ' + placement)


def psg():
    url = "https://www.espn.in/football/team/fixtures/_/id/160/paris-saint-germain"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "lxml") 
    
    team1 = soup.select('div.local')[0].text 
    team2 = soup.select('div.away')[0].text
    date = soup.select('div.matchTeams')[0].text
    time = soup.select('td.Table__TD')[4].text
    comp = soup.select('td.Table__TD')[5].text
    placement = soup.select('ul.list')[0].text
    
    date_time_comp = ' on ' + date + ' at ' + time + ' in the ' + comp
    
    main_team = 'Paris Saint-Germain '

    bolded_main_team = "\033[1m" + main_team + "\033[0m"

    if team1 == main_team:
           print('• ' + bolded_main_team + ' vs ' + team2 + date_time_comp)

    else:
          print('• ' + bolded_main_team + ' vs ' + team1 + date_time_comp)
          
    print('  ' + 'PSG are ' + placement)

def barca():
    url = "https://www.espn.in/football/team/fixtures/_/id/83/barcelona"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "lxml") 
    
    team1 = soup.select('div.local')[0].text 
    team2 = soup.select('div.away')[0].text
    date = soup.select('div.matchTeams')[0].text
    time = soup.select('td.Table__TD')[4].text
    comp = soup.select('td.Table__TD')[5].text
    placement = soup.select('ul.list')[0].text

    
    date_time_comp = ' on ' + date + ' at ' + time + ' in the ' + comp

    main_team = 'Barcelona'

    bolded_main_team = "\033[1m" + main_team + "\033[0m"
    
    if team1 == main_team:
        print('• ' + bolded_main_team + ' vs ' + team2 + date_time_comp)
    else:
        print('• ' + bolded_main_team + ' vs ' + team1 + date_time_comp)
        
    print('  ' + 'Barcelona are ' + placement)

def hotspur():
    url = "https://www.espn.in/football/team/fixtures/_/id/367/tottenham-hotspur"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "lxml") 
    
    team1 = soup.select('div.local')[0].text 
    team2 = soup.select('div.away')[0].text
    date = soup.select('div.matchTeams')[0].text
    time = soup.select('td.Table__TD')[4].text
    comp = soup.select('td.Table__TD')[5].text
    placement = soup.select('ul.list')[0].text

    
    date_time_comp = ' on ' + date + ' at ' + time + ' in the ' + comp

    main_team = "Tottenham Hotspur"

    bolded_main_team = "\033[1m" + main_team + "\033[0m"
    
    if team1 == main_team:
        print('• ' + bolded_main_team + ' vs ' + team2 + date_time_comp)
        
    else:
        print('• ' + bolded_main_team + ' vs ' + team1 + date_time_comp)
        
    print('  ' + 'Tottenham Hotspur are ' + placement)

def bayern():
    url = "https://www.espn.in/football/team/fixtures/_/id/132/bayern-munich"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "lxml") 
    
    team1 = soup.select('div.local')[0].text 
    team2 = soup.select('div.away')[0].text
    date = soup.select('div.matchTeams')[0].text
    time = soup.select('td.Table__TD')[4].text
    comp = soup.select('td.Table__TD')[5].text
    placement = soup.select('ul.list')[0].text
    
    date_time_comp = ' on ' + date + ' at ' + time + ' in the ' + comp

    main_team = 'Bayern Munich'

    bolded_main_team = "\033[1m" + main_team + "\033[0m"

    if team1 == main_team:
        print('• ' + bolded_main_team + ' vs ' + team2 + date_time_comp)
        
    else:
        print('• ' + bolded_main_team + ' vs ' + team1 + date_time_comp)
    
    print('  ' + 'Bayern Munich are ' + placement)



realmadrid()
print("")
manu()
print("")
liverpool()
print("")
psg()
print("")
barca()
print("")
hotspur()
print("")
bayern()


input()
