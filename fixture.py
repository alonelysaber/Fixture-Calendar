"""
Welcome to my first serious python project 
I will be trying to build a program that lets me know when a football team's next fixture is without needing
to google again and again for it.
The basic idea is for the program to make a google search about the fixture whenever I ask for it
If the barebones program works well, I may have date to implement a neat GUI to go with it.
Let the hacking begin
Update: 1:43 am 25 oct. All basic funcionality seems good. Program is working as expected. Next step will be to
upload to github and hopefully scale this up to a gui output using basic tkinter.
"""

from bs4 import BeautifulSoup
import requests
import webbrowser


#my_team = input('Enter the name of the team: ')

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
    

    if team1 == "Real Madrid":
        print('Real Madrid will play ' + team2 + date_time_comp)
        print('Real Madrid are ' + placement)
    else:
        print('Real Madrid will play ' + team1 + date_time_comp)
        print('Real Madrid are ' + placement)
        
    #webbrowser.open_new(url)

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
    

    if team1 == "Manchester United":
        print('Manchester United will play ' + team2 + date_time_comp)
        print('Manchester United are ' + placement)
    else:
        print('Manchester United will play ' + team1 + date_time_comp)
        print('Manchester United are ' + placement)
        
    #webbrowser.open_new(url)
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

    if team1 == "Liverpool":
         print('Liverpool will play ' + team2 + date_time_comp)
         print('Liverpool are ' + placement)
    else:
        print('Liverpool will play ' + team1 + date_time_comp)
        print('Liverpool are ' + placement)
    #webbrowser.open_new(url)


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

    if team1 == "Paris Saint-Germain ":
           print('Paris Saint Germain will play ' + team2 + date_time_comp)
           print('PSG are ' + placement)

    else:
          print('Paris Saint Germain will play ' + team1 + date_time_comp)
          print('PSG are ' + placement)
    #webbrowser.open_new(url)

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

    if team1 == "Barcelona":
        print('Barcelona will play ' + team2 + date_time_comp)
        print('Barcelona are ' + placement)
    else:
        print('Barcelona will play ' + team1 + date_time_comp)
        print('Barcelona are ' + placement)
    #webbrowser.open_new(url)

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

    if team1 == "Tottenham Hotspur":
        print('Tottenham Hotspur will play ' + team2 + date_time_comp)
        print('Tottenham Hotspur are ' + placement)
    else:
        print('Tottenham Hotspur will play ' + team1 + date_time_comp)
        print('Tottenham Hotspur are ' + placement)
    #webbrowser.open_new(url)




realmadrid()
manu()
liverpool()
psg()
barca()
hotspur()
'''if my_team == "real madrid":
    realmadrid()
elif my_team =='manchester united':
    manu()
elif my_team == 'liverpool':
    liverpool()
elif my_team == 'psg' :
    psg()
elif my_team == 'barcelona':
    barca()
elif my_team =='hotspur':
    hotspur()
elif my_team =='all':
    realmadrid()
    manu()
    liverpool()
    psg()
    barca()
    hotspur()
else:
    print('Invalid input.')'''

input()


