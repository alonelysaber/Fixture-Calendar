from bs4 import BeautifulSoup
import requests

# The main array for the teams URL
TEAMS = [
    '86/real-madrid',
    '360/manchester-united',
    '364/liverpool',
    '160/paris-saint-germain',
    '83/barcelona',
    '367/tottenham-hotspur',
    '132/bayern-munich',
]


def extract_team_name(content: bytes) -> str:
    soup = BeautifulSoup(content, 'html.parser')

    # Finding by class name
    return soup.find(class_='db fw-bold').text


def process_url(url: str) -> None:
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content, 'lxml')
    team1 = soup.select('div.local')[0].text
    team2 = soup.select('div.away')[0].text
    date = soup.select('div.matchTeams')[0].text
    time = soup.select('td.Table__TD')[4].text
    comp = soup.select('td.Table__TD')[5].text
    placement = soup.select('ul.list')[0].text

    main_team = extract_team_name(content).rstrip()

    bolded_main_team = f'\033[1m{main_team}\033[0m'

    print(f'• {bolded_main_team} vs {team2 if team1 == main_team else team1} on {date} at {time} in the {comp}')
    print(f'  {bolded_main_team} are {placement}\n')


def print_all_teams() -> None:
    for team in TEAMS:
        process_url(f'https://www.espn.in/football/team/fixtures/_/id/{team}')


if __name__ == '__main__':
    print_all_teams()
