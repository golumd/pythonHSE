def viberi_turik(spisok):
    n = 1
    print("Турниры на выбор: ")
    for i in spisok:
        print(n, i)
        n += 1
    nomer = int(input(f"Введите номер нужного турнира (от 1 до {n - 1}): "))
    while 1:
        if nomer in range(n):
            break
        else:
            nomer = int(input(f"Введите номер выбранного турнира еще раз (от 1 до {n - 1}): "))
    turnir = spisok_csv[nomer - 1]
    return turnir


# выбираем турнир из списка турниров


def viberi_pravila(rules):
    n = 1
    print("Правила на выбор: ")
    for i in rules:
        print(n, i)
        n += 1
    nomer = int(input(f"Введите номер выбранного правила ранжирования (от 1 до {n - 1}): "))
    while 1:
        if nomer in range(n):
            break
        else:
            nomer = int(input(f"Введите номер выбранного правила ранжирования еще раз (от 1 до {n - 1}): "))
    rule = rules_func[nomer - 1]
    return rule


# выбираем правила из списка правил


def Read_table(file_name):
    table = []
    with open(file_name) as f:
        for line in f:
            data = []
            list = line.split(',')
            date, home, away, home_goals, away_goals = list[1:6]
            data.append(date), data.append(home), data.append(away), data.append(home_goals), data.append(away_goals)
            table.append(data)
    return table


# считываем таблицу


def Matches_of_team(team_name):
    games = []
    for line in table:
        if line[1] == team_name or line[2] == team_name:
            games.append(line)
    return games


# закидываем игры определенной команды в список


def Show_Matches_of_team(team_name):
    print(f"Games of {team_name}:")
    columns_names = ['Date', 'Home team name', 'Away team name', 'Home team goals', 'Away team goals']
    games = Matches_of_team(team_name)
    if games:
        row_format = "{:>22}" * (len(columns_names))
        print(row_format.format(*columns_names))
        for game in games:
            print(row_format.format(*game))
    else:
        print("No such team", end=2 * "\n")


# принтим матчи команды в нужном формате (выравнены столбцы)


def Matches_by_date(date):
    games = []
    for line in table:
        if line[0] == date:
            games.append(line)
    return games


# Матчи в опеределенный день


def Show_Matches_by_date(date):
    print(f"Games {date}:")
    columns_names = ['Date', 'Home team', 'Away team', 'Home team goals', 'Away team goals']
    games = Matches_by_date(date)
    if games:
        row_format = "{:>22}" * (len(columns_names))
        print(row_format.format(*columns_names))
        for game in games:
            print(row_format.format(*game))
    else:
        print("No games in this day", end=2 * "\n")


# принтим матчи


def teams_info(table):
    teams = []
    for line in table[1:]:
        t = [line[1], 0, 0, 0, 0, 0, 0, 0]  # назв[0], игр[1], wins[2], draws[3], loses[4], разн[5], забитых[6], очки[7]
        if t not in teams:
            teams.append(t)
    for team in teams:
        for line in table[1:]:
            if team[0] == line[1]:
                team[1] += 1
                team[6] += int(line[3])
                team[5] += (int(line[3]) - int(line[4]))
                if int(line[3]) > int(line[4]):
                    team[2] += 1
                elif int(line[3]) == int(line[4]):
                    team[3] += 1
                else:
                    team[4] += 1
            elif team[0] == line[2]:
                team[1] += 1
                team[6] += int(line[4])
                team[5] += (int(line[4]) - int(line[3]))
                if int(line[4]) > int(line[3]):
                    team[2] += 1
                elif int(line[3]) == int(line[4]):
                    team[3] += 1
                else:
                    team[4] += 1
    for team in teams:
        team[7] = team[2] * 3 + team[3] * 2 + team[4] * 1
    return teams


# создем информативную таблицу по командам (графы таблицы см. в комментарии внутри кода)


def sorting_1(table):
    teams_info_1 = teams_info(table)
    teams_info_1.sort(key=lambda x: (x[7], x[5], x[6]))
    teams_info_1.reverse()
    i = 1
    teams_info_1[0].insert(0, i)
    for t in range(1, len(teams_info_1)):
        if teams_info_1[t - 1][5] == teams_info_1[t][5] and teams_info_1[t - 1][6] == teams_info_1[t][6] \
                and teams_info_1[t - 1][7] == teams_info_1[t][7]:
            teams_info_1[t].insert(0, i)
        else:
            i += 1
            teams_info_1[t].insert(0, i)
    return teams_info_1


# сортировка таблицы по правилу №1


def sorting_2(table):
    teams_info_1 = teams_info(table)
    teams_info_1.sort(key=lambda x: (x[7], x[2], x[5]))
    teams_info_1.reverse()
    i = 1
    teams_info_1[0].insert(0, i)
    for t in range(1, len(teams_info_1)):
        if teams_info_1[t - 1][5] == teams_info_1[t][5] and teams_info_1[t - 1][2] == teams_info_1[t][2] \
                and teams_info_1[t - 1][7] == teams_info_1[t][7]:
            teams_info_1[t].insert(0, i)
        else:
            i += 1
            teams_info_1[t].insert(0, i)
    return teams_info_1


# сортировка таблицы по правилу №2


def Show_sorted_teams(table):
    teams = rule_of_sorting(table)
    columns_names = ["Place", "Name", "Games", "Wins", "Draws", "Loses", "difference", "goals", "points"]
    row_format = "{:>22}" * (len(columns_names))
    print("Table of teams: ")
    print(row_format.format(*columns_names))
    for team in teams:
        print(row_format.format(*team))


spisok = ["Premier League 2011-2012", "Premier League 2012-1013", "Premier League 2013-2014"]
spisok_csv = ['premier_league_11-12.csv', 'premier_league_12-13.csv', 'premier_league_13-14.csv']
file_name = viberi_turik(spisok)
rules = ["Правила №1 (см. текстовый файл)", "Правила №2 (см. текстовый файл)"]
rules_func = [sorting_1, sorting_2]
rule_of_sorting = viberi_pravila(rules)
try:
    table = Read_table(file_name)
except:
    print("Something goes wrong")
try:
    Show_Matches_of_team("Milan")
except:
    print("Something goes wrong")
try:
    Show_Matches_by_date("18/08/12")
except:
    print("Something goes wrong")
try:
    Show_sorted_teams(table)
except:
    print("Something goes wrong")
