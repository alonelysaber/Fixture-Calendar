from bs4 import BeautifulSoup
from requests import get

# The main array for the teams URL
TEAMS = ["86/real-madrid", "360/manchester-united", "364/liverpool", "160/paris-saint-germain", "83/barcelona",
         "367/tottenham-hotspur", "132/bayern-munich"]


def team_name(url):
    req = get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    # Finding by class name
    return soup.find(class_="db fw-bold").text


def parser(url):
    page = get(url)
    soup = BeautifulSoup(page.content, "lxml")
    team1 = soup.select("div.local")[0].text
    team2 = soup.select("div.away")[0].text
    date = soup.select("div.matchTeams")[0].text
    time = soup.select("td.Table__TD")[4].text
    comp = soup.select("td.Table__TD")[5].text
    placement = soup.select("ul.list")[0].text

    date_time_comp = " on " + date + " at " + time + " in the " + comp

    main_team = team_name(url).rstrip()

    bolded_main_team = "\033[1m" + main_team + "\033[0m"

    if team1 == main_team:
        print("• " + bolded_main_team + " vs " + team2 + date_time_comp)
    else:
        print('• ' + bolded_main_team + " vs " + team1 + date_time_comp)

    print("  " + f"{bolded_main_team} are " + placement)


def team_parser(team):
    if int(team) < len(TEAMS) + 1:
        url = f"https://www.espn.in/football/team/fixtures/_/id/{TEAMS[int(team) - 1]}"
        parser(url)
    else:
        count = 0
        while len(TEAMS) > count:
            url = f"https://www.espn.in/football/team/fixtures/_/id/{TEAMS[count]}"
            parser(url)
            count += 1


if __name__ == '__main__':
    while True:
        team_selection = input(
            "Please select a team by indicating the number: \n 1. Real Madrid \n 2. Manchester United \n 3. Liverpool "
            "\n 4. PSG \n 5. Barcelona \n 6. Tottenham Hotspurs \n 7. Bayern Munich \n 8. All teams \n")
        if team_selection.isnumeric() and int(team_selection) in range(1, len(TEAMS) + 2):
            team_parser(team_selection)
            break
        else:
            print("Invalid input, please try again")
